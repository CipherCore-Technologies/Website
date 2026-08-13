from flask import Blueprint, render_template

# Create a blueprint for dashboard routes
dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
def dashboard_home():
    """Main dashboard view — placeholder"""
    return "<h1>Dashboard Coming Soon</h1><p>This is where you'll manage projects and clients.</p>"

@dashboard_bp.route('/projects')
def dashboard_projects():
    """Projects view — placeholder"""
    return "<h1>Projects</h1><p>Project management coming soon.</p>"

@dashboard_bp.route('/clients')
def dashboard_clients():
    """Clients view — placeholder"""
    return "<h1>Clients</h1><p>Client management coming soon.</p>"


# To use this in app.py, uncomment these lines:
# from dashboard import dashboard_bp
# app.register_blueprint(dashboard_bp)
