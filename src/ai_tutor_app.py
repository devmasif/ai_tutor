import gradio as gr
import requests
import json
import uuid
from datetime import datetime
from src.ai_tutor_core import AITutorCore

class AITutorApp:
    def __init__(self):
        self.core = None  # Will be initialized when user logs in
        self.backend_url = "http://localhost:8000"
        self.token = None
        self.current_user = None
        self.current_user_id = None
        self.current_session_id = str(uuid.uuid4())
        self.demo = self._create_interface()

    def register_user(self, username, password, email):
        try:
            response = requests.post(f"{self.backend_url}/register", json={
                "username": username,
                "password": password,
                "email": email
            })
            
            if response.status_code == 200:
                data = response.json()
                self.token = data["token"]
                self.current_user = data["user"]
                self.current_user_id = data["user"]["id"]
                
                # Initialize core with user ID
                try:
                    self.core = AITutorCore(user_id=self.current_user_id)
                    print(f"[INFO] Initialized AI Tutor for user: {username} (ID: {self.current_user_id})")
                except Exception as e:
                    print(f"[ERROR] Failed to initialize core for user {username}: {e}")
                    return f"✅ Registered but failed to initialize personal AI: {str(e)}", gr.update(), gr.update()
                
                return f"✅ Registered successfully! Welcome, {username}!", gr.update(visible=False), gr.update(visible=True)
            else:
                return f"❌ Registration failed: {response.json().get('detail', 'Unknown error')}", gr.update(), gr.update()
        except Exception as e:
            return f"❌ Connection error: {str(e)}", gr.update(), gr.update()

    def login_user(self, username, password):
        try:
            response = requests.post(f"{self.backend_url}/login", json={
                "username": username,
                "password": password
            })
            
            if response.status_code == 200:
                data = response.json()
                self.token = data["token"]
                self.current_user = data["user"]
                self.current_user_id = data["user"]["id"]
                
                # Initialize core with user ID
                try:
                    self.core = AITutorCore(
                        user_id=self.current_user["id"],        
                        username=self.current_user["username"]  
                    )
                    print(f"[INFO] Initialized AI Tutor for user: {username} (ID: {self.current_user_id})")
                except Exception as e:
                    print(f"[ERROR] Failed to initialize core for user {username}: {e}")
                    return f"✅ Logged in but failed to initialize personal AI: {str(e)}", gr.update(), gr.update()
                
                return f"✅ Welcome back, {username}!", gr.update(visible=False), gr.update(visible=True)
            else:
                return f"❌ Login failed: {response.json().get('detail', 'Invalid credentials')}", gr.update(), gr.update()
        except Exception as e:
            return f"❌ Connection error: {str(e)}", gr.update(), gr.update()

    def logout_user(self):
        # Clean up core resources
        if self.core:
            try:
                self.core.close()
                print(f"[INFO] Closed AI Tutor for user: {self.current_user_id}")
            except Exception as e:
                print(f"[WARNING] Error closing core: {e}")
        
        self.token = None
        self.current_user = None
        self.current_user_id = None
        self.current_session_id = str(uuid.uuid4())
        self.core = None
        
        return "👋 Logged out successfully!", gr.update(visible=True), gr.update(visible=False)

    def chat_with_tutor(self, message, history):
        """Enhanced chat with progress tracking"""
        if not self.token or not self.core:
            return "⚠️ Please login first to use the AI Tutor."
        
        try:
            # Get AI response from core
            ai_response = self.core.chat_with_tutor(message, history)
            
            # Generate progress analysis prompt
            progress_prompt = f"""
Based on this learning interaction, analyze the user's progress and generate a JSON progress report.

User ID: {self.current_user_id}
User Question: {message}
AI Response: {ai_response}

Generate a progress analysis in this exact JSON format:
{{
    "topics_covered": ["topic1", "topic2"],
    "difficulty_level": "beginner/intermediate/advanced",
    "learning_insights": "Brief insight about user's understanding",
    "weak_areas": ["area1", "area2"],
    "strong_areas": ["area1", "area2"],
    "recommendations": "What the user should focus on next"
}}

Only return the JSON, nothing else.
"""
            
            # Get progress analysis from AI
            progress_response = self.core.model.invoke([{"role": "user", "content": progress_prompt}])
            progress_text = progress_response.content
            
            # Try to parse JSON from AI response
            try:
                # Extract JSON from response (in case AI adds extra text)
                start = progress_text.find('{')
                end = progress_text.rfind('}') + 1
                if start != -1 and end != 0:
                    progress_json = json.loads(progress_text[start:end])
                else:
                    progress_json = {"error": "Could not parse progress data"}
            except:
                progress_json = {"error": "Failed to generate progress data"}
            
            # Log to backend
            if self.token:
                self._log_session_to_backend(message, ai_response, progress_json)
                
        except Exception as e:
            print(f"Progress tracking error for user {self.current_user_id}: {e}")
            return f"AI Error for user {self.current_user_id}: {str(e)}"
        
        return ai_response

    def _log_session_to_backend(self, user_message, ai_response, progress_data):
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            requests.post(f"{self.backend_url}/log_session", 
                json={
                    "session_id": self.current_session_id,
                    "user_message": user_message,
                    "ai_response": ai_response,
                    "progress_data": progress_data
                },
                headers=headers
            )
        except Exception as e:
            print(f"Failed to log session for user {self.current_user_id}: {e}")

    def get_user_progress(self):
        """Get user progress from backend"""
        if not self.token:
            return "⚠️ Please login to view progress."
        
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.get(f"{self.backend_url}/progress", headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                
                # Get document count from MongoDB
                doc_count = self.core.get_user_document_count() if self.core else 0
                
                progress_text = f"""
📊 **Your Learning Progress** (User: {self.current_user.get('username', 'Unknown')})

📈 **Stats:**
• Total Sessions: {data.get('total_sessions', 0)}
• Documents in Knowledge Base: {doc_count}
• Current Session: {self.current_session_id[:8]}...
• User ID: {self.current_user_id[:8]}...

🎯 **Strong Areas:** {', '.join(data.get('strong_topics', ['None yet']))}

⚠️ **Areas to Improve:** {', '.join(data.get('weak_topics', ['None identified']))}

📚 **Recent Learning:**
"""
                
                for item in data.get('recent_progress', [])[:3]:
                    progress = item.get('progress', {})
                    timestamp = item.get('timestamp', '')
                    progress_text += f"\n• {timestamp[:10]}: {progress.get('learning_insights', 'Learning session')}"
                
                return progress_text
            else:
                return "❌ Could not fetch progress data."
        except Exception as e:
            return f"❌ Error fetching progress: {str(e)}"

    def get_kb_status(self):
        """Get current knowledge base status"""
        if not self.core:
            return f"⚠️ AI Tutor not initialized. Please login first."
        
        return self.core.get_kb_status()

    def add_files_to_kb(self, files):
        """Add uploaded files to knowledge base"""
        if not self.core:
            return "⚠️ Please login first to upload files."
        
        if not files:
            return "⚠️ No files selected."
        
        try:
            results = []
            for file in files:
                if hasattr(file, 'name'):
                    file_path = file.name
                else:
                    file_path = str(file)
                
                result = self.core.add_content_to_kb(file_path)
                results.append(f"📄 {file_path}:\n{result}")
            
            return "\n\n".join(results)
        except Exception as e:
            return f"❌ Error adding files for user {self.current_user_id}: {str(e)}"

    def show_visualization(self, vis_type):
        """Show vector visualization"""
        return self.core.show_visualization(vis_type)
    

    def clear_knowledge_base(self):
        """Clear the entire knowledge base"""
        if not self.core:
            return "⚠️ Please login first."
        
        
        try:
            result = self.core.clear_knowledge_base()
            return f"✅ {result}"
        except Exception as e:
            return f"❌ Error clearing knowledge base for user {self.current_user_id}: {str(e)}"

    def _create_interface(self):
        with gr.Blocks(title="AI Tutor - Your Personal Learning Assistant", theme=gr.themes.Soft()) as demo:
            gr.Markdown("# 🤖 AI Tutor - Your Personal Learning Assistant")
            
            # Authentication section
            auth_section = gr.Column(visible=True)
            main_section = gr.Column(visible=False)
            
            with auth_section:
                gr.Markdown("## 🔐 Login or Register to Start Learning")
                gr.Markdown("*Each user gets their own secure knowledge base in MongoDB*")
                
                with gr.Tabs():
                    with gr.Tab("Login"):
                        login_username = gr.Textbox(label="Username", placeholder="Enter your username")
                        login_password = gr.Textbox(label="Password", type="password", placeholder="Enter your password")
                        login_btn = gr.Button("🚀 Login", variant="primary")
                        
                    with gr.Tab("Register"):
                        reg_username = gr.Textbox(label="Username", placeholder="Choose a username")
                        reg_email = gr.Textbox(label="Email", placeholder="Enter your email")
                        reg_password = gr.Textbox(label="Password", type="password", placeholder="Create a password")
                        register_btn = gr.Button("📝 Register", variant="primary")
                
                auth_message = gr.Textbox(label="Status", interactive=False)
            
            # Main application
            with main_section:
                with gr.Row():
                    gr.Markdown(f"### 🎓 Welcome to your Personal AI Learning Session!")
                    logout_btn = gr.Button("🚪 Logout", size="sm")
                
                with gr.Row():
                    # Chat section
                    with gr.Column(scale=3):
                        chatbot = gr.Chatbot(
                            type="messages", 
                            placeholder="💬 Ask me anything about your uploaded documents! Your knowledge base is private and secure in MongoDB.",
                            height=400
                        )
                        gr.ChatInterface(
                            fn=self.chat_with_tutor, 
                            chatbot=chatbot,
                            title=""
                        )
                    
                    # Control & Progress panel
                    with gr.Column(scale=1):
                        # Progress section
                        gr.Markdown("### 📊 Your Progress")
                        progress_display = gr.Textbox(
                            label="Learning Progress", 
                            lines=10, 
                            interactive=False,
                            value="Login and start chatting to see your progress!"
                        )
                        refresh_progress_btn = gr.Button("🔄 Refresh Progress")
                        
                        # Knowledge Base Management
                        gr.Markdown("### 📚 Personal Knowledge Base (MongoDB)")
                        
                        # KB Status
                        kb_status = gr.Textbox(
                            label="Knowledge Base Status", 
                            interactive=False, 
                            lines=4,
                            value="Please login to access your personal knowledge base"
                        )
                        refresh_kb_btn = gr.Button("🔄 Refresh Status")
                        
                        # Content Addition
                        gr.Markdown("#### 📁 Add Content")
                        
                        # File Upload Section
                        upload_files_btn = gr.UploadButton(
                            "➕ Upload Files", 
                            file_types=[".pdf", ".docx", ".pptx", ".xls", ".xlsx", ".txt", ".zip"],
                            file_count="multiple",
                            variant="primary"
                        )

                        # Visualization
                        gr.Markdown("#### Vector Visualization")
                        vis_dropdown = gr.Dropdown(
                            choices=["2D Visualization", "3D Visualization"],
                            label="Visualization Type",
                            value="2D Visualization"
                        )
                        show_vis_btn = gr.Button("📈 Show Visualization")
                        vis_output = gr.Textbox(label="Visualization Status", interactive=False)
                        
                        # System output
                        system_output = gr.Textbox(label="System Messages", interactive=False, lines=4)
                        
                        # Management
                        gr.Markdown("#### 🗑️ Management")
                        clear_kb_btn = gr.Button("🗑️ Clear My Knowledge Base", variant="stop")
                        


            # Event handlers
            login_btn.click(
                self.login_user,
                inputs=[login_username, login_password],
                outputs=[auth_message, auth_section, main_section]
            ).then(
                self.get_kb_status,
                outputs=kb_status
            )
            
            register_btn.click(
                self.register_user,
                inputs=[reg_username, reg_password, reg_email],
                outputs=[auth_message, auth_section, main_section]
            ).then(
                self.get_kb_status,
                outputs=kb_status
            )
            
            logout_btn.click(
                self.logout_user,
                outputs=[auth_message, auth_section, main_section]
            )
            
            refresh_progress_btn.click(
                self.get_user_progress,
                outputs=progress_display
            )
            
            refresh_kb_btn.click(
                self.get_kb_status,
                outputs=kb_status
            )
            
            show_vis_btn.click(
                self.show_visualization,
                inputs=vis_dropdown,
                outputs=vis_output
            )

            # File upload handlers
            upload_files_btn.upload(
                self.add_files_to_kb,
                inputs=upload_files_btn,
                outputs=system_output
            ).then(
                self.get_kb_status,
                outputs=kb_status
            )
            
            clear_kb_btn.click(
                self.clear_knowledge_base,
                outputs=system_output
            ).then(
                self.get_kb_status,
                outputs=kb_status
            )
        
        return demo

    def launch(self):
        print("🚀 Starting AI Tutor App with MongoDB Backend...")
        print("📝 Make sure the FastAPI backend is running on http://localhost:8000")
        print("🗄️ MongoDB connection will be established per user")
        
        # Enable live reload for Gradio UI
        self.demo.launch(share=False, debug=True)


    def __del__(self):
        """Cleanup on app deletion"""
        if self.core:
            try:
                self.core.close()
            except Exception as e:
                print(f"[WARNING] Error during cleanup: {e}")