from flask import Flask, jsonify

app = Flask(__name__)

# Liste des utilisateurs
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue sur mon API !"})

@app.route('/users')
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)

