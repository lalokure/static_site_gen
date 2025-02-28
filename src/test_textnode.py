import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node3 = TextNode("Another text node", TextType.ITALIC, "url1")
        node4 = TextNode("Another text node", TextType.TEXT, "url2")
        self.assertNotEqual(node3, node4)
    
    def test_eq_url(self):
        node5 = TextNode("Another text node", TextType.TEXT, "url2")
        node6 = TextNode("Another text node", TextType.TEXT, "url2")
        self.assertEqual(node5, node6)

    def test_eq_text(self):
        node7 = TextNode("Another text node, the last", TextType.BOLD, "url1")
        node8 = TextNode("Another text node", TextType.BOLD, "url")
        self.assertNotEqual(node7, node8)

if __name__ == "__main__":
    unittest.main()
