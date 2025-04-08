"""
app.py - Main entry point for the Flask Budget Tracker.
Handles routing and API requests.
"""
from flask import Flask, request, jsonify
from models import db, BudgetEntry # Imports database and model
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json()
    category = data.get('category')
    amount = data.get('amount')
    date = data.get('date')
    
    if not category or not amount or not date:
        return jsonify({"error": "Missing Data"}), 400
    new_entry = BudgetEntry(category=category, amount=amount, date=date)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({"message": "Entry added successfully!"})
@app.route('/entries', methods=['GET'])
def get_entries():
    """Fetches all budget entries from the database."""
    entries = BudgetEntry.query.all()
    result = [{"category": entry.category, "amount": entry.amount, "date": entry.date} for entry in entries]
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True) # Runs the flask app