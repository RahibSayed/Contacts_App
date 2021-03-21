import requests
import unittest

BASE_URL = 'http://localhost:5000'

class TestApi(unittest.TestCase):

    def test_1_get_contacts(self):
        result = requests.get(BASE_URL + '/contact')
        self.assertAlmostEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()