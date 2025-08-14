#!/usr/bin/env python3
"""
Test script for the GCN Flask application
"""

import sys
import os
from app import app

def test_routes():
    """Test that all routes are accessible"""
    with app.test_client() as client:
        routes_to_test = [
            '/',
            '/team',
            '/events',
            '/events/upcoming',
            '/events/past',
            '/events/workshops',
            '/community',
            '/community/success-stories',
            '/community/mentorship',
            '/community/forum',
            '/resources',
            '/join'
        ]
        
        print("Testing routes...")
        for route in routes_to_test:
            response = client.get(route)
            if response.status_code == 200:
                print(f"✓ {route} - OK")
            elif response.status_code == 302:  # Redirect for resources
                print(f"✓ {route} - Redirect OK")
            else:
                print(f"✗ {route} - Failed (Status: {response.status_code})")
                return False
        return True

def test_static_files():
    """Test that static files are accessible"""
    with app.test_client() as client:
        static_files = [
            '/static/css/style.css',
            '/static/js/main.js',
            '/static/gcn.png'
        ]
        
        print("\nTesting static files...")
        for file_path in static_files:
            response = client.get(file_path)
            if response.status_code == 200:
                print(f"✓ {file_path} - OK")
            else:
                print(f"✗ {file_path} - Failed (Status: {response.status_code})")
                return False
        return True

def main():
    """Main test function"""
    print("GCN Website Test Suite")
    print("=" * 30)
    
    # Test routes
    routes_ok = test_routes()
    
    # Test static files
    static_ok = test_static_files()
    
    print("\n" + "=" * 30)
    if routes_ok and static_ok:
        print("✓ All tests passed! The website is ready to run.")
        print("\nTo start the website, run:")
        print("python3 app.py")
        print("\nThen open http://localhost:5000 in your browser.")
        return 0
    else:
        print("✗ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 