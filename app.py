"""
app.py - Main entry point for the Flask Budget Tracker.
Handles routing and API requests.
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, BudgetEntry, User # Imports database and model
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
CORS(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    if User.query.filter_by(username=username).first():
         return jsonify({"error": "Username already exists"}), 400
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({"message": "Login successful", "user_id": user.id})
    return jsonify({"error": "Wrong username or password"}), 401
    

@app.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json()
    category = data.get('category')
    amount = data.get('amount')
    date = data.get('date')
    user_id = data.get('user_id')
    if not category or not amount or not date or not user_id:
        return jsonify({"error": "Missing Data"}), 400
    new_entry = BudgetEntry(category=category, amount=amount, date=date, user_id=user_id)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({"message": "Entry added successfully!"})
@app.route('/entries', methods=['GET'])
def get_entries():
    """Fetches all budget entries from the database."""
    entries = BudgetEntry.query.all()
    result = [{"category": entry.category, "amount": entry.amount, "date": entry.date.isoformat(), "user_id": entry.user_id} for entry in entries]
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True) # Runs the flask app