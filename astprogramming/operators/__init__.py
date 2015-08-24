import collections

class TypeDict:
  def __init__(self):
    self.dict = {}

  def __getitem__(self, cls):
    cls = self._closest_key(cls)
    if cls is None:
      raise KeyError('neither {} nor any superclass in dict'.format(key.__name__))
    return self.dict[cls]

  def __setitem__(self, key, value):
    self.dict[key] = value

  def __delitem__(self, key):
    del self.dict[key]

  def __iter__(self):
    return iter(self.dict)

  def __len__(self, key):
    return len(self.dict)

  def __contains__(self, cls):
    return (self._closest_key(cls) is not None)

  def _closest_key(self, cls):
    for sup in cls.__mro__:
      if sup in self.dict:
        return sup
    return None


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

  @classmethod
  def method_for_class(cls, node_class):
    for sup in cls.__mro__:
      if 'operator_methods' in vars(sup):
        if node_class in sup.operator_methods:
          return sup.operator_methods[node_class]
    return None

  def call(self, node):
    method = self.method_for_class(type(node))
    if method is None:
      raise TypeError('no method for nodes of type {}'.format(type(node).__name__))
    return method(self, node)

from .pythonizer import Pythonizer
