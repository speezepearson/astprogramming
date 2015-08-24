class Operator:
  @classmethod
  def _ensure_has_own_operator_methods(cls):
    if 'operator_methods' not in vars(cls):
      cls.operator_methods = {}

  @classmethod
  def set_method(cls, node_cls, function):
    cls._ensure_has_own_operator_methods()
    cls.operator_methods[node_cls] = function

  def call(self, node):
    return self.operator_methods[type(node)](self, node)

from .pythonizer import Pythonizer