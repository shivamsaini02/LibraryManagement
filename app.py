from flask import Flask
from routes.books import books_bp

app = Flask(__name__)
app.register_blueprint(books_bp)

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Library Management System</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 0;
                    text-align: center;
                }
                header {
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    font-size: 24px;
                }
                main {
                    margin: 50px auto;
                    max-width: 600px;
                    background: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                ul {
                    text-align: left;
                }
                a {
                    color: #4CAF50;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <header>📚 Welcome to the Library Management System</header>
            <main>
                <p>Use the API endpoints to manage books and members:</p>
                <ul>
                    <li><b>Books API:</b> <a href="/books">/books</a></li>
                    <li><b>Members API:</b> <a href="/members">/members</a> (if implemented)</li>
                </ul>
                <p>For testing, use tools like Postman or cURL.</p>
            </main>
        </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
