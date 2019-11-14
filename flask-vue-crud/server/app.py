from flask import Flask, jsonify, request
from flask_cors import CORS

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
        'title': 'El mundo de Sofía',
        'author': 'Josteein Gaarder',
        'genre': 'Novela filosófica',
        'available': True
    
    },
    {
        'title': 'El principito',
        'author': 'Antoine de Saint-Exupéry',
        'genre': 'Fábula',
        'available': False
    },
    {
        'title': 'Romeo y Julieta',
        'author': 'William Shakespeare',
        'genre': 'Tragedia',
        'available': True
    }
]

# Route to handle GET requests Books component
@app.route('/books', methods=['GET', 'POST'])
# Return a json formatted answer with all the books
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'genre': post_data.get('genre'),
            'available': post_data.get('available') 
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()