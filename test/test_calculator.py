import unittest
from astprogramming.operators import Pythonizer, PseudocodeGenerator
from astprogramming.examples.calculator import *

class TestCalculator(unittest.TestCase):
  def test_evaluation(self):
    self.assertEqual(1, Pythonizer.evaluate(Number(1)))
    self.assertEqual(3, Pythonizer.evaluate(Add(Number(1), Number(2))))

  def test_pseudocode(self):
    self.assertEqual('1', PseudocodeGenerator().call(Number(1)))
    self.assertEqual('1 + 2', PseudocodeGenerator().call(Add(Number(1), Number(2))))
