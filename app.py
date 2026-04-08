from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    users.append(data)
    return jsonify({"message": "User added"}), 201

@app.route('/users/<int:index>', methods=['DELETE'])
def delete_user(index):
    if 0 <= index < len(users):
        users.pop(index)
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "Invalid index"}), 404

if __name__ == '__main__':
    app.run(debug=True)