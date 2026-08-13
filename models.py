"""
Database Models — Placeholder for future database structure.

This file will eventually contain:
- User model (authentication)
- Client model
- Project model
- Message/Inquiry model (from contact form)
- Blog Post model

For now, it's a placeholder to establish the module structure.
"""

# Uncomment when ready to set up database:
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

# Example models for future reference:

"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_admin = db.Column(db.Boolean, default=False)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    company = db.Column(db.String(100))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(50), default='planning')
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)
    project_type = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_read = db.Column(db.Boolean, default=False)
"""

# For now, just a placeholder message
print("Models module loaded — ready for future database setup")
