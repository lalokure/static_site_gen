import unittest

from blocks import Block, BlockType, block_to_block_type

class TestBlock(unittest.TestCase):
    def test_eq(self):
        node = Block("```This is a code block```", BlockType.CODE)
        node2 = Block("```This is a code block```", BlockType.CODE)
        self.assertEqual(node, node2)
        # print("Block class is working")

    def test_btb_code(self):
        md_block = "```This should return a code block type```"
        type_of_block = block_to_block_type(md_block)
        #print(f"This is a {type_of_block} block")


    def test_btb_paragraph(self):
        md_block = "``This should return a paragraph block type```"
        type_of_block = block_to_block_type(md_block)
        #print(f"This is a {type_of_block} block")

    def test_btb_headings(self):
        block_list_test = []

        md_block1 = "## This is a second level heading"
        typeblock1 = block_to_block_type(md_block1)
        block_list_test.append(typeblock1)
        
        md_block2 = "#### This is a fourth level heading"
        typeblock2 = block_to_block_type(md_block2)
        block_list_test.append(typeblock2)
        
        md_block3 = "####### This is a seventh level heading"
        typeblock3 = block_to_block_type(md_block3)
        block_list_test.append(typeblock3)
        
        self.assertEqual(block_list_test, ["heading", "heading", "paragraph"])

    
    def test_btb_ul(self):
        
        md_list = """- This is the first line of a list block"""
        #print(block_to_block_type(md_list))
        md_list = """- This is the first line of a list block
        But with a new line without a dash, this should be a paragraph"""
        #print(block_to_block_type(md_list))
        md_list = """- This is the first line of a list block
        -This should be a paragraph too"""
        #print(block_to_block_type(md_list))
        md_list = """- This is the first line of a list block
- Now we are talking
- about a real block list"""
        #print(block_to_block_type(md_list))

    def test_btb_ol(self):
        test_list = []
        md_list = """1. This is the first line of an ordered list
2. Ok, we are going good"""
        test_list.append(block_to_block_type(md_list))
        #print(block_to_block_type(md_list))
        md_list = """1. This is the first line of an ordered list
2. Ok, we are going good
4. And now...?"""
        test_list.append(block_to_block_type(md_list))
        #print(block_to_block_type(md_list))
        md_list = """1. This is the first line of an ordered list
2. Ok, we are going good
3. All in order
4. Ok ok"""
        test_list.append(block_to_block_type(md_list))
        #print(block_to_block_type(md_list))

        self.assertEqual(test_list, ["ordered_list", "paragraph", "ordered_list"])

    def test_btb_quote(self):
        md_text = "> This is a quote"
        self.assertEqual(block_to_block_type(md_text), "quote")
