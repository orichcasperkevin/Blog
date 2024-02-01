import tempfile
import os

class TemporaryDirectoryContext:
    def __enter__(self):
        print("Creating temporary directory")
        self.temp_dir = tempfile.mkdtemp()
        return self.temp_dir

    def __exit__(self, exc_type, exc_value, traceback):
        print("Deleting temporary directory")
        try:
            os.rmdir(self.temp_dir)
        except FileNotFoundError:
            pass  # Handle the case where the directory was already deleted

# Define a convenient API for the TemporaryDirectory class
class ConvenientFileHandlingAPI:
    def __init__(self):
        self.temp_dir_manager = TemporaryDirectoryContext()

    def create_file(self, file_name, content):
        with self.temp_dir_manager as temp_dir:
            file_path = os.path.join(temp_dir, file_name)
            print(f"Creating file: {file_path}")
            with open(file_path, 'w') as file:
                file.write(content)
            return file_path

# Usage
file_handling_api = ConvenientFileHandlingAPI()
file_path = file_handling_api.create_file("example.txt", "This is some content.")

# The temporary directory is automatically cleaned up when exiting the 'with' block
print(f"File created at: {file_path}")
