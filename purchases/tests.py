from django.test import TestCase
from json import loads
from requests import post, put, delete, get
from http import HTTPStatus


class TestPurchase(TestCase):
    _NUMBER_OF_REQUESTS = 10

    def test_create_purchase(self):

        for i in range(self._NUMBER_OF_REQUESTS):
            p = {
                "purchase_name": "purchase",
                "user_id": 100,
                "username": "user1",
                "phone_number": f"+098765432{i}",
                "email": f"test{i}@example.com",
                "address": "address1",
            }

            res = post('http://localhost:8000/purchases/', data=p)
            self.assertEqual(HTTPStatus.CREATED, res.status_code)

    def test_get_purchases(self):

        res = get('http://localhost:8000/purchases/')
        self.assertEqual(HTTPStatus.OK, res.status_code)

        results = loads(res.content).get('results', [])
        for i in results:
            res = get(f'http://localhost:8000/purchases/{i["id"]}/')
            self.assertEqual(HTTPStatus.OK, res.status_code)

    def test_delete_purchases(self):

        res = get('http://localhost:8000/purchases/')
        self.assertEqual(HTTPStatus.OK, res.status_code)

        results = loads(res.content).get('results', [])
        for i in results:
            res = delete(f'http://localhost:8000/purchases/{i["id"]}/')
            self.assertEqual(HTTPStatus.NO_CONTENT, res.status_code)

    def test_update_purchases(self):

        res = get('http://localhost:8000/purchases/')
        self.assertEqual(HTTPStatus.OK, res.status_code)

        results = loads(res.content).get('results', [])
        for i in results:
            purchase = i
            purchase["username"] = f'UpdatedUserName{i["id"]}'

            res = put(f'http://localhost:8000/purchases/{i["id"]}/', data=purchase)
            self.assertEqual(HTTPStatus.OK, res.status_code)

    def test_create_purchase_with_empty_body(self):

        p = {}
        res = post('http://localhost:8000/purchases/')
        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)

        fields = [
            'purchase_name',
            'user_id',
            'username',
            'phone_number',
            'email',
            'address',
        ]

        result = loads(res.content)

        error_message = 'This field is required.'
        for k in result.keys():
            self.assertIn(error_message, result[k])

    def test_create_purchase_with_bad_email(self):

        p = {
            'purchase_name': 'product1',
            'user_id': 'user1',
            'username': 'username1',
            'phone_number': '98912345678',
            'email': 'this is a bad email',
            'address': 'address1',
        }

        res = post('http://localhost:8000/purchases/', data=p)
        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)

        result = loads(res.content)

        error_message = 'Enter a valid email address.'
        self.assertIn(error_message, result['email'])

    def test_create_purchase_with_bad_phone_number(self):

        p = {
            'purchase_name': 'product1',
            'user_id': 'user1',
            'username': 'username1',
            'phone_number': 'this is a bad phone number',
            'email': 'test@example.com',
            'address': 'address1',
        }

        res = post('http://localhost:8000/purchases/', data=p)
        self.assertEqual(HTTPStatus.BAD_REQUEST, res.status_code)

        result = loads(res.content)

        error_message = 'Enter a valid value.'
        self.assertIn(error_message, result['phone_number'])

