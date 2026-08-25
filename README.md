# Flask Books REST API

A beginner-friendly REST API built with **Python and Flask** for managing a collection of books.

This project demonstrates the fundamental **CRUD operations** used when designing REST APIs:

* **GET** — Retrieve books
* **POST** — Create a new book
* **PATCH** — Partially update an existing book
* **DELETE** — Delete a book

The API currently stores book data in a Python list, so the data is stored **in memory** and will be lost whenever the application restarts.

## Technologies Used

* Python
* Flask
* HTTP
* REST API
* JSON
* Postman or another API testing tool

## Project Structure

```text
flask-books-api/
│
├── app.py
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd flask-books-api
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Flask

```bash
pip install flask
```

## Running the API

Start the Flask development server:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

You can then test the endpoints using **Postman**, **Insomnia**, `curl`, or a web browser for GET requests.

---

# API Endpoints

Base URL:

```text
http://127.0.0.1:5000/api/v1
```

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/books`      | Get all books           |
| GET    | `/books/<id>` | Get a specific book     |
| POST   | `/books`      | Create a new book       |
| PATCH  | `/books/<id>` | Partially update a book |
| DELETE | `/books/<id>` | Delete a book           |

---

# 1. Get All Books

### Request

```http
GET /api/v1/books
```

Example:

```text
http://127.0.0.1:5000/api/v1/books
```

### Response

```json
[
    {
        "id": 1,
        "title": "The Silent Algorithm",
        "author": "Daniel Carter",
        "year": 2018
    },
    {
        "id": 2,
        "title": "Python for Everyone",
        "author": "Maya Brooks",
        "year": 2020
    }
]
```

This endpoint returns the complete list of books.

---

# 2. Get a Specific Book

### Request

```http
GET /api/v1/books/<id>
```

Example:

```text
GET http://127.0.0.1:5000/api/v1/books/5
```

### Successful Response

```json
{
    "id": 5,
    "title": "Linux from the Ground Up",
    "author": "Michael Adams",
    "year": 2019
}
```

### Book Not Found

If the requested ID does not exist:

```json
{
    "message": "Book not found"
}
```

The API returns:

```http
404 Not Found
```

---

# 3. Create a Book

### Request

```http
POST /api/v1/books
```

When using Postman:

1. Select **POST**
2. Enter:

```text
http://127.0.0.1:5000/api/v1/books
```

3. Go to **Body**
4. Select **raw**
5. Select **JSON**
6. Send:

```json
{
    "title": "API Development with Flask",
    "author": "John Smith",
    "year": 2026
}
```

### Successful Response

```json
{
    "id": 21,
    "title": "API Development with Flask",
    "author": "John Smith",
    "year": 2026
}
```

The API returns:

```http
201 Created
```

The `201` status code indicates that a new resource was successfully created.

---

# 4. Update a Book with PATCH

The `PATCH` method is used to **partially update** an existing resource.

### Request

```http
PATCH /api/v1/books/<id>
```

For example:

```text
PATCH http://127.0.0.1:5000/api/v1/books/20
```

You do not have to send every field.

For example, to change only the year:

```json
{
    "year": 2029
}
```

The API will update only the `year` field.

### Response

```json
{
    "id": 20,
    "title": "Engineering Reliable APIs",
    "author": "Laura Wilson",
    "year": 2029
}
```

This demonstrates the difference between **partial updates** and replacing an entire resource.

You can also update multiple fields:

```json
{
    "title": "Advanced API Engineering",
    "year": 2030
}
```

The `author` field will remain unchanged.

---

# 5. Delete a Book

### Request

```http
DELETE /api/v1/books/<id>
```

Example:

```text
DELETE http://127.0.0.1:5000/api/v1/books/20
```

If the book exists, it is removed from the list.

The API returns:

```http
204 No Content
```

A `204` response means the request succeeded but there is no response body.

If the book does not exist:

```json
{
    "error": "Book not found"
}
```

with:

```http
404 Not Found
```

---

# HTTP Status Codes Used

This API currently uses several important HTTP status codes:

| Status Code      | Meaning                                 | Used By            |
| ---------------- | --------------------------------------- | ------------------ |
| `200 OK`         | Request succeeded                       | GET, PATCH         |
| `201 Created`    | Resource successfully created           | POST               |
| `204 No Content` | Request succeeded with no response body | DELETE             |
| `404 Not Found`  | Requested book does not exist           | GET, PATCH, DELETE |

