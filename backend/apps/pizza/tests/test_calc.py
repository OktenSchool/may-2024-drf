from unittest import TestCase
from ..service import calc, math

from unittest.mock import MagicMock, patch

class CalcTestCase(TestCase):
    # @patch('apps.pizza.service.cos')
    @patch.object(math, 'cos')
    def test_plus(self, mock_cos:MagicMock):
        mock_cos.return_value = 55
        res = calc(1,2,'+')
        self.assertEqual(res,57)

    def test_minus(self):
        res = calc(1,2,'-')
        self.assertEqual(res,-1)

    def test_multiply(self):
        res = calc(1,2,'*')
        self.assertEqual(res,2)