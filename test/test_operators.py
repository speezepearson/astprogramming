import unittest
import astprogramming

class DummyA(astprogramming.ASTNode):
  pass

class DummyB(astprogramming.ASTNode):
  pass

class TestOperator(unittest.TestCase):
  def setUp(self):
    class MyOperator(astprogramming.Operator):
      pass
    self.cls = MyOperator

  def test_call__selects_correct_method(self):
    self.cls.set_method(DummyA, (lambda self, node: 'a'))
    self.cls.set_method(DummyB, (lambda self, node: 'b'))

    self.assertEqual('a', self.cls().call(DummyA()))

  def test_call__raises_when_no_method(self):
    self.cls.set_method(DummyA, (lambda self, node: None))
    with self.assertRaises(TypeError):
      self.cls().call(DummyB())

  def test_call__respects_node_inheritance(self):
    class DummyAB(DummyA, DummyB):
      pass

    self.cls.set_method(astprogramming.ASTNode, (lambda self, node: 'top'))
    self.assertEqual('top', self.cls().call(astprogramming.ASTNode()))
    self.assertEqual('top', self.cls().call(DummyA()))
    self.assertEqual('top', self.cls().call(DummyB()))
    self.assertEqual('top', self.cls().call(DummyAB()))

    self.cls.set_method(DummyB, (lambda self, node: 'b'))
    self.assertEqual('top', self.cls().call(astprogramming.ASTNode()))
    self.assertEqual('top', self.cls().call(DummyA()))
    self.assertEqual('b', self.cls().call(DummyB()))
    self.assertEqual('b', self.cls().call(DummyAB()))

    self.cls.set_method(DummyAB, (lambda self, node: 'ab'))
    self.assertEqual('top', self.cls().call(astprogramming.ASTNode()))
    self.assertEqual('top', self.cls().call(DummyA()))
    self.assertEqual('b', self.cls().call(DummyB()))
    self.assertEqual('ab', self.cls().call(DummyAB()))

    self.cls.set_method(DummyA, (lambda self, node: 'a'))
    self.assertEqual('top', self.cls().call(astprogramming.ASTNode()))
    self.assertEqual('a', self.cls().call(DummyA()))
    self.assertEqual('b', self.cls().call(DummyB()))
    self.assertEqual('ab', self.cls().call(DummyAB()))

  def test_call__respects_operator_inheritance(self):
    class OperatorVariant(self.cls):
      pass

    self.cls.set_method(DummyA, (lambda self, node: 'superA'))
    self.assertEqual('superA', OperatorVariant().call(DummyA()))

    OperatorVariant.set_method(DummyB, (lambda self, node: 'subB'))
    self.assertEqual('superA', OperatorVariant().call(DummyA()))
    self.assertEqual('subB', OperatorVariant().call(DummyB()))

    OperatorVariant.set_method(DummyA, (lambda self, node: 'subA'))
    self.assertEqual('subA', OperatorVariant().call(DummyA()))

  def test_def_method(self):
    @self.cls.def_method(DummyA)
    def f(self, node):
      return 'a'

    self.assertEqual('a', self.cls().call(DummyA()))

