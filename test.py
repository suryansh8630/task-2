import unittest
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        response = requests.get("https://atg.world")
        if response.status_code == 200:
            return "Website loaded successfully!", 200
        else:
            return "Failed to load website.", 500
    except requests.ConnectionError:
        return "Failed to connect to website.", 500
@app.route('/hello')
def ind():
    return 'Hello, World!'       

class TestWebsiteConnection(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_website_loading(self):
        print("Testing connection to atg.world website...")
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Website loaded successfully!")
        self.assertEqual(response.location, 'http://20.197.8.46/hello')
        print("atg.world website loaded successfully!")
        print("Website redirected to Hello World Flask route successfully!")
        
if __name__ == "__main__":
    unittest.main()
