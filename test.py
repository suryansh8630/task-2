import unittest
import requests
import subprocess
import time

class TestWebsiteConnection(unittest.TestCase):
    def test_website_loading(self):
        print("Testing connection to atg.world website...")
        try:
            response = requests.get("https://atg.world")
            self.assertEqual(response.status_code, 200)
            print("atg.world website loaded successfully!")
        except requests.ConnectionError:
            self.fail("Failed to connect to atg.world website!")

class TestFlaskApp(unittest.TestCase):
    def test_flask_hello_world(self):
        print("Testing Flask Hello World application...")
        try:
            # Start Flask application
            flask_process = subprocess.Popen(["python", "app.py"])
            time.sleep(2)  # Allow some time for Flask to start

            # Make request to Flask app
            response = requests.get("http://localhost:5000")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.text, "Hello, World!")
            print("Flask Hello World application running on port 5000!")
        except Exception as e:
            self.fail(f"Failed to run Flask Hello World application: {str(e)}")
        finally:
            # Stop Flask application
            flask_process.terminate()
            flask_process.wait()

if __name__ == "__main__":
    unittest.main()
