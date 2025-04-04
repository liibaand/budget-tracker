from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BudgetEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Add this line
    category = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<BudgetEntry {self.category} {self.amount}>'
