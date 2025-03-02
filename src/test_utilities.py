import unittest
from textnode import TextType, TextNode
from utilities import *

class TestTxtToHTML(unittest.TestCase):
    
    def test_text(self):
        text_node = TextNode("Hello world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello world!"
        #assert html_node.children == []
        # Test bold node
        bold = TextNode("Bold text", TextType.BOLD)
        html = text_node_to_html_node(bold)
        assert html.tag == "b", "Bold node should have 'b' tag"
        assert html.value == "Bold text", "Bold node value should be preserved"

        # Add a test for link
        link = TextNode("Click me", TextType.LINK, "https://www.example.com")
        html = text_node_to_html_node(link)
        assert html.tag == "a", "Link should have 'a' tag"
        assert html.value == "Click me", "Link text should be preserved"
        assert html.props == {"href": "https://www.example.com"}, "Link should have href prop"

    def test_nullvalues(self):
        try:
            text_node = TextNode("Lets see what happens", None)
            html_node = text_node_to_html_node(text_node)
            assert False, "Should have raised TypeError"
        except TypeError:
            pass


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_not_text_type(self):
        node = TextNode("*The bold line*", TextType.BOLD)
        new_node = split_nodes_delimiter([node], "*", TextType.BOLD)
        assert new_node == [node]
        # print("First test passed!")

    def test_bold(self):
        node = TextNode("This is a **bold** text", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        assert len(new_node) == 3
        #print("Testing a text with a bold string... \n Test #1 passed.")
        assert new_node[0].text == "This is a "
        assert new_node[0].text_type == TextType.TEXT
        #print("Test #2 passed.")
        assert new_node[1].text == "bold"
        assert new_node[1].text_type == TextType.BOLD
        #print("Test #3 passed.")
        assert new_node[2].text == " text"
        assert new_node[2].text_type == TextType.TEXT
        # print("Test bold passed!")

    def test_italic(self):
        node = TextNode("This is a *italic text* line", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "*", TextType.ITALIC)
        assert len(new_node) == 3
        #print("Testing a text with a italic string... \n Test #1 passed.")
        assert new_node[0].text == "This is a "
        assert new_node[0].text_type == TextType.TEXT
        #print("Test #2 passed.")
        assert new_node[1].text == "italic text"
        assert new_node[1].text_type == TextType.ITALIC
        #print("Test #3 passed.")
        assert new_node[2].text == " line"
        assert new_node[2].text_type == TextType.TEXT
        # print("Test italic passed!")

    def test_code(self):
        node = TextNode("This is a `code block`, only suited for programmers", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(new_node) == 3
        #print("Testing a text with a code block... \n Test #1 passed.")
        assert new_node[0].text == "This is a "
        assert new_node[0].text_type == TextType.TEXT
        #print("Test #2 passed.")
        assert new_node[1].text == "code block"
        assert new_node[1].text_type == TextType.CODE
        #print("Test #3 passed.")
        assert new_node[2].text == ", only suited for programmers"
        assert new_node[2].text_type == TextType.TEXT
        #print("Test code passed!")

    def test_complex_bold_cases(self):
        nodes = [
                TextNode("Normal text", TextType.TEXT),
                TextNode("Already bold", TextType.BOLD),
                TextNode("Start **bold** middle **more bold** end", TextType.TEXT),
                TextNode("No change here", TextType.CODE),
                ]

        new_node = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        
        #print("Testing a more complex bold case")
        assert len(new_node) == 8
        #print("Test #1 - passed")
        
        assert new_node[0].text == "Normal text"
        assert new_node[0].text_type == TextType.TEXT
        
        assert new_node[1].text == "Already bold"
        assert new_node[1].text_type == TextType.BOLD
        
        assert new_node[2].text == "Start "
        assert new_node[2].text_type == TextType.TEXT
        
        assert new_node[3].text == "bold"
        assert new_node[3].text_type == TextType.BOLD
        
        assert new_node[4].text == " middle "
        assert new_node[4].text_type == TextType.TEXT
        
        assert new_node[5].text == "more bold"
        assert new_node[5].text_type == TextType.BOLD
        
        assert new_node[6].text == " end"
        assert new_node[6].text_type == TextType.TEXT

        assert new_node[7].text == "No change here"
        assert new_node[7].text_type == TextType.CODE

class TestExtractImage_nLink(unittest.TestCase):
    def test_extract_image(self):
        test_text = """
            Here is a [regular link](https://example.com) 
            and here is an ![image link](https://image.com)
            and another [link to test](https://test.com)
            """
        image_alt, image_link = extract_markdown_images(test_text)[0]
        links = extract_markdown_links(test_text)
        #print(f"Images found: {image_alt}, {image_link}")
        #print("Links found: ", links)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        #print("This image was found too")

    def test_split_oneimage(self):
        node = TextNode("This is an image ![perrito](https://perritos.com) of perritos", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
                [
                    TextNode("This is an image ", TextType.TEXT),
                    TextNode("perrito", TextType.IMAGE, "https://perritos.com"),
                    TextNode(" of perritos", TextType.TEXT)
                    ], 
                new_nodes
                )
        #print("Perritos test ok!")

    # This is the test from the lesson:
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        #print("Lane test passed!")

    # Boots test
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and another [second link](https://www.test.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.test.com"),
            ],
            new_nodes,
        )
        #print("Boots test passed!")

    # One more test from me
    def test_split_links_morenodes(self):
        node = TextNode(
            "This is text with a [link](https://www.example.com) and another [second link](https://www.test.com). A new line.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.example.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.test.com"),
                TextNode(". A new line.", TextType.TEXT)
            ],
            new_nodes,
        )
        #print("Improved boots test passed!")

    def test_text_to_textnodes(self):
        nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ], nodes,
        )
        #print("Another Lane test passed!")

if __name__ == "__main__":
    unittest.main()
