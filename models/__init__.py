print("start init")
from models.engine.file_storage import FileStorage

# Create storage variable and assign it an instance of FileStorage
storage = FileStorage()
print("checker 1")
# Call reload method on storage variable
storage.reload()
print("checker 2")
print("first line")
