from flask import Flask, render_template

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/hello/<name>')
def hello_name(name):
    return render_template("hello.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)

=======
@app.route('/')
def index():
    # Sample data list: each book is represented as a dictionary with a title and an author.
    books = [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"id": 2, "title": "1984", "author": "George Orwell"},
        {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
    ]
    # Pass the list and a title string to the template.
    return render_template('index.html', books=books, title="Book List")

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 979a292 (Finish lab_18)
