import ast
import astprogramming

class Number(astprogramming.ASTNode):
  attribute_names = ('value',)
  def __init__(self, value, **kwargs):
    super().__init__(value=value, **kwargs)

astprogramming.operators.Pythonizer.set_method(Number, lambda self, node: ast.Num(node.value))

class Add(astprogramming.ASTNode):
  child_names = ('left', 'right')
  def __init__(self, left, right, **kwargs):
    super().__init__(left=left, right=right, **kwargs)

astprogramming.operators.Pythonizer.set_method(Add, lambda self, node: ast.BinOp(op=ast.Add(), left=self.call(node.left), right=self.call(node.right)))
