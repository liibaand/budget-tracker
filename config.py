"""
config.py - Configuration settings for the Flask Budget Tracker.
Defines database URI and other app settings.
"""
import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///budget.db' \
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
