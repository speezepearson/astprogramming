import unittest
import astprogramming


class Number(astprogramming.ASTNode):
  attribute_names = ('value',)

class Add(astprogramming.ASTNode):
  child_names = ('left', 'right')

class Attribute(astprogramming.ASTNode):
  child_names = ('object',)
  attribute_names = ('attr',)

class TestASTNode(unittest.TestCase):

  def test_definition_with_attribute_names(self):
    self.assertEqual(3, Number(value=3).value)

  def test_definition_with_child_names(self):
    child = Add(left=None, right=None)
    parent = Add(left=child, right=None)
    self.assertIs(child, parent.left)

  def test_definition_with_attribute_and_child_names(self):
    child = Attribute(object=None, attr='child_attr')
    parent = Attribute(object=child, attr='parent_attr')

    self.assertIs(child, parent.object)
    self.assertEqual('parent_attr', parent.attr)

  def test_repr(self):
    self.assertEqual('Number(value=3)', repr(Number(value=3)))
    self.assertEqual(
      'Add(left=Number(value=3), right=Number(value=4))',
      repr(Add(left=Number(value=3), right=Number(value=4))))

  def test_eq_and_hash(self):
    x1 = Attribute(object=Number(value=3), attr='conjugate')
    x2 = Attribute(object=Number(value=3), attr='conjugate')
    y = Attribute(object=Number(value=3), attr='other_attribute')
    z = Attribute(object=Number(value=99), attr='conjugate')
    self.assertEqual(x1, x2)
    self.assertEqual(hash(x1), hash(x2))
    self.assertNotEqual(x1, y)
    self.assertNotEqual(x1, z)
    self.assertNotEqual(y, z)

    self.assertNotEqual(Number(value=3), Add(left=Number(value=3), right=Number(value=4)))

  def test_eq__similar_class_definitions(self):
    class A(astprogramming.ASTNode): pass
    class B(astprogramming.ASTNode): pass

    self.assertEqual(A(), A())
    self.assertNotEqual(A(), B())

    class LooksLikeNumber(astprogramming.ASTNode):
      attribute_names = ('value',)
    self.assertNotEqual(Number(value=3), LooksLikeNumber(value=3))
