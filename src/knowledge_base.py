from src.document_processor import DocumentProcessor
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from src.config import db_name
import os


class KnowledgeBase:
    def __init__(self):
        self.vectorstore = None
        self.db_name = db_name
        self.doc_processor = DocumentProcessor()  

    def create_vector_store(self):
        base_path = "E:\\New folder\\Rag_Tutor\\knowledge_base\\test_data"

        # Build directory summary for Gradio output
        summary_lines = []
        for root, dirs, files in os.walk(base_path):
            indent = "  " * (root[len(base_path):].count(os.sep))
            summary_lines.append(f"{indent}{os.path.relpath(root, base_path)}/")
            for d in dirs:
                summary_lines.append(f"{indent}  {d}/")
            for f in files:
                summary_lines.append(f"{indent}  {f}")
        summary = "\n".join(summary_lines)

        all_documents = self.doc_processor.load_document_from_folders(base_path)

        if not all_documents:
            return f"{summary}\n\nNo Documents Found"
        
        chunks = self.doc_processor.split_documents(all_documents)

        embeddings = OpenAIEmbeddings()
        self.vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=self.db_name
        )

        subjects = set(doc.metadata['doc_type'] for doc in all_documents)
        return (
            f"Directory structure:\n{summary}\n\n"
            f"Created vector store with {len(chunks)} chunks from subjects: {', '.join(subjects)}"
        )

    def initialize_knowledge_base(self, _=None):
        if os.path.exists(self.db_name):
            self.vectorstore = Chroma(
                persist_directory=self.db_name,
                embedding_function=OpenAIEmbeddings()
            )
            print(self.investigate_vectors())
            return "Knowledge base already exists and is loaded."  
        return self.create_vector_store()
    
    def add_folder(self, folder_path):
        if self.vectorstore is None:
            return "Please initialize the knowledge base first."
        new_docs = self.doc_processor.load_directory(folder_path)
        if not new_docs:
            return f"No PDFs found in {folder_path}."
        chunks = self.doc_processor.split_documents(new_docs)
        self.vectorstore.add_documents(chunks)
        return f"Added {len(chunks)} chunks from folder: {folder_path}"

    def add_file(self, file_path):
        if self.vectorstore is None:
            return "Please initialize the knowledge base first."
        new_docs = self.doc_processor.load_file(file_path)
        if not new_docs:
            return f"File not found or not a valid PDF: {file_path}"
        chunks = self.doc_processor.split_documents(new_docs)
        self.vectorstore.add_documents(chunks)
        return f"Added {len(chunks)} chunks from file: {file_path}"
    

    def investigate_vectors(self):
        if self.vectorstore is None:
            return "Vectorstore not initialized."
        collection = self.vectorstore._collection
        count = collection.count()

        sample_embedding = collection.get(limit=1, include=["embeddings"])["embeddings"][0]
        dimensions = len(sample_embedding)
        return f"There are {count:,} vectors with {dimensions:,} dimensions in the vector store"