import requests
import unittest
import random
import string

BASE_URL = 'http://localhost:5000'

class TestApi(unittest.TestCase):

    # test create contact
    def test_1_add_contact(self):
        before_create = requests.get(BASE_URL + '/contact')
        before_length = len(before_create.json())
        letters = string.ascii_lowercase
        numbers = string.digits
        randomString = ''.join(random.choice(letters) for i in range(10))
        randomNumber = ''.join(random.choice(numbers) for i in range(9))

        contact = {
            "name": "Test_" + randomString,
            "email": randomString + "@hotamil.co.uk",
            "phone_number": "07" + randomNumber
        }

        result = requests.post(BASE_URL + '/contact', json=contact)
        self.assertEqual(result.status_code, 201)
        
        after_create = requests.get(BASE_URL + '/contact')
        after_length = len(after_create.json())

        self.assertGreater(int(after_length), int(before_length))

    # test get all contacts
    def test_2_get_contacts(self):
        result = requests.get(BASE_URL + '/contact')
        self.assertEqual(result.status_code, 200)
    
    # test get contact by id
    def test_3_get_contact(self):
        result = requests.get(BASE_URL + '/contact')
        res_id = result.json()[0]['id']
        result = requests.get(BASE_URL + '/contact/' + str(res_id))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(b'name' in result.content)
        self.assertTrue(b'phone_number' in result.content)
        self.assertTrue(b'email' in result.content)

    # test get contact/s by name 
    def test_4_get_contact_by_name(self):
        result = requests.get(BASE_URL + '/contact')
        res_name = result.json()[0]['name']
        new_result = requests.get(BASE_URL + '/contact/name?name=' + res_name)
        self.assertEqual(result.json()[0]['id'], new_result.json()[0]['id'])
    

    # # test update contact
    def test_5_update_contact(self):
        letters = string.ascii_lowercase
        randomString = ''.join(random.choice(letters) for i in range(10))

        result = requests.get(BASE_URL + '/contact')
        before_update = result.json()[0]
        change = before_update
        change['name'] = before_update['name'] + randomString

        after = requests.put(BASE_URL + '/contact/' + str(before_update['id']), json=change)
        after_update = after.json()
        self.assertEqual(change['name'], after_update['name'])

    # test delete contact
    def test_6_delete_contact(self):
        before_delete = requests.get(BASE_URL + '/contact')
        before_length = len(before_delete.json())

        result = requests.delete(BASE_URL + '/contact/' + str(before_delete.json()[0]['id']))
        self.assertEqual(result.status_code, 204)

        after_delete = requests.get(BASE_URL + '/contact')
        after_length = len(after_delete.json())
        self.assertLess(int(after_length), int(before_length))

if __name__ == '__main__':
    unittest.main()