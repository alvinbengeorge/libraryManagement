# `LIBRARY MANAGEMENT`

## `Description`
This is a project made for DSC recruitment

## `Installation and Setup`
```bash
git clone https://github.com/alvinbengeorge/libraryManagement
cd libraryManagement

# Install dependencies
pip3 install -r requirements.txt

# Run the app
uvicorn main:app --reload
```

## `Routes`

### `GET /books`
Returns all the books in the library

### `GET /books/:id`
Returns the book with the given id

### `POST /books`
Adds a new book to the library

```json
{
    "name": "The Alchemist", // string
    "author": "Paulo Coelho",// string
    "price": 100.0           // float
}
```

### `PUT /books/:id`
Updates the book with the given id

```json
{
    "name": "The Alchemist", // string
    "author": "Paulo Coelho",// string
    "price": 100.0           // float
}
```

### `DELETE /books/:id`
Deletes the book with the given id