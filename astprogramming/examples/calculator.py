import ast
import astprogramming

class Number(astprogramming.ASTNode):
  attribute_names = ('value',)
  def __init__(self, value, **kwargs):
    super().__init__(value=value, **kwargs)

astprogramming.operators.Pythonizer.set_method(Number, lambda self, node: ast.Num(node.value))
astprogramming.operators.PseudocodeGenerator.set_method(Number, lambda self, node: str(node.value))

class Add(astprogramming.ASTNode):
  child_names = ('left', 'right')
  def __init__(self, left, right, **kwargs):
    super().__init__(left=left, right=right, **kwargs)

astprogramming.operators.Pythonizer.set_method(Add, lambda self, node: ast.BinOp(op=ast.Add(), left=self.call(node.left), right=self.call(node.right)))
astprogramming.operators.PseudocodeGenerator.set_method(Add, lambda self, node: '{} + {}'.format(self.call(node.left), self.call(node.right)))

class Variable(astprogramming.ASTNode):
  attribute_names = ('name',)
  def __init__(self, name, **kwargs):
    super().__init__(name=name, **kwargs)

astprogramming.operators.Pythonizer.set_method(Variable, lambda self, node: ast.Name(id=node.name))
astprogramming.operators.PseudocodeGenerator.set_method(Variable, lambda self, node: node.name)

class Assignment(astprogramming.ASTNode):
  child_names = ('lhs', 'value')
  def __init__(self, lhs, value, **kwargs):
    super().__init__(lhs=lhs, value=value, **kwargs)

astprogramming.operators.Pythonizer.set_method(Assignment, lambda self, node: ast.Assign(targets=[self.call(node.lhs)], value=self.call(node.value)))
astprogramming.operators.PseudocodeGenerator.set_method(Assignment, lambda self, node: '{} = {}'.format(self.call(node.lhs), self.call(node.value)))
