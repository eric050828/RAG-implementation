import os
from io import BytesIO


ROOT_DIR = os.getcwd()

class PDF:
    @staticmethod
    def save(files: list[BytesIO]) -> list[str]:
        save_paths = []
        for file in files:
            save_path = ROOT_DIR + "\\data\\" + file.name
            with open(save_path, "wb") as f:
                f.write(file.getbuffer())
            save_paths.append(save_path)
        return save_paths
        
    @staticmethod
    def open(file: str) -> bytes:
        path = ROOT_DIR + "\\data\\" + file
        if not os.path.exists(path):
            raise FileNotFoundError(f"'{path} does not found.'")
        
        with open(path, "rb") as f:
            pdf_bytes = f.read()
        return pdf_bytes


def list_files(directory: str) -> list[str]:
    if os.path.isfile(directory):
        raise NotADirectoryError(f"'{directory}' does not a directory.")
    
    if "/" in directory:
        directory.replace("/", "\\")
        
    target_dir = ROOT_DIR + directory
    if not os.path.exists(target_dir):
        raise FileNotFoundError(f"Directory '{target_dir}' does not exist.")
    
    files = os.listdir(target_dir)
    return files



if __name__ == "__main__":
    pass