import os
from flask import Flask, render_template, jsonify
from config import DEBUG, PORT, env

# Create Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Configure app based on environment
app.config['DEBUG'] = DEBUG
app.config['ENV'] = env

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html', 
                         environment=env, 
                         debug_mode=DEBUG, 
                         port=PORT)

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html', 
                         environment=env,
                         debug_mode=DEBUG,
                         port=PORT)

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'environment': env,
        'debug': DEBUG,
        'port': PORT
    })

@app.route('/config')
def show_config():
    """Display current configuration"""
    return jsonify({
        'environment': env,
        'debug_mode': DEBUG,
        'port': PORT,
        'flask_env': os.getenv('FLASK_ENV', 'not set')
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html', 
                         error="Page not found",
                         environment=env,
                         debug_mode=DEBUG,
                         port=PORT), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('index.html', 
                         error="Internal server error",
                         environment=env,
                         debug_mode=DEBUG,
                         port=PORT), 500

if __name__ == '__main__':
    print(f"Starting Flask app in {env} environment")
    print(f"Debug mode: {DEBUG}")
    print(f"Port: {PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
