
import gridfs
import pymongo
from pymongo import MongoClient
import os

class MongoGridFSOperations:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.fs = gridfs.GridFS(self.db)

    def upload_file(self, file_path: str, filename: str = None):
        filename = filename or os.path.basename(file_path)
        with open(file_path, "rb") as f:
            self.fs.put(f, filename=filename)

    def download_file(self, filename: str, output_path: str):
        file_data = self.fs.find_one({"filename": filename})
        if file_data:
            with open(output_path, "wb") as f:
                f.write(file_data.read())
        else:
            raise FileNotFoundError(f"File '{filename}' not found in MongoDB GridFS")