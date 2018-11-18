#!/usr/bin/env python
import unittest


class RomanNumerals:
  @staticmethod
  def to_roman(n):
    return (
      ('', 'M', 'MM', 'MMM')[n // 1000 % 10] +
      ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')[n // 100 % 10] +
      ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')[n // 10 % 10] +
      ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')[n % 10]
    )
  
  @staticmethod
  def from_roman(r):
    values = (
      ('M', 1000), ('CM', -200), ('D', 500), ('CD', -200), ('C', 100),
      ('XC', -20), ('L', 50), ('XL', -20), ('X', 10), ('IX', -2),
      ('V', 5), ('IV', -2), ('I', 1)
    )
    return sum(r.count(s) * v for s, v in values)


class TestRomanNumerals(unittest.TestCase):
  def test_to_roman1(self):
    self.assertEqual(RomanNumerals.to_roman(1000), 'M')
  
  def test_to_roman2(self):
    self.assertEqual(RomanNumerals.to_roman(4), 'IV')
  
  def test_to_roman3(self):
    self.assertEqual(RomanNumerals.to_roman(1), 'I')
  
  def test_to_roman4(self):
    self.assertEqual(RomanNumerals.to_roman(1990), 'MCMXC')
  
  def test_to_roman5(self):
    self.assertEqual(RomanNumerals.to_roman(2009), 'MMIX')
  
  def test_from_roman1(self):
    self.assertEqual(RomanNumerals.from_roman('XXI'), 21)
  
  def test_from_roman2(self):
    self.assertEqual(RomanNumerals.from_roman('I'), 1)
  
  def test_from_roman3(self):
    self.assertEqual(RomanNumerals.from_roman('IV'), 4)
  
  def test_from_roman4(self):
    self.assertEqual(RomanNumerals.from_roman('MMVIII'), 2008)
  
  def test_from_roman5(self):
    self.assertEqual(RomanNumerals.from_roman('MDCLXVI'), 1666)


if __name__ == '__main__':
  unittest.main()
