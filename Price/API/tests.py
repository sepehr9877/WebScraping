from pprint import pprint

from django.test import TestCase
import requests
# Create your tests here.
class Api_test(TestCase):
    def setUp(self):
        self.url="http://127.0.0.1:8000/"
    def test_get_prameter(self):
        prameter="USDT-USD"
        url=self.url+"?q="+prameter
        request_url=requests.request(method="get",url=url)
        pprint(request_url.text)