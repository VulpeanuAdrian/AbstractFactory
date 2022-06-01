import unittest
from unittest.mock import patch, call

from autos.ford.fiesta import FordFiesta


class TestFiesta(unittest.TestCase):
    fiesta_test_obj = FordFiesta()

    @patch('builtins.print')
    def test_start_fiesta(self):
        assert TestFiesta.fiesta_test_obj.start() == [call('Ford Fiesta running cheaply.')]

    @staticmethod
    @patch('builtins.print')
    def test_stop_fiesta(self):
        assert TestFiesta.fiesta_test_obj.stop() == [call('Ford Fiesta shutting down.')]


if __name__ == '__main__':
    unittest.main()
