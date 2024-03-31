import unittest
import requests
from flask import Flask
import uwsgi



class TestWebsiteConnection(unittest.TestCase):
    
    def test_website_connection(self):
        url = 'https://atg.world'
        
        print("Attempting to connect to", url)
        try:
            response = requests.get(url)
            status_code = response.status_code
            print("Status code:", status_code)
            
            self.assertEqual(status_code, 200)  # Assuming 200 is the expected status code for successful connection
            print("Website loaded successfully!")

            app = Flask(__name__)

            @app.route('/')
            def hello():
                return 'Hello, World!'

            if __name__ == '__main__':
                app.run(port=5000)


        except Exception as e:
            print("Failed to connect to website:", e)
            self.fail("Failed to connect to website")

if __name__ == '__main__':
    unittest.main()
