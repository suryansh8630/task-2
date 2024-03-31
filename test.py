import unittest
from flask import Flask, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        response = requests.get("https://atg.world")
        if response.status_code == 200:
            return redirect(url_for('hello'))
        else:
            return "Failed to load website.", 500
    except requests.ConnectionError:
        return "Failed to connect to website.", 500

@app.route('/hello')
def hello():
    return 'Hello, World!'

class TestWebsiteConnection(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_website_loading(self):
        print("Testing connection to atg.world website...")
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertEqual(response.location, 'http://localhost/hello')
        print("Website redirected to Hello World Flask route successfully!")

if __name__ == "__main__":
    unittest.main()
