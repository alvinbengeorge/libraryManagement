from fastapi import FastAPI
from routes import books

app = FastAPI()
app.include_router(books.router, prefix="/books")

@app.get("/")
async def root():
    return {"Project": "Library Management"}