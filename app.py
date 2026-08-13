from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, 
            template_folder='templates',
            static_folder='static')

# Secret key for sessions (change this in production)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-this')

# ---------- Routes ----------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page>.html')
def serve_page(page):
    """Serve any HTML page dynamically"""
    try:
        return render_template(f'{page}.html')
    except:
        return render_template('404.html'), 404

# ---------- Static Files ----------
@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files (images, CSS, etc.)"""
    return send_from_directory('static', filename)

# ---------- Error Handlers ----------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# ---------- Run ----------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
