import uuid
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from dotenv import load_dotenv
import os


from langchain_openai import ChatOpenAI

from src.knowledge_base import KnowledgeBase
from src.vector_visualizer import VectorVisualizer
from src.config import MODEL


class AITutorCore:
    def __init__(self):
        load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
        
        self.progress_file = "progress_tracking.json"
        self.KB = KnowledgeBase()
        self.visualizer = None
        self.memory = MemorySaver()
        self.workflow = StateGraph(state_schema=MessagesState)
        self.model = ChatOpenAI(temperature=0.7, model=MODEL)
        self.thread_id = str(uuid.uuid4())
        
        self._setup_workflow()

    def _setup_workflow(self):
        self.workflow.add_edge(START, "model")
        self.workflow.add_node("model", self._call_model)
        self.app = self.workflow.compile(checkpointer=self.memory)

    def _call_model(self, state: MessagesState):
        response = self.model.invoke(state["messages"])
        return {"messages": response}

    def chat_with_tutor(self, message, history):
        if self.KB.vectorstore is None:
            reply = "Knowledge base not initialized. Please click 'Initialize Knowledge Base' first."
            return reply
        
        retriever = self.KB.vectorstore.as_retriever(search_kwargs={"k": 10})
        relevant_docs = retriever.get_relevant_documents(message)
        context = "\n\n".join(doc.page_content for doc in relevant_docs)
        
        print("question:",message)
        for i, doc in enumerate(relevant_docs):
            print(i, ":", doc.page_content)

        chat_history = "\n".join(
            f"{msg['role'].capitalize()}: {msg['content']}" for msg in history
        )

        system_prompt = f"""
You are an expert, friendly AI tutor. Always reply in English. Use the provided context and your own pretrained knowledge to answer the student's question in a clear, concise, and educational way.

- If the answer is in the context, explain it step by step, using examples if helpful.
- If the answer is not in the context, but you know it from your own training, answer clearly and mention that you are using your general knowledge.
- If you truly do not know the answer, say "I don't know based on the provided materials or my training."
- If the student asks for a summary, provide a structured summary from the context.
- If the student asks for a quiz, create a few multiple-choice questions with answers and explanations.
- Always encourage curiosity and deeper understanding.
- **Always reply in English, even if the question is in another language.**

Context:
{context}

Chat History:
{chat_history}

Question:
{message}

Answer:
"""

        messages = [SystemMessage(content=system_prompt)]
        for msg in history:
            if msg["role"] == "user":
                messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                messages.append(AIMessage(content=msg["content"]))
        messages.append(HumanMessage(content=message))
        
        config = {"configurable": {"thread_id": self.thread_id}}
        
        for event in self.app.stream({"messages": messages}, config, stream_mode="values"):
            last_msg = event["messages"][-1]
            answer = last_msg.content if hasattr(last_msg, "content") else str(last_msg)

        return answer

    def initialize_kb_and_visualizer(self):
        result = self.KB.initialize_knowledge_base()
        print(self.KB.vectorstore._collection)
        self.visualizer = VectorVisualizer(self.KB.vectorstore)
        return result
    
    def add_data_to_db(self, data_type, path):
        if data_type == "Add file":
            self.KB.add_file(path)
        elif data_type == "Add folder":
            self.KB.add_folder(path)
        else:
            "Select"

    def show_visualization(self, vis_type):
        if not self.visualizer:
            return "Initialize knowledge base first"
        
        if vis_type == "2D Visualization":
            self.visualizer.visualize_2d()
            return "2D visualization displayed"
        elif vis_type == "3D Visualization":
            self.visualizer.visualize_3d()
            return "3D visualization displayed"
        else:
            return "Select a visualization type"

