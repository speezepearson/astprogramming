class ASTNode:
  attribute_names = ()
  child_names = ()

  def __init__(self, **kwargs):
    for field_name in self.field_names:
      setattr(self, field_name, kwargs.pop(field_name))
    super().__init__(**kwargs)

  @property
  def field_names(self):
    return tuple(self.attribute_names) + tuple(self.child_names)
