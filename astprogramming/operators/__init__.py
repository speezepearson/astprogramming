import collections

class TypeDict:
  def __init__(self):
    self.dict = {}

  def __getitem__(self, key):
    for cls in key.__mro__:
      if cls in self.dict:
        return self.dict[cls]
    raise KeyError('neither {} nor any superclass in dict'.format(key.__name__))

  def __setitem__(self, key, value):
    self.dict[key] = value

  def __delitem__(self, key):
    del self.dict[key]

  def __iter__(self):
    return iter(self.dict)

  def __len__(self, key):
    return len(self.dict)

class Operator:
  @classmethod
  def _ensure_has_own_operator_methods(cls):
    if 'operator_methods' not in vars(cls):
      cls.operator_methods = TypeDict()

  @classmethod
  def set_method(cls, node_cls, function):
    cls._ensure_has_own_operator_methods()
    cls.operator_methods[node_cls] = function

  @classmethod
  def def_method(cls, node_cls):
    def decorate(function):
      cls.set_method(node_cls, function)
      return function
    return decorate

  def call(self, node):
    try:
      method = self.operator_methods[type(node)]
    except KeyError:
      pass # raises TypeError; see comment below
    else:
      return method(self, node)
    # I'd put this in the "except KeyError" block, but that obscures the traceback.
    raise TypeError('no method for nodes of type {}'.format(type(node).__name__))

from .pythonizer import Pythonizer
