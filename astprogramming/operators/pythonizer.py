import ast
from . import Operator

class Pythonizer(Operator):
  @classmethod
  def evaluate(cls, node, **kwargs):
    pythonizer = cls(**kwargs)
    t = ast.fix_missing_locations(ast.Expression(pythonizer.call(node)))
    return eval(compile(t, filename='<ast>', mode='eval'))
