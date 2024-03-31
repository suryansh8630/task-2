import unittest
import requests

class TestWebsiteConnection(unittest.TestCase):
    def test_website_loading(self):
        print("Testing connection to atg.world website...")
        try:
            response = requests.get("https://atg.world")
            self.assertEqual(response.status_code, 200)
            print("atg.world website loaded successfully!")
        except requests.ConnectionError:
            self.fail("Failed to connect to atg.world website!")

if __name__ == "__main__":
    unittest.main()
