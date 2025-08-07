"""
app.py - Main entry point for the Flask Budget Tracker.
Handles routing and API requests.
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, BudgetEntry, User 
from config import Config
from datetime import datetime

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})


    @app.route('/register', methods=['POST'])
    def register():
        try:
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
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "Registration failed"}), 500

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return jsonify({"message": "Login successful", "user_id": user.id})
        return jsonify({"error": "Wrong username or password"}), 401

# @app.route('/add', methods=['POST'])
#    def add_entry():
       
    @app.route('/entries', methods=['GET'])
    def get_entries():
        entries = BudgetEntry.query.all()
        result = [{"category": entry.category, "amount": entry.amount, "date": entry.date.isoformat(), "user_id": entry.user_id} for entry in entries]
        return jsonify(result)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
