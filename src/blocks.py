from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

class Block:
    def __init__(self, text, block_type):
        self.text = text
        self.block_type = block_type

    def __eq__(self, other):
        if isinstance(other, Block):
            return self.text == other.text and self.block_type == other.block_type
        return False

    def __repr__(self):
        return f"Block({self.text}, {self.text_type.value})"


def block_to_block_type(block): # block is just a string
    if block.startswith("#"):
        if block.startswith("#######"):
            block_obj = Block(block, BlockType.PARAGRAPH)
            return block_obj.block_type.value
        block_obj = Block(block, BlockType.HEADING)
        return block_obj.block_type.value
    if block.startswith("```") and block.endswith("```"):
        block_obj = Block(block, BlockType.CODE)
        return block_obj.block_type.value
    if block.startswith(">"):
        block_obj = Block(block, BlockType.QUOTE)
        return block_obj.block_type.value
    if block.startswith("- "):
        lines = block.splitlines()
        for line in lines:
            if all((line.startswith("- ") for line in lines)):
                block_obj = Block(block, BlockType.UNORDERED_LIST)
                return block_obj.block_type.value
        block_obj = Block(block, BlockType.PARAGRAPH)
        return block_obj.block_type.value
    if block.startswith("1. "):
        lines = block.splitlines()
        is_ol_sofar = True
        for i in range(0, len(lines)):
            if lines[i].startswith(f"{i+1}. ") and is_ol_sofar == True:
                is_ol_sofar = True
            else:
                is_ol_sofar = False
                break
        if is_ol_sofar == True:
            block_obj = Block(block, BlockType.ORDERED_LIST)
            return block_obj.block_type.value
        block_obj = Block(block, BlockType.PARAGRAPH)
        return block_obj.block_type.value
    block_obj = Block(block, BlockType.PARAGRAPH)
    return block_obj.block_type.value




"""
def block_to_block_type(block): # block is just a string
    match block:
        case block.startswith("```"):
            block_obj = Block(block, BlockType.CODE)
            return block_obj.BlockType.value
        case _:
            print("This is a test")
"""

