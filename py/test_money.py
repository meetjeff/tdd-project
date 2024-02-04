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
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

    def testAdditionOfDollarsAndEuros(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, "USD")
        actualValue = portfolio.evaluate("USD")
        self.assertEqual(
            expectedValue, 
            actualValue, 
            "%s != %s" % (expectedValue, actualValue)
        )

    def testAdditionOfDollarsAndWons(self):
        oneDollar = Money(1, "USD")
        elevenHundredWon = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(oneDollar, elevenHundredWon)
        expectedValue = Money(2200, "KRW")
        actualValue = portfolio.evaluate("KRW")
        self.assertEqual(
            expectedValue,
            actualValue,
            "%s != %s" % (expectedValue, actualValue)
        )


if __name__ == '__main__':
    unittest.main()