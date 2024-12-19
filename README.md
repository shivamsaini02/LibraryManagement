# 📚 Library Management System

A simple Flask-based **Library Management System** that provides RESTful APIs to perform CRUD operations for managing books and members.

---

## 🚀 Features
- **Books Management**: Add, retrieve, update, and delete books.
- **Members Management**: Add, retrieve, update, and delete members.
- Designed to be **lightweight** and **beginner-friendly**.
- Scalable and easily extendable for future enhancements.

---

## 🛠️ Installation and Setup

Follow the steps below to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/shivamsaini02/LibraryManagement.git
cd LibraryManagement
```

### 2. Set up a virtual environment.
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies.
```bash
pip install -r requirements.txt
```

### 4. Run the application.
```bash
python3 app.py
```
The application will run at: http://127.0.0.1:5000


## 🛡️ API Endpoints

### **Books**
| Method | Endpoint            | Description                |
|--------|---------------------|----------------------------|
| GET    | `/books`            | Retrieve all books         |
| POST   | `/books`            | Add a new book             |
| PUT    | `/books/<book_id>`  | Update a book by ID        |
| DELETE | `/books/<book_id>`  | Delete a book by ID        |

### **Members**
| Method | Endpoint               | Description                 |
|--------|------------------------|-----------------------------|
| GET    | `/members`             | Retrieve all members        |
| POST   | `/members`             | Add a new member            |
| PUT    | `/members/<member_id>` | Update a member by ID       |
| DELETE | `/members/<member_id>` | Delete a member by ID       |

## 🧪 Testing the API
You can test the API endpoints using Postman, cURL, or any other REST client.

### Add a New Book:
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "id": 1,
  "title": "The Pragmatic Programmer",
  "author": "Andrew Hunt"
}' http://127.0.0.1:5000/books

```

### 2. Retrieve All Books:
```bash
curl http://127.0.0.1:5000/books
```

### 3. Update a Book:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{
  "title": "The Pragmatic Programmer - Updated",
  "author": "Andrew Hunt"
}' http://127.0.0.1:5000/books/1
```

### 4. Delete a Book:
```bash
curl -X DELETE http://127.0.0.1:5000/books/1
```

## 🤔 Assumptions and Limitations

### 1. In-Memory Storage: 
Data is stored in memory and will reset when the server restarts.

### 2. No Authentication:
Token-based authentication is not implemented (bonus feature).

### 3. Minimal Error Handling: 
Limited validation for invalid inputs or edge cases.

## 📚 Future Improvements

* Integrate a database like SQLite or PostgreSQL for persistent data storage.
* Add token-based authentication for secure access.
* Implement search functionality for books by title or author.
* Include pagination for large datasets.

## 💡 Design Choices

### 1. Framework:
Flask is used for its simplicity and flexibility.

### 2. Data Storage:
Python dictionaries are used for in-memory storage to keep the project lightweight.

### 3. Extensibility:
The project structure is designed to allow easy addition of new features.

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify it.

## 👨‍💻 Author

# Shivam Saini
A passionate learner exploring software development and backend technologies.
Feel free to contact me for any questions or suggestions.






