from fastapi import FastAPI, HTTPException, Depends, status 
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from pymongo import MongoClient
import bcrypt
from datetime import datetime, timedelta
import jwt
import os
import uuid
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# FastAPI app
app = FastAPI(title="AI Tutor Backend - MongoDB Edition")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()
SECRET_KEY = os.getenv("MY_SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("MY_SECRET_KEY is not set. Check your .env")

ALGORITHM = os.getenv("ALGORITHM")
TOKEN_EXPIRE_HOURS = int(os.getenv("TOKEN_EXPIRE_HOURS"))

MONGO_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGO_URI)
db = client.ai_tutor_db


# Collections
users = db.users
sessions = db.sessions
subjects = db.subjects
# Vector collections will be created dynamically per user

# Pydantic models
class UserRegister(BaseModel):
    username: str
    password: str
    email: str

class UserLogin(BaseModel):
    username: str
    password: str

class ProgressSession(BaseModel):
    session_id: str
    user_message: str
    ai_response: str
    progress_data: Dict[str, Any]  

class User(BaseModel):
    id: str
    username: str
    email: str

class VectorStats(BaseModel):
    user_id: str
    collection_name: str
    total_documents: int
    embedding_dimensions: int
    document_types: Dict[str, int]

# Helper functions
def create_token(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=TOKEN_EXPIRE_HOURS)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
  
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def get_user_vector_collection(user_id: str):
    """Get the vector collection for a specific user"""
    collection_name = f"user_vectors_{user_id}"
    return db[collection_name]

# Routes

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

@app.post("/register")
async def register(user_data: UserRegister):
    if users.find_one({"$or": [{"username": user_data.username}, {"email": user_data.email}]}):
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_id = str(uuid.uuid4())
    user_doc = {
        "_id": user_id,
        "username": user_data.username,
        "email": user_data.email,
        "password_hash": hash_password(user_data.password),  
        "created_at": datetime.utcnow(),
        "vector_collection": f"user_vectors_{user_id}"  # Track user's vector collection
    }
    
    users.insert_one(user_doc)
    token = create_token(user_id)
    
    # Initialize empty vector collection for user
    try:
        vector_collection = get_user_vector_collection(user_id)
        # Create initial index for the collection
        vector_collection.create_index([
            ("user_id", 1),
            ("doc_type", 1),
            ("created_at", -1)
        ])
        print(f"[INFO] Created vector collection for user: {user_id}")
    except Exception as e:
        print(f"[WARNING] Could not initialize vector collection for user {user_id}: {e}")
    
    return {"message": "User registered", "token": token, "user": {"id": user_id, "username": user_data.username}}

@app.post("/login")
async def login(user_data: UserLogin):
    user = users.find_one({"username": user_data.username})
    if not user or not verify_password(user_data.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token(user["_id"])
    return {"message": "Login successful", "token": token, "user": {"id": user["_id"], "username": user["username"]}}

@app.get("/me")
async def get_current_user(user_id: str = Depends(verify_token)):
    user = users.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"id": user["_id"], "username": user["username"], "email": user["email"]}

@app.post("/log_session")
async def log_session(session_data: ProgressSession, user_id: str = Depends(verify_token)):
    session_doc = {
        "_id": str(uuid.uuid4()),
        "user_id": user_id,
        "session_id": session_data.session_id,
        "user_message": session_data.user_message,
        "ai_response": session_data.ai_response,
        "progress_data": session_data.progress_data,
        "timestamp": datetime.utcnow()
    }
    
    sessions.insert_one(session_doc)
    return {"message": "Session logged successfully"}

@app.get("/progress")
async def get_progress(user_id: str = Depends(verify_token)):
    recent_sessions = list(sessions.find(
        {"user_id": user_id}
    ).sort("timestamp", -1).limit(10))
    
    total_sessions = sessions.count_documents({"user_id": user_id})
    
    all_progress = []
    weak_topics = set()
    strong_topics = set()
    
    for session in recent_sessions:
        progress = session.get("progress_data", {})
        all_progress.append({
            "timestamp": session["timestamp"],
            "progress": progress
        })
        
        if "weak_areas" in progress and isinstance(progress["weak_areas"], list):
            weak_topics.update(progress["weak_areas"])
        if "strong_areas" in progress and isinstance(progress["strong_areas"], list):
            strong_topics.update(progress["strong_areas"])
    
    return {
        "total_sessions": total_sessions,
        "recent_progress": all_progress,
        "weak_topics": list(weak_topics),
        "strong_topics": list(strong_topics)
    }

# Vector Database specific endpoints

@app.get("/vector_stats")
async def get_vector_stats(user_id: str = Depends(verify_token)):
    """Get statistics about user's vector database"""
    try:
        vector_collection = get_user_vector_collection(user_id)
        
        total_docs = vector_collection.count_documents({"user_id": user_id})
        
        # Get document types distribution
        doc_types_pipeline = [
            {"$match": {"user_id": user_id}},
            {"$group": {"_id": "$doc_type", "count": {"$sum": 1}}}
        ]
        doc_types = list(vector_collection.aggregate(doc_types_pipeline))
        doc_types_dict = {dt["_id"]: dt["count"] for dt in doc_types}
        
        # Get embedding dimensions from sample document
        sample = vector_collection.find_one({"user_id": user_id, "embedding": {"$exists": True}})
        dimensions = len(sample["embedding"]) if sample and "embedding" in sample else 0
        
        return {
            "user_id": user_id,
            "collection_name": f"user_vectors_{user_id}",
            "total_documents": total_docs,
            "embedding_dimensions": dimensions,
            "document_types": doc_types_dict
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting vector stats: {str(e)}")

@app.delete("/clear_vectors")
async def clear_user_vectors(user_id: str = Depends(verify_token)):
    """Clear all vectors for the authenticated user"""
    try:
        vector_collection = get_user_vector_collection(user_id)
        result = vector_collection.delete_many({"user_id": user_id})
        
        return {
            "message": f"Cleared {result.deleted_count} vectors for user {user_id}",
            "deleted_count": result.deleted_count
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error clearing vectors: {str(e)}")

@app.get("/vector_collections")
async def list_vector_collections():
    """List all vector collections (admin endpoint)"""
    try:
        collections = db.list_collection_names()
        vector_collections = [col for col in collections if col.startswith("user_vectors_")]
        
        collection_stats = []
        for col_name in vector_collections:
            collection = db[col_name]
            count = collection.count_documents({})
            user_id = col_name.replace("user_vectors_", "")
            
            # Get username
            user = users.find_one({"_id": user_id})
            username = user["username"] if user else "Unknown"
            
            collection_stats.append({
                "collection_name": col_name,
                "user_id": user_id,
                "username": username,
                "document_count": count
            })
        
        return {
            "total_collections": len(vector_collections),
            "collections": collection_stats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error listing collections: {str(e)}")

# Subject management (existing endpoints)
from fastapi import Body

@app.post("/subjects/add")
async def add_subject(subject: str = Body(...), user_id: str = Depends(verify_token)):
    subject = subject.strip().lower()
    if not subject:
        raise HTTPException(status_code=400, detail="Subject name required")
    
    # Check if subject exists for this user
    if subjects.find_one({"name": subject, "user_id": user_id}):
        return {"message": "Subject already exists for user"}
    
    subjects.insert_one({
        "name": subject,
        "user_id": user_id,
        "created_at": datetime.utcnow()
    })
    return {"message": "Subject added", "subject": subject}

@app.get("/subjects")
async def get_user_subjects(user_id: str = Depends(verify_token)):
    """Get subjects for the authenticated user"""
    subject_list = [s["name"] for s in subjects.find({"user_id": user_id}, {"_id": 0, "name": 1})]
    return {"subjects": subject_list}

@app.get("/subjects/all")
async def get_all_subjects():
    """Get all subjects across all users (admin endpoint)"""
    subject_list = list(subjects.find({}, {"_id": 0, "name": 1, "user_id": 1}))
    return {"subjects": subject_list}

# Health check endpoint
@app.get("/health")
async def health_check():
    try:
        # Test MongoDB connection
        db.command("ping")
        
        # Count total users and collections
        total_users = users.count_documents({})
        all_collections = db.list_collection_names()
        vector_collections = [col for col in all_collections if col.startswith("user_vectors_")]
        
        return {
            "status": "healthy",
            "mongodb": "connected",
            "total_users": total_users,
            "vector_collections": len(vector_collections),
            "timestamp": datetime.utcnow()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    import threading, webbrowser, time

    host = "0.0.0.0"
    port = 8000

    def open_swagger():
        time.sleep(1.0)
        webbrowser.open(f"http://127.0.0.1:{port}/docs")

    print("🚀 Starting AI Tutor Backend with MongoDB Vector Support")
    print(f"📊 MongoDB URI: {MONGO_URI}")
    print("🗄️ Each user gets their own vector collection")
    
    threading.Thread(target=open_swagger, daemon=True).start()
    uvicorn.run(app, host=host, port=port)