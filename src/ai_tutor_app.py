import gradio as gr
from dotenv import load_dotenv
import os

from src.config import MODEL
from src.knowledge_base import KnowledgeBase 
from src.vector_visualizer import VectorVisualizer
from src.ai_tutor_core import AITutorCore


class AITutorApp:
    def __init__(self):
        load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
        self.core = AITutorCore()
        self.demo = self._create_interface()

    def initialize_kb_and_visualizer(self, dummy=None):
        return self.core.initialize_kb_and_visualizer()

    def add_data_to_db(self, data_type, path):
        return self.core.add_data_to_db(data_type, path)

    def show_visualization(self, vis_type):
        return self.core.show_visualization(vis_type)

    def chat_with_tutor(self, message, history):
        return self.core.chat_with_tutor(message, history)

    def _create_interface(self):
        with gr.Blocks(title="Your personal AI Tutor") as demo:
            gr.Markdown("Your personal AI Tutor")
            gr.Markdown("Your personalized learning companion with progress tracking!")
            
            with gr.Row():
                with gr.Column(scale=3):
                    chatbot = gr.Chatbot(type="messages", placeholder="Ask me anything about your courses!")
                    gr.ChatInterface(fn=self.chat_with_tutor, chatbot=chatbot)

                with gr.Column(scale=1):
                    dummy = gr.Textbox(visible=False)
                    Initialize_btn = gr.Button("Initialize Knowledge Base")
                    Add_data_btn = gr.Button("Add data into DB")
                    data_dropdown = gr.Dropdown(
                        choices=["Add file", "Add folder"],
                        label="Choose",
                        value="Add folder"
                    )

                    path_input = gr.Textbox(label="Path to file or folder")

                    system_output = gr.Textbox(label="System Output", interactive=False)
            
            with gr.Row():
                with gr.Column():
                    vis_dropdown = gr.Dropdown(
                        choices=["2D Visualization", "3D Visualization"],
                        label="Select Visualization",
                        value="2D Visualization"
                    )
                    show_vis_btn = gr.Button("Show Visualization")
                    vis_output = gr.Textbox(label="Visualization", interactive=False)

            Initialize_btn.click(
                self.initialize_kb_and_visualizer,
                inputs=dummy,
                outputs=system_output
            )
            
            show_vis_btn.click(
                self.show_visualization,
                inputs=vis_dropdown,
                outputs=vis_output
            )

            Add_data_btn.click(
                self.add_data_to_db,
                inputs=[data_dropdown,path_input],
                outputs=system_output
            )
        return demo

    def launch(self):
        self.demo.launch()


if __name__ == "__main__":
    tutor_app = AITutorApp()
    tutor_app.launch()

