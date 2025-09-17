import unittest

from flask import json

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.order import Order  # noqa: E501
from openapi_server.test import BaseTestCase


class TestStoreController(BaseTestCase):
    """StoreController integration test stubs"""

    def test_delete_order(self):
        """Test case for delete_order

        Delete purchase order by identifier.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/store/order/{order_id}'.format(order_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_inventory(self):
        """Test case for get_inventory

        Returns pet inventories by status.
        """
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/api/v3/store/inventory',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_order_by_id(self):
        """Test case for get_order_by_id

        Find purchase order by ID.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v3/store/order/{order_id}'.format(order_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_place_order(self):
        """Test case for place_order

        Place an order for a pet.
        """
        order = {"petId":198772,"quantity":7,"id":10,"shipDate":"2000-01-23T04:56:07.000+00:00","complete":True,"status":"approved"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v3/store/order',
            method='POST',
            headers=headers,
            data=json.dumps(order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
