# MAIN PACKAGE

class ASTNode:
  pass

class Visitor:
  @classmethod
  def _ensure_has_own_visitation_methods(cls):
    if 'visitation_methods' not in vars(cls):
      cls.visitation_methods = {}

  @classmethod
  def set_visitation_method(cls, node_cls, function):
    cls._ensure_has_own_visitation_methods()
    cls.visitation_methods[node_cls] = function

  def visit(self, node):
    return self.visitation_methods[type(node)](self, node)



# SUBPACKAGE

class Pythonizer(Visitor):
  pass



# APPLICATION

class Number(ASTNode):
  def __init__(self, value):
    self.value = value

class Add(ASTNode):
  def __init__(self, left, right):
    self.left = left
    self.right = right

import ast
Pythonizer.set_visitation_method(Number, lambda self, node: ast.Num(node.value))
Pythonizer.set_visitation_method(Add, lambda self, node: ast.BinOp(op=ast.Add(), left=self.visit(node.left), right=self.visit(node.right)))
def evaluate(node):
  t = ast.fix_missing_locations(ast.Expression(Pythonizer().visit(node)))
  return eval(compile(t, filename='<ast>', mode='eval'))


import unittest
class TestEverything(unittest.TestCase):
  def test_basics(self):
    self.assertEqual(3, evaluate(Add(Number(1), Number(2))))

if __name__ == '__main__':
  unittest.main()