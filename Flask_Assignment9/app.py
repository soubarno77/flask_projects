from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = r'mysql://user:123@localhost:3306/my_db'
db = SQLAlchemy(app)

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  author = db.Column(db.String(50))

@app.route('/')
def index():
  books = Book.query.all()
  return render_template('index.html', books=books)  

@app.route('/books/new', methods=['GET', 'POST'])
def new():
  if request.method == 'POST':
    title = request.form['title']
    author = request.form['author']
    
    new_book = Book(title=title, author=author)
    db.session.add(new_book)
    db.session.commit()
    
    return redirect(url_for('index'))

  return render_template('new.html')

@app.route('/books/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
  book = Book.query.get(id)
  if request.method == 'POST':
    book.title = request.form['title']
    book.author = request.form['author']
    db.session.commit()
    return redirect(url_for('index'))
    
  return render_template('edit.html', book=book)

@app.route('/books/<int:id>/delete')
def delete(id):
  book = Book.query.get(id)
  db.session.delete(book)
  db.session.commit()
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)