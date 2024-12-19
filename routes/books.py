from flask import Blueprint, request, jsonify

books_bp = Blueprint('books', __name__)

books = []

@books_bp.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'GET':
        return jsonify(books)
    elif request.method == 'POST':
        new_book = request.json
        books.append(new_book)
        return jsonify({"message": "Book added successfully!"}), 201

@books_bp.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(book_id):
    for book in books:
        if book['id'] == book_id:
            if request.method == 'GET':
                return jsonify(book)
            elif request.method == 'PUT':
                book.update(request.json)
                return jsonify({"message": "Book updated successfully!"})
            elif request.method == 'DELETE':
                books.remove(book)
                return jsonify({"message": "Book deleted successfully!"})
    return jsonify({"error": "Book not found"}), 404
