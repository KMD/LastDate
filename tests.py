import unittest

from firstdate import FirstDate, IncorrectInputString


class TestDateFunction(unittest.TestCase):

    def test_exeptions(self):
        self.assertRaises(IncorrectInputString, FirstDate, "110")
        self.assertRaises(IncorrectInputString, FirstDate, "11/0")
        self.assertRaises(IncorrectInputString, FirstDate, "2/1/1/0")
        self.assertRaises(IncorrectInputString, FirstDate, "2/x/0")
        self.assertRaises(IncorrectInputString, FirstDate, "2/x/z")
        self.assertRaises(IncorrectInputString, FirstDate, "a/3/0")

    def test_exeptions_values(self):
        self.assertRaises(IncorrectInputString, FirstDate, "10/3200/0")
        self.assertRaises(IncorrectInputString, FirstDate, "2011/20/20")
        self.assertRaises(IncorrectInputString, FirstDate, "2011/20/0")
        self.assertRaises(IncorrectInputString, FirstDate, "2011/40/3")
        self.assertRaises(IncorrectInputString, FirstDate, "2100/2/29")

    def test_zero(self):
        self.assertEqual(FirstDate('1/1/0').__str__(), '2000-01-01')
        self.assertEqual(FirstDate('0/1/1').__str__(), '2000-01-01')
        self.assertEqual(FirstDate('1/00/1').__str__(), '2000-01-01')

    def test_ones(self):
        self.assertEqual(FirstDate('2/3/1').__str__(), '2001-02-03')
        self.assertEqual(FirstDate('20/7/1').__str__(), '2001-07-20')
        self.assertEqual(FirstDate('10/1/20').__str__(), '2001-10-20')

    def test_four_digt(self):
        self.assertEqual(FirstDate('1/1/2000').__str__(), '2000-01-01')
        self.assertEqual(FirstDate('3/2001/1').__str__(), '2001-01-03')
        self.assertEqual(FirstDate('1/4/2002').__str__(), '2002-01-04')
        self.assertEqual(FirstDate('28/2/2100').__str__(), '2100-02-28')


if __name__ == '__main__':
    unittest.main()
