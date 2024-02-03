import unittest
import functools
import operator

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
    
    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)
    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency
    

class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, 
            map(lambda m: m.amount, self.moneys),
            0
        )
        return Money(total, currency)


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollers(self):
        fiveDollers = Money(5, "USD")
        tenDollers = Money(10, "USD")
        self.assertEqual(tenDollers, fiveDollers.times(2))

    def testMutilplicationInEuros(self):
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