#!/usr/bin/env python
import unittest


def get_value(v):
	us = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
	ts = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	ds = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	ss = ['hundred', 'thousand']
	if v in us: return (us.index(v) + 1)
	if v in ts: return (ts.index(v) + 11)
	if v in ds: return (ds.index(v) + 2) * 10
	return 0


def str_to_int(string):
	if string == 'zero': return 0
	if string == 'one million': return 1000000
	thousands = 0
	currvalue = 0
	for e in string.replace('-', ' ').replace(' and ', ' ').split(' '):
		if e == 'hundred':
			currvalue *= 100
		elif e == 'thousand':
			thousands = currvalue
			currvalue = 0
		else:
			currvalue += get_value(e)
	return thousands * 1000 + currvalue


class TestStrToInt(unittest.TestCase):
  def test_str_to_int1(self):
    self.assertEqual(str_to_int('one'), 1)
  
  def test_str_to_int2(self):
    self.assertEqual(str_to_int('thirteen'), 13)
  
  def test_str_to_int3(self):
    self.assertEqual(str_to_int('twenty'), 20)
  
  def test_str_to_int4(self):
    self.assertEqual(str_to_int('one hundred'), 100)
  
  def test_str_to_int5(self):
    self.assertEqual(str_to_int('three hundred and one'), 301)
  
  def test_str_to_int6(self):
    self.assertEqual(str_to_int('two hundred forty-six'), 246)
  
  def test_str_to_int7(self):
    self.assertEqual(str_to_int('seven hundred eighty-three thousand nine hundred and nineteen'), 783919)


if __name__ == '__main__':
  unittest.main()
