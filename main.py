"""
Flask Application Factory
Creates and configures the Flask app instance
"""

from flask import Flask, render_template, jsonify
from flask_cors import CORS


def create_app():
    """
    Create and configure the Flask application
    
    Returns:
        Flask app instance
    """
    
    # Initialize Flask app
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static',
                static_url_path='/static')
    
    # Enable CORS (Cross-Origin Resource Sharing)
    CORS(app)
    
    # Configuration
    app.config['JSON_SORT_KEYS'] = False
    
    # ==================== Routes ====================
    
    @app.route('/')
    def index():
        """Serve the main application page"""
        return render_template('index.html')
    
    
    @app.route('/api/config')
    def get_config():
        """
        API endpoint: Get app configuration
        Returns guitar string frequencies and settings
        """
        return jsonify({
            'strings': {
                'E2': 82.41,    # Low E (6th string)
                'A': 110.00,    # A (5th string)
                'D': 146.83,    # D (4th string)
                'G': 196.00,    # G (3rd string)
                'B': 246.94,    # B (2nd string)
                'E4': 329.63    # High E (1st string)
            },
            'tuningThreshold': 5,  # cents
            'maxCents': 50
        })
    
    
    @app.route('/api/health')
    def health_check():
        """
        API endpoint: Health check
        Used to verify the server is running
        """
        return jsonify({
            'status': 'healthy',
            'service': 'guitar-tuner'
        })
    
    
    # ==================== Error Handlers ====================
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return jsonify({
            'error': 'Not found',
            'message': 'The requested resource does not exist'
        }), 404
    
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        return jsonify({
            'error': 'Internal server error',
            'message': 'An unexpected error occurred'
        }), 500
    
    
    return app
