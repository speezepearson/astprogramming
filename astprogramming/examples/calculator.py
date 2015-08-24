import ast
import astprogramming

class Number(astprogramming.ASTNode):
  def __init__(self, value):
    self.value = value

astprogramming.operators.Pythonizer.set_method(Number, lambda self, node: ast.Num(node.value))

class Add(astprogramming.ASTNode):
  def __init__(self, left, right):
    self.left = left
    self.right = right

astprogramming.operators.Pythonizer.set_method(Add, lambda self, node: ast.BinOp(op=ast.Add(), left=self.call(node.left), right=self.call(node.right)))
