from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Lista de usuários (inicialmente vazia)
users = []

# ID inicial para os usuários
next_id = 1

# Rota para obter todos os usuários
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

# Rota para obter um usuário pelo ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404)
    return jsonify({'user': user})

# Rota para adicionar um novo usuário
@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or 'name' not in request.json:
        abort(400)
    global next_id
    user = {
        'id': next_id,
        'name': request.json['name'],
        'age': request.json.get('age', None),
        'email': request.json.get('email', None)
    }
    users.append(user)
    next_id += 1
    return jsonify({'user': user}), 201

# Rota para atualizar um usuário existente
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404)
    if not request.json:
        abort(400)
    user['name'] = request.json.get('name', user['name'])
    user['age'] = request.json.get('age', user['age'])
    user['email'] = request.json.get('email', user['email'])
    return jsonify({'user': user})

# Rota para excluir um usuário existente
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404)
    users.remove(user)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
