import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_neq_tag_value(self):
        hnode = HTMLNode("p", "This is a paragraph")
        hnode2 = HTMLNode("p", "This is a paragraph")
        self.assertNotEqual(hnode, hnode2)

    def test_neq_all(self):
        hnode = HTMLNode(
            tag="div",
            value=None,  # Since it has children, we don't need a value
            children=[
                HTMLNode(tag="p", value="First paragraph"),
                HTMLNode(tag="p", value="Second paragraph")
            ],
            props={
                "class": "container",
                "style": "color: blue"
            }
        )
        hnode2 = HTMLNode(
            tag="div",
            value=None,  # Since it has children, we don't need a value
            children=[
                HTMLNode(tag="p", value="First paragraph"),
                HTMLNode(tag="p", value="Second paragraph")
            ],
            props={
                "class": "container",
                "style": "color: blue"
            }
        )
        self.assertNotEqual(hnode, hnode2)


if __name__ == "__main__":
    unittest.main()



