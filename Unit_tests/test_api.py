import requests
import unittest

BASE_URL = 'http://localhost:5000'

class TestApi(unittest.TestCase):

    # test get all contacts
    def test_1_get_contacts(self):
        result = requests.get(BASE_URL + '/contact')
        self.assertAlmostEqual(result.status_code, 200)
    
    # test get contact by id
    def test_2_get_contact(self):
        result = requests.get(BASE_URL + '/contact/1')
        self.assertAlmostEqual(result.status_code, 200)

    # test get contact/s by name 
    def test_3_get_contact_by_name(self):
        result = requests.get(BASE_URL + '/contact/name?name=a')
        self.assertAlmostEqual(result.status_code, 200)
    
    # test create contact
    def test_4_add_contact(self):
        contact = {
            "name": "Rahib",
            "email": "rahib@hotamil.co.uk",
            "phone_number": "07465639232"
        }

        result = requests.post(BASE_URL + '/contact', json=contact)
        self.assertAlmostEqual(result.status_code, 201)

    # test update contact
    def test_5_update_contact(self):
        contact = {
            "name": "Bob Change",
            "email": "bob@hotmail.co.uk",
            "phone_number": "07465109239"
        }
        result = requests.put(BASE_URL + '/contact/1', json=contact)
        self.assertAlmostEqual(result.status_code, 200)

    # test delete contact
    def test_6_delete_contact(self):
        result = requests.delete(BASE_URL + '/contact/4')
        self.assertAlmostEqual(result.status_code, 204)

if __name__ == '__main__':
    unittest.main()