
from flask import render_template, request, redirect, Blueprint
from models.library import *
from models.book import *



library_blueprint = Blueprint('library', __name__)

@library_blueprint.route('/library')
def index():
    return render_template('index.html', title='Home',library=library)

@library_blueprint.route('/library', methods=['POST'])
def add_new_book():
  
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']
  
  new_book = Book(title=title, author=author, genre=genre)
  add_new_book(new_book)
  return redirect('/library')

@library_blueprint.route('/library/remove/<title>', methods=['POST'])
def remove_book(title):
  remove_book(title)
  return redirect('/library')