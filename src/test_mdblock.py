import unittest
from mdblock import *

class TestMdtoBlock(unittest.TestCase):

    def test_simple_case(self):
        md = """
            # Heading

            This is a paragraph.

            - List item 1

            - List item 2
        """
        #blocks = markdown_to_blocks(md)
        ##print(blocks)


    def test_md_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
        """

        blocks = markdown_to_blocks(md)
        #print(blocks)

        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        #print("Lane test passed!")

    def test_md_block_numbertwo(self):
        md = """
            This is an _italic_ line. Lets see if this works.
            This is the same paragraph but another line.

            `Here I could have a code block, but this is not one of them`

            Finally, a numbered list:

            1. First item
            2. Second item
            3. Third item
        """
        blocks = markdown_to_blocks(md)
        #print(blocks)
        
        self.assertEqual(blocks,
                         [
                             "This is an _italic_ line. Lets see if this works.\nThis is the same paragraph but another line.",
                             "`Here I could have a code block, but this is not one of them`",
                             "Finally, a numbered list:",
                             "1. First item\n2. Second item\n3. Third item",
                             ],
                         )
        #print("Another test passed!")
