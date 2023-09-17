from fastapi import APIRouter, Request, Response
from database import Database
from utilities.schema import Book
from json import dumps
from bson import ObjectId

router = APIRouter()
db = Database()

# C
@router.post("/")
async def add_book(req: Request, body: Book): 
    result = db.insertBook(dict(body))
    return Response(
        dumps(result), media_type="application/json"
    )

# R
@router.get("/{id}")
async def get_books(req: Request, id: str):
    return Response(
        dumps(db.getBooks() if id == "all" else dict(db.getBook(id=id))), media_type="application/json"
    )

# U
@router.put("/{id}")
async def edit_book(req: Request, body: Book, id: str):
    result = db.updateBook({"_id": ObjectId(id)}, {"$set": dict(body)})
    return Response(
        dumps(result), media_type="application/json"
    )

# D
@router.delete("/{id}")
async def delete_book(req: Request, id: str):
    result = db.deleteBook({"_id": ObjectId(id)})
    return Response(
        dumps(result), media_type="application/json"
    )