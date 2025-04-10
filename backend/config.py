"""
config.py - Configuration settings for the Flask Budget Tracker.
Defines database URI and other app settings.
"""
import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///budget.db' \
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")


class TestConfig(Config):
    # Test-specific database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_budget.db'
