from dotenv import load_dotenv
import os

load_dotenv()

class CONSTANTS:
    DB_NAME = "library"
    DB_HOST = os.getenv("MONGODB_URI")
    BOOK = "book"