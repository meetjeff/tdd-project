import unittest 

from money import Money
from portfolio import Portfolio

class TestMoney(unittest.TestCase):
    def testMutilplication(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def testDivision(self):
        originaMoney = Money(4002, "KRW")
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(
            expectedMoneyAfterDivision,
            originaMoney.divide(4)
        )

    def testAddition(self):
        fiveDollers = Money(5, "USD")
        tenDollers = Money(10, "USD")
        fifteenDollers = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollers, tenDollers)
        self.assertEqual(fifteenDollers, portfolio.evaluate("USD"))


if __name__ == '__main__':
    unittest.main()