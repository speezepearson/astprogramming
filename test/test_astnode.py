import unittest
import astprogramming

class TestASTNode(unittest.TestCase):

  def test_definition_with_attribute_names(self):
    class Number(astprogramming.ASTNode):
      attribute_names = ('value',)
    self.assertEqual(3, Number(value=3).value)

  def test_definition_with_child_names(self):
    class Add(astprogramming.ASTNode):
      child_names = ('left', 'right')
    child = Add(left=None, right=None)
    parent = Add(left=child, right=None)
    self.assertIs(child, parent.left)

  def test_definition_with_attribute_and_child_names(self):
    class Attribute(astprogramming.ASTNode):
      child_names = ('object',)
      attribute_names = ('attr',)
    child = Attribute(object=None, attr='child_attr')
    parent = Attribute(object=child, attr='parent_attr')

    self.assertIs(child, parent.object)
    self.assertEqual('parent_attr', parent.attr)
