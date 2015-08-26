import nodes

class ASTNode(nodes.Node):
  attribute_names = ()
  child_names = ()

  def __init__(self, **kwargs):
    for field_name in self.field_names:
      setattr(self, field_name, kwargs.pop(field_name))
    super().__init__(**kwargs)

  @property
  def field_names(self):
    return tuple(self.attribute_names) + tuple(self.child_names)

  @property
  def children(self):
    for name in self.child_names:
      child = getattr(self, name)
      if child is not None:
        yield child

  def __repr__(self):
    return '{typename}({args})'.format(
      typename=type(self).__name__,
      args=', '.join(
        '{name}={value!r}'.format(
          name=name,
          value=getattr(self, name))
        for name in self.field_names))

  def __eq__(self, other):
    return (
      type(self) is type(other) and
      all(getattr(self, name) == getattr(other, name) for name in self.field_names))

  def __hash__(self):
    return hash(tuple(getattr(self, name) for name in self.field_names))

  def __setattr__(self, name, value):
    if name in self.child_names:
      if hasattr(self, name):
        old_value = getattr(self, name)
        if old_value is not None:
          old_value.parent = None
      if value is not None:
        value.parent = self
    super().__setattr__(name, value)
