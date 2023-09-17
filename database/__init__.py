from pymongo import MongoClient
from utilities.constants import CONSTANTS
from bson import ObjectId

client = MongoClient(CONSTANTS.DB_HOST)

class Database:
    def __init__(self):
        self.client = client
        self.db = self.client[CONSTANTS.DB_NAME]
        self.book = self.db[CONSTANTS.BOOK]

    def insertBook(self, data: dict):
        print(data)
        self.book.insert_one(data)
        return {
            "status": True,
            "message": "Inserted Data"
        }
    
    def getBooks(self, query: dict = {}):
        result = self.book.find(query)
        output = []
        for book in result:
            book["id"] = str(book.pop("_id"))
            output.append(book)
        return output
    
    def getBook(self, id: str):
        if not self.book.count_documents({"_id": ObjectId(id)}):
            return {
                "status": False,
                "message": "No Data Found"
            }
        result = dict(self.book.find_one({"_id": ObjectId(id)}))
        result["id"] = str(result.pop("_id"))
        return result
    
    def deleteBook(self, query: dict):
        if not self.book.count_documents(query):
            return {
                "status": False,
                "message": "No Data Found"
            }
        self.book.delete_one(query)
        return {
            "status": True,
            "message": "Deleted Data"
        }
    
    def updateBook(self, query: dict, data: dict):
        if not self.book.count_documents(query):
            return {
                "status": False,
                "message": "No Data Found"
            }
        self.book.update_one(query, data)
        return {
            "status": True,
            "message": "Updated Data",
            "data": data
        }
