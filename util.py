import os

def delete_all_ppt(folder_path):
    deleted = 0
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(".md"):
                full_path = os.path.join(root, filename)
                try:
                    os.remove(full_path)
                    print(f"Deleted: {full_path}")
                    deleted += 1
                except Exception as e:
                    print(f"Failed to delete {full_path}: {e}")
    print(f"Total .ppt files deleted: {deleted}")

# Example usage:
delete_all_ppt("E:\\LargeLanGuageModel\\New folder\\RagProject\\knowledge_base")