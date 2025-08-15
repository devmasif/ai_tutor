import uuid
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_mongodb import MongoDBAtlasVectorSearch  

from src.knowledge_base import MongoKnowledgeBase 
from src.vector_visualizer import VectorVisualizer
from src.config import MODEL


class AITutorCore:
    def __init__(self, user_id: str = None, username: str = None):
        load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
        
        self.user_id = user_id
        self.username = username
        
        # Initialize MongoDB-based Knowledge Base with per-user collection
        try:
            self.KB = MongoKnowledgeBase(
                user_id=self.user_id,
                username=self.username
            )
            print(f"[INFO] MongoDB Knowledge Base initialized for user: {self.username}")
            print(f"[INFO] User collection: {self.KB.collection_name}")
        except Exception as e:
            print(f"[ERROR] Failed to initialize MongoDB Knowledge Base: {e}")
            self.KB = None
        
        # Initialize workflow components
        self.memory = MemorySaver()
        self.workflow = StateGraph(state_schema=MessagesState)
        self.model = ChatOpenAI(temperature=0.7, model=MODEL)
        self.thread_id = str(uuid.uuid4())
        self.history = []
        self.visualizer = None
        self._setup_workflow()
        self._initialize_visualizer_if_needed()

    def _setup_workflow(self):
        self.workflow.add_edge(START, "model")
        self.workflow.add_node("model", self._call_model)
        self.app = self.workflow.compile(checkpointer=self.memory)

    def _call_model(self, state: MessagesState):
        response = self.model.invoke(state["messages"])
        return {"messages": response}
    
    def _initialize_visualizer_if_needed(self):
        """Initialize visualizer if knowledge base exists"""
        if self.KB and self.KB.vectorstore is not None:  
            try:
                self.visualizer = VectorVisualizer(self.KB.vectorstore)
                print(f"[INFO] Vector visualizer initialized for user: {self.username}")
            except Exception as e:
                print(f"[WARNING] Could not initialize visualizer for user {self.username}: {e}")
        else:
            print(f"[INFO] No vectorstore available for user {self.username}")
    
    def debug_documents(self):
        """Debug function to check what documents exist - SIMPLIFIED"""
        if not self.KB or not self.KB.vectorstore:
            print("[DEBUG] No knowledge base available")
            return
        
        try:
            collection = self.KB.collection
            
            # Count total documents in user's collection
            total_docs = collection.count_documents({})
            print(f"[DEBUG] Total documents in user collection '{self.KB.collection_name}': {total_docs}")
            
            # Show sample document structure
            sample_doc = collection.find_one({})
            if sample_doc:
                print(f"[DEBUG] Sample document structure:")
                print(f"  - _id: {sample_doc.get('_id')}")
                print(f"  - content: {sample_doc.get('content', '')[:100]}...")
                print(f"  - metadata: {sample_doc.get('metadata', {})}")
                print(f"  - has embedding: {'embedding' in sample_doc}")
            else:
                print(f"[DEBUG] No documents found in user collection")
                
        except Exception as e:
            print(f"[DEBUG] Debug failed: {e}")
    
    def chat_with_tutor(self, message, history):
        """Enhanced chat function with improved per-user collection retrieval"""
        self.history = history if history else []
        
        # Debug documents first
        self.debug_documents()
        
        # Try to retrieve from knowledge base if available - MUCH SIMPLER NOW
        context = ""
        retrieval_info = ""
        
        if self.KB and self.KB.vectorstore:
            try:
                print(f"[DEBUG] Attempting retrieval from collection: {self.KB.collection_name}")
                
                # Direct similarity search - no user filtering needed!
                relevant_docs = self.KB.similarity_search_with_user_filter(message, k=5)
                
                if relevant_docs:
                    context = "\n\n".join(doc.page_content for doc in relevant_docs)
                    print(f"[DEBUG] Retrieved {len(relevant_docs)} relevant documents")
                    
                    # Log first few characters of each document for debugging
                    for i, doc in enumerate(relevant_docs):
                        print(f"[DEBUG] Doc {i+1}: {doc.page_content[:100]}...")
                    
                    retrieval_info = f"Based on your uploaded documents (User: {self.username})"
                else:
                    print(f"[DEBUG] No relevant documents found for user {self.username}")
                    retrieval_info = "No relevant documents found in your knowledge base"
                    
            except Exception as e:
                print(f"[ERROR] Retrieval failed for user {self.username}: {e}")
                retrieval_info = "Retrieval failed, using general knowledge"
        else:
            retrieval_info = f"No knowledge base available for user {self.username}, using general knowledge"

        # Build chat history for context
        chat_history = "\n".join(
            f"{msg['role'].capitalize()}: {msg['content']}" for msg in self.history
        ) if self.history else "No previous conversation"

        # Create system prompt based on whether we found relevant content
        if context.strip():
            system_prompt = f"""
You are AI Tutor Assistant, an AI-powered educational companion for User: {self.username}
Your role is to teach, test, and track — providing accurate help from uploaded content
and encouraging improvement through intelligent feedback.

🎯 Key Principle: Always distinguish between information from uploaded documents vs. general AI knowledge.

🧠 Core Behaviors:
📂 Document-Based Assistance
- Prioritize information from uploaded documents
- When using document context, clearly indicate "Based on your uploaded documents..."
- If document context is insufficient, combine with general knowledge and indicate both sources

📝 Quiz Generation & Evaluation
- Generate quizzes based on document content when available
- DO NOT provide answers immediately after quiz questions
- Evaluate responses and provide detailed feedback
- Identify weak areas and suggest improvements

📈 Progress Tracking & Reporting
- Track learning patterns and difficulties
- Provide progress summaries when requested
- Offer personalized recommendations

🎯 Communication Style:
- Be supportive, clear, and educational
- Ask clarifying questions when needed
- Focus on helping users learn and improve
- Always output equations in plain-text math form

Context from your uploaded documents:
{context}

Chat History:
{chat_history}

Question: {message}

Answer (remember to indicate source - documents vs general knowledge):
"""
        else:
            system_prompt = f"""
You are AI Tutor Assistant, an AI-powered educational companion for User: {self.username}

🎯 Current Status: {retrieval_info}

🧠 Core Behaviors:
📚 General Knowledge Assistance
- Provide helpful educational support using general AI knowledge
- Clearly indicate "Based on general knowledge..." when appropriate
- If user asks about specific documents, explain that no relevant documents were found

📝 Educational Support
- Help with learning and understanding concepts
- Generate practice questions when appropriate
- Provide clear explanations and examples

🎯 Communication Style:
- Be supportive, clear, and educational
- Ask clarifying questions when needed
- Focus on helping users learn and improve
- Always output equations in plain-text math form

Chat History:
{chat_history}

Question: {message}

Answer (based on general knowledge):
"""

        # Prepare messages for the model
        messages = [SystemMessage(content=system_prompt)]
        for msg in self.history:
            if msg["role"] == "user":
                messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                messages.append(AIMessage(content=msg["content"]))
        messages.append(HumanMessage(content=message))
        
        config = {"configurable": {"thread_id": self.thread_id}}
        
        try:
            for event in self.app.stream({"messages": messages}, config, stream_mode="values"):
                last_msg = event["messages"][-1]
                answer = last_msg.content if hasattr(last_msg, "content") else str(last_msg)

            print(f"[DEBUG] Response generated for user {self.username}. Context used: {bool(context.strip())}")
            return answer
            
        except Exception as e:
            print(f"[ERROR] Chat generation failed for user {self.username}: {e}")
            return f"Sorry, I encountered an error while processing your request: {str(e)}"
        
    def add_content_to_kb(self, path):
        """Add content to knowledge base from file, folder, or ZIP"""
        if not self.KB:
            return f"Error: Knowledge base not initialized for user {self.username}"
        
        try:
            result = self.KB.add_content(path)
            print(f"[INFO] Content added to KB for user {self.username}")

            if self.KB.vectorstore is not None:
                try:
                    self.visualizer = VectorVisualizer(self.KB.vectorstore)
                    print("[INFO] Vector visualizer refreshed after adding content.")
                except Exception as e:
                    print(f"[WARNING] Could not refresh visualizer: {e}")
            
            return result
            
        except Exception as e:
            return f"Error adding content for user {self.username}: {str(e)}"
    
    def show_visualization(self, vis_type):
        """Show vector visualization"""
        if self.KB.vectorstore is None:
            return "No knowledge base available. Please add some content first."
            
        if not self.visualizer:
            try:
                self.visualizer = VectorVisualizer(self.KB.vectorstore)
            except Exception as e:
                return f"Could not initialize visualizer: {str(e)}"
        
        try:
            if vis_type == "2D Visualization":
                self.visualizer.visualize_2d()
                return "2D visualization displayed"
            elif vis_type == "3D Visualization":
                self.visualizer.visualize_3d()
                return "3D visualization displayed"
            else:
                return "Please select a visualization type (2D or 3D)"
        except Exception as e:
            return f"Visualization failed: {str(e)}"

    def get_kb_status(self):
        """Get current knowledge base status"""
        if not self.KB:
            return f"Knowledge base not initialized for user {self.username}"
        
        try:
            return self.KB.investigate_vectors()
        except Exception as e:
            return f"Error getting KB status for user {self.username}: {str(e)}"

    def clear_knowledge_base(self):
        """Clear the entire knowledge base for this user"""
        if not self.KB:
            return f"Knowledge base not initialized for user {self.username}"
        
        try:
            result = self.KB.clear_knowledge_base()
            print(f"[INFO] Knowledge base cleared for user {self.username}")
            
            # Reinitialize visualizer after clearing
            self._initialize_visualizer_if_needed()
            
            return result
        except Exception as e:
            return f"Error clearing KB for user {self.username}: {str(e)}"

    def get_directory_summary(self, path):
        """Get directory structure summary"""
        if not self.KB:
            return f"Knowledge base not initialized for user {self.username}"
        
        return self.KB.get_directory_summary(path)
    
    def get_user_document_count(self):
        """Get total document count for this user"""
        if not self.KB:
            return 0
        
        try:
            return self.KB.get_user_document_count()
        except Exception as e:
            print(f"Error getting document count for user {self.username}: {e}")
            return 0
    
    def set_user(self, user_id, username=None):
        """Set user and reinitialize knowledge base and visualizer"""
        try:
            # Close existing connections
            self.close()
            
            # Set new user info
            self.user_id = user_id
            self.username = username or user_id
            
            # Reinitialize KB for new user (will create new collection)
            self.KB = MongoKnowledgeBase(user_id=user_id, username=self.username)
            print(f"[INFO] MongoDB Knowledge Base reinitialized for user: {self.username}")
            print(f"[INFO] New user collection: {self.KB.collection_name}")
            
            # Reinitialize visualizer
            self._initialize_visualizer_if_needed()
            
            # Reset other user-specific data
            self.history = []
            self.thread_id = str(uuid.uuid4())  # New thread for new user
            
            return f"Successfully switched to user: {self.username} (Collection: {self.KB.collection_name})"
            
        except Exception as e:
            print(f"[ERROR] Failed to switch user to {self.username}: {e}")
            return f"Error switching to user {self.username}: {str(e)}"
        
    def close(self):
        """Close knowledge base connection"""
        if self.KB:
            try:
                self.KB.close()
                print(f"[INFO] Closed KB connection for user {self.username}")
            except Exception as e:
                print(f"[WARNING] Error closing KB for user {self.username}: {e}")

    def __del__(self):
        """Ensure cleanup on deletion"""
        self.close()
    
    # Admin functions for managing multiple users
    def list_all_user_collections(self):
        """List all user collections in the database (admin function)"""
        if not self.KB:
            return "Knowledge base not initialized"
        
        try:
            collections = self.KB.list_user_collections()
            if not collections:
                return "No user collections found in the database"
            
            result = f"Found {len(collections)} user collections:\n"
            for collection in collections:
                try:
                    # Get document count for each collection
                    col_ref = self.KB.mongo_client[self.KB.db_name][collection]
                    doc_count = col_ref.count_documents({})
                    result += f"- {collection}: {doc_count} documents\n"
                except Exception as e:
                    result += f"- {collection}: Error getting count ({e})\n"
            
            return result
            
        except Exception as e:
            return f"Error listing user collections: {str(e)}"
    
    def get_database_statistics(self):
        """Get comprehensive database statistics (admin function)"""
        if not self.KB:
            return "Knowledge base not initialized"
        
        try:
            stats = self.KB.get_database_stats()
            
            if "error" in stats:
                return f"Error getting database stats: {stats['error']}"
            
            result = "=== DATABASE STATISTICS ===\n\n"
            
            # Database level stats
            db_stats = stats.get("database_stats", {})
            result += f"Database: {self.KB.db_name}\n"
            result += f"Total Collections: {db_stats.get('collections', 'N/A')}\n"
            result += f"Total Documents: {db_stats.get('objects', 'N/A')}\n"
            result += f"Database Size: {db_stats.get('dataSize', 0) / (1024*1024):.2f} MB\n"
            result += f"Index Size: {db_stats.get('indexSize', 0) / (1024*1024):.2f} MB\n\n"
            
            # User collections stats
            user_collections = stats.get("user_collections", {})
            result += f"=== USER COLLECTIONS ({len(user_collections)}) ===\n"
            
            total_user_docs = 0
            total_user_size = 0
            
            for collection_name, col_stats in user_collections.items():
                if "error" in col_stats:
                    result += f"❌ {collection_name}: {col_stats['error']}\n"
                else:
                    docs = col_stats.get('documents', 0)
                    size_mb = col_stats.get('size_bytes', 0) / (1024*1024)
                    indexes = col_stats.get('index_count', 0)
                    
                    total_user_docs += docs
                    total_user_size += col_stats.get('size_bytes', 0)
                    
                    result += f"✅ {collection_name}:\n"
                    result += f"   Documents: {docs:,}\n"
                    result += f"   Size: {size_mb:.2f} MB\n"
                    result += f"   Indexes: {indexes}\n\n"
            
            result += f"=== TOTALS ===\n"
            result += f"Total User Documents: {total_user_docs:,}\n"
            result += f"Total User Data Size: {total_user_size / (1024*1024):.2f} MB\n"
            
            return result
            
        except Exception as e:
            return f"Error getting database statistics: {str(e)}"