from types import MappingProxyType
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from payments import PaymentStatus, RedirectNeeded
from payments_portmone import PortmoneProvider

PAYEE_ID = "test"
LOGIN = "login"
PASSWORD = "password"


PROCESS_DATA = MappingProxyType({})


class Payment(Mock):
    pk = 1
    variant = "portmone"
    currency = "UAH"
    total = 100
    status = PaymentStatus.WAITING
    captured_amount = 0
    message = ""

    def get_process_url(self):
        return "http://example.com"

    def get_failure_url(self):
        return "http://cancel.com"

    def get_success_url(self):
        return "http://success.com"

    def change_status(self, status, message=""):
        self.status = status
        self.message = message


class TestPortmoneProvider(TestCase):
    def setUp(self):
        self.payment = Payment()

    def test_process_data_redirects_to_success_on_payment_success(self):
        # TODO:
        pass

    def test_process_data_redirects_to_failure_on_payment_failure(self):
        # TODO:
        pass
