from django.test import TestCase
from json import loads
from requests import post, put, delete, get
from http import HTTPStatus


class TestCrudPurchase(TestCase):
    _NUMBER_OF_REQUESTS = 10

    def test_create_purchase(self):

        for i in range(self._NUMBER_OF_REQUESTS):
            p = {
                "purchase_name": f"purchase{i}",
                "user_id": 100,
                "user_name": "user1",
                "phone_number": "+0987654321",
                "email": "test1@example.com",
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
            purchase["user_name"] = f'UpdatedUserName{i["id"]}'

            res = put(f'http://localhost:8000/purchases/{i["id"]}/', data=purchase)
            self.assertEqual(HTTPStatus.OK, res.status_code)

