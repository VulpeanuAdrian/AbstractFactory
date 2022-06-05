import unittest
from unittest.mock import patch, call
from autos.ford.fiesta import FordFiesta

class TestFiesta(unittest.TestCase):
    fiesta_test_obj = FordFiesta()

    @patch('builtins.print')
    def test_start_fiesta(self,mocked_print):
        mocked_print.mock_calls == [call('Ford Fiesta running cheaply.'),TestFiesta.fiesta_test_obj.start()]

    @patch('builtins.print')
    def test_stop_fiesta(self,mocked_print):
        mocked_print.mock_calls == [TestFiesta.fiesta_test_obj.stop(),call('Ford Fiesta shutting down.')]


if __name__ == '__main__':
    unittest.main()
