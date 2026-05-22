#!/usr/bin/env python
"""
Guitar Tuner Flask Application - Entry Point
Run this file to start the development server
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import create_app

if __name__ == '__main__':
    app = create_app()
    
    print("\n" + "="*50)
    print("  Guitar Tuner Flask App")
    print("="*50)
    print("\n✓ Local:    http://127.0.0.1:5000")
    print("✓ Network:  http://192.168.X.X:5000")
    print("\n(Replace 192.168.X.X with your actual IP address)")
    print("="*50 + "\n")
    
    # Run on all interfaces (accessible from network)
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=True
    )
