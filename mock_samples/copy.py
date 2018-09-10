from unittest import TestCase
from unittest.mock import patch
import main
from main import Calculator

class TestCalculator(TestCase):

    # using mock patch
    @patch('main.Calculator.sum', return_value=6)
    def test_sum(self, sum):
        self.assertEqual(sum(2, 4), 6)

    # using normal unit testing
    def setUp(self):
        self.calc = Calculator()

    def test_two(self):
        ans = self.calc.sum(2,5)
        self.assertEqual(ans,7)

if __name__ == '__main__':
    with patch('main.func.CreateAccount') as mockAccount:
        mockAccount.CreateAccount.return_value = (50,1)

    main.Calculator.accounts(5)
