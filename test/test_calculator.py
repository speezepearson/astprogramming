import unittest
import ast
from astprogramming.operators import Pythonizer, PseudocodeGenerator
from astprogramming.examples.calculator import *

class TestCalculator(unittest.TestCase):
  def test_number(self):
    self.assertEqual(1, Pythonizer.evaluate(Number(1)))
    self.assertEqual('1', PseudocodeGenerator().call(Number(1)))

  def test_add(self):
    self.assertEqual(3, Pythonizer.evaluate(Add(Number(1), Number(2))))
    self.assertEqual('1 + 2', PseudocodeGenerator().call(Add(Number(1), Number(2))))

  def test_variable(self):
    python_ast = Pythonizer().call(Variable('x'))
    self.assertIsInstance(python_ast, ast.Name)
    self.assertEqual('x', python_ast.id)
    self.assertEqual('x', PseudocodeGenerator().call(Variable('x')))

  def test_assignment(self):
    python_ast = Pythonizer().call(Assignment(Variable('x'), Number(1)))
    self.assertIsInstance(python_ast, ast.Assign)
    self.assertEqual('x', python_ast.targets[0].id)
    self.assertEqual(1, python_ast.value.n)
    self.assertEqual('x = 1', PseudocodeGenerator().call(Assignment(Variable('x'), Number(1))))
