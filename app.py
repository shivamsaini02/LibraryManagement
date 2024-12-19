from flask import Flask
from routes.books import books_bp

app = Flask(__name__)
app.register_blueprint(books_bp)

@app.route('/')
def home():
    return "Welcome to the Library Management System!"

if __name__ == "__main__":
    app.run(debug=True)
