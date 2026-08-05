# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI to practice route creation, request validation, and CRUD operations using in-memory data.

## 📝 Tasks

### 🛠️ Create Core Endpoints

#### Descrição
Set up a FastAPI application and implement core endpoints to manage a collection of books.

#### Requisitos
O programa concluído deve:

- Create a `FastAPI` app instance
- Implement `GET /health` returning API status
- Implement `GET /books` returning all books
- Implement `GET /books/{book_id}` returning one book or `404` when not found


### 🛠️ Add Validation and CRUD

#### Descrição
Use Pydantic models to validate requests and complete create, update, and delete operations.

#### Requisitos
O programa concluído deve:

- Define request and response models for books (`title`, `author`, `year`)
- Implement `POST /books` to create a new book with auto-incremented ID
- Implement `PUT /books/{book_id}` to update an existing book
- Implement `DELETE /books/{book_id}` to remove a book and return a success message
- Return proper HTTP status codes (`201`, `404`, `422`)
