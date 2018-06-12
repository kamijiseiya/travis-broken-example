import unittest

from sample_a import SampleA


class TestSampleA(unittest.TestCase):
  def test_a1(self):
    print('Test sample A1')
    a = SampleA()
    a.hello()

  def test_a2(self):
    print('Test sample A2')

  def a3(self):
    print('Test sample A3')
