import unittest

from blocktohtml import *
from htmlnode import HTMLNode
from parentnode import ParentNode

class TestBlockToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        #print(node)
        html = node.to_html()
        #print(html)
        self.assertEqual(
                html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
        print("Lane test passed!!!")

    def test_codeblock(self):
        md = """
This is text that _should_ remain
the **same** even with inline stuff
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(html)
        #self.assertEqual(
         #   html,
          #  "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        #)
        #print("Another checked Lanetest")

    def test_construction_test(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

```
This is python coding
```

And now we have an ordered list:

1. This is the number one
2. Then the number two
3. It is three
4. Four and is over

Now an unordered list:

- Necesito comprar manzanas
- Muchas naranjas
- Y ver el video completo de como hacer masa madre

> Life is too short to try to understand it.

# Pasos para hacer la masa madre

## Necesitamos masa sin blanquear y masa de grano entero

### El equipo necesario es el que necesitamos


"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(html)

    def test_simple_paragraph(self):
        md = "This is a simple paragraph."
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a simple paragraph.</p></div>"
        )

    def test_heading(self):
        md = "# This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1></div>"
        )

    def test_unordered_list(self):
        md = """
    - Item 1
    - Item 2
    - Item 3
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        )

    def test_mixed_blocks(self):
        md = """
        # Main Heading

        This is a paragraph with **bold** and _italic_ text.

        ## Subheading

        - List item with code
        - Another item with a link

        > This is a blockquote with **formatting** is the problem here?
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)
        #self.assertEqual(
        #        html,
        #        "<div><h1>Main Heading</h1><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><h2>Subheading</h2><ul><li>List item with code</li><li>Another item with a link</li></ul><blockquote>This is a blockquote with <b>formatting</b> is the problem here?</blockquote></div>"
         #       )
