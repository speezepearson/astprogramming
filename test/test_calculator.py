import unittest
from astprogramming.operators import Pythonizer
from astprogramming.examples.calculator import *

class TestCalculator(unittest.TestCase):
  def test_basics(self):
    self.assertEqual(1, Pythonizer.evaluate(Number(1)))
    self.assertEqual(3, Pythonizer.evaluate(Add(Number(1), Number(2))))
