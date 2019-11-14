# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
# Configuration
DEGUB = True

# Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Route to ping component
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# Book list
BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'El mundo de Sofía',
        'author': 'Josteein Gaarder',
        'genre': 'Novela filosófica',
        'available': True
    
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'El principito',
        'author': 'Antoine de Saint-Exupéry',
        'genre': 'Fábula',
        'available': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Romeo y Julieta',
        'author': 'William Shakespeare',
        'genre': 'Tragedia',
        'available': True
    }
]

# Route to handle GET,POST requests Books component
@app.route('/books', methods=['GET', 'POST'])
# Return a json formatted answer with all the books
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'genre': post_data.get('genre'),
            'available': post_data.get('available') 
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

# Route to handle PUT requests to update the list
@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'genre': post_data.get('genre'),
            'available': post_data.get('available') 
        })
        response_object['message'] = 'Libro actualizado!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Libro eliminado!'
    return jsonify(response_object)
def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False
if __name__ == '__main__':
    app.run()