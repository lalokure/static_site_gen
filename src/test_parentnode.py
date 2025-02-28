import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_pnode_case1(self):
        simple_node = ParentNode("div", [LeafNode("p", "Hello")])
        result = simple_node.to_html()
        self.assertEqual(
            result,
            "<div><p>Hello</p></div>",
            "Simple parent node with one leaf child should render correctly"
        )

    def test_pnode_twoparents(self):
        pnode = ParentNode("section", [
            ParentNode("article", [
                LeafNode("p", "text")
                ])
            ])
        result = pnode.to_html()
        self.assertEqual(result, 
                         "<section><article><p>text</p></article></section>",
                         "Testing a nested parent node")

    def test_pnode_mixed(self):
        pnode =ParentNode("div", [
            LeafNode(None, "plain text"),
            ParentNode("p", [
                LeafNode("em", "emphasized")
                ]),
            LeafNode("br", "here was the problem")
            ])
        result = pnode.to_html()
        self.assertEqual(result,
                         "<div>plain text<p><em>emphasized</em></p><br>here was the problem</br></div>",
                         "Testing a mixed node")
