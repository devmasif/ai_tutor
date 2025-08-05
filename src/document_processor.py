from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
import glob
import os

class DocumentProcessor:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def load_document_from_folders(self, base_path):
        all_documents = []
    # Find all subfolders (subjects) recursively under base_path
        for root, dirs, files in os.walk(base_path):
            # Only process leaf folders (that contain PDFs)
            pdfs = [f for f in files if f.lower().endswith(".pdf")]
            if pdfs:
                doc_type = os.path.basename(root)
                print(f"Processing {doc_type} in {root}")
                loader = DirectoryLoader(
                    root,
                    recursive=False,  # Only this folder
                    glob="*.pdf",
                    loader_cls=PyPDFLoader
                )
                folder_docs = loader.load()
                for doc in folder_docs:
                    doc.metadata["doc_type"] = doc_type
                    doc.metadata["source_folder"] = root
                    doc.metadata["subject"] = doc_type
                all_documents.extend(folder_docs)
        return all_documents

    def load_directory(self, folder):
        if os.path.isdir(folder):
            doc_type = os.path.basename(folder)
            print(f"Processing {doc_type}")
            loader = DirectoryLoader(
                folder,
                recursive=True,
                glob="**/*.pdf",
                loader_cls=PyPDFLoader
            )
            folder_docs = loader.load()
            for doc in folder_docs:
                doc.metadata["doc_type"] = doc_type
                doc.metadata["source_folder"] = folder
                doc.metadata["subject"] = doc_type
            return folder_docs
        return []

    def load_file(self, path):
        if os.path.isfile(path):
            doc_type = os.path.basename(os.path.dirname(path)) 
            source_folder = os.path.dirname(path)
            loader = PyPDFLoader(path)
            docs = loader.load()
            for doc in docs:
                doc.metadata["doc_type"] = doc_type
                doc.metadata["source_folder"] = source_folder
                doc.metadata["subject"] = doc_type
            return docs
        else:
            return []

    def split_documents(self, documents):
        return self.text_splitter.split_documents(documents)