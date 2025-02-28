import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_lnode_noprops(self):
        lnode = LeafNode("p", "Hello world")
        lnode2 = LeafNode("p", "Hello world")
        self.assertEqual(lnode, lnode2)

    def test_lnode_notag(self):
        lnode = LeafNode(None, "Hello world", {"href": "https://example.com"})
        lnode2 = LeafNode(None, "Hello world", {"href": "https://example.com"})
        self.assertEqual(lnode, lnode2)

    def test_lnode(self):
        lnode = LeafNode("a", "Click me!", {"href": "https://example.com"})
        lnode2 = LeafNode("a", "Click me!", {"href": "https://example.com"})
        self.assertEqual(lnode, lnode2)

if __name__ == "__main__":
    unittest.main()