---

# How the API Works

The application stores its books in a Python list:

```python
books = [
    {
        "id": 1,
        "title": "The Silent Algorithm",
        "author": "Daniel Carter",
        "year": 2018
    }
]
```

Each book is represented as a Python dictionary.

For example:

```python
{
    "id": 1,
    "title": "The Silent Algorithm",
    "author": "Daniel Carter",
    "year": 2018
}
```

The API exposes this data through HTTP endpoints.

### GET

Retrieves resources.

```text
Client → GET /books → Flask → Books
```

### POST

Creates a new resource.

```text
Client → POST /books + JSON → Flask → New Book
```

### PATCH

Modifies part of an existing resource.

```text
Client → PATCH /books/20 + JSON → Flask → Updated Book
```

### DELETE

Removes a resource.

```text
Client → DELETE /books/20 → Flask → 204 No Content
```

---

# Important Flask Concepts Demonstrated

## `request.get_json()`

The API uses:

```python
data = request.get_json()
```

This reads JSON data sent by the client in the HTTP request body and converts it into a Python dictionary.

For example, this request:

```json
{
    "year": 2029
}
```

becomes approximately:

```python
{
    "year": 2029
}
```

Python can then access the value:

```python
data["year"]
```

---

## Flask Route Decorators

The application uses modern Flask route decorators:

```python
@app.get("/api/v1/books")
```

```python
@app.post("/api/v1/books")
```

```python
@app.patch("/api/v1/books/<int:id>")
```

```python
@app.delete("/api/v1/books/<int:id>")
```

The decorator tells Flask which **HTTP method** and **URL path** should trigger a particular Python function.

For example:

```python
@app.get("/api/v1/books/<int:id>")
def get_book_by_id(id):
```

The `<int:id>` part is a dynamic URL parameter.

Therefore:

```text
/api/v1/books/1
```

passes:

```python
id = 1
```

while:

```text
/api/v1/books/15
```

passes:

```python
id = 15
```

---

# Testing with Postman

You can test the API using Postman.

### GET all books

```text
GET http://127.0.0.1:5000/api/v1/books
```

### GET one book

```text
GET http://127.0.0.1:5000/api/v1/books/10
```

### Create a book

```text
POST http://127.0.0.1:5000/api/v1/books
```

Body:

```json
{
    "title": "Learning REST APIs",
    "author": "Alex Morgan",
    "year": 2026
}
```

### Update a book

```text
PATCH http://127.0.0.1:5000/api/v1/books/10
```

Body:

```json
{
    "year": 2027
}
```

### Delete a book

```text
DELETE http://127.0.0.1:5000/api/v1/books/10
```

---

# Current Limitations

This project is intentionally simple and is designed for learning REST API fundamentals.

It currently does **not** include:

* Database persistence
* Authentication
* Authorization
* Input validation
* Error handling for malformed JSON
* Schema validation
* Rate limiting
* Logging
* API documentation
* HTTPS
* CORS configuration
* Pagination
* Filtering
* Search
* Production deployment

The books are stored in a Python list, meaning all changes disappear when the Flask application restarts.

---

# Future Improvements

Possible improvements include:

1. Replace the Python list with PostgreSQL or another database.
2. Add SQLAlchemy for database interaction.
3. Add request validation.
4. Implement proper error handling.
5. Add authentication and authorization.
6. Add JWT-based authentication.
7. Add rate limiting.
8. Add pagination.
9. Add filtering and search.
10. Add automated tests with `pytest`.
11. Add API documentation with OpenAPI/Swagger.
12. Deploy the API using Docker and a production WSGI server.
13. Add security protections against common API vulnerabilities.

---

# Learning Objectives

This project is intended to help beginners understand:

* REST API fundamentals
* HTTP methods
* HTTP status codes
* URL routing
* Dynamic route parameters
* JSON request bodies
* JSON responses
* CRUD operations
* Flask route decorators
* `request.get_json()`
* API testing with Postman
* Basic API design

It also provides a foundation for moving from a simple Flask API toward **database-backed, authenticated, tested, and security-focused APIs**.

## License

This project is intended for educational and learning purposes.
