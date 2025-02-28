from blocks import BlockType, Block, block_to_block_type
from htmlnode import HTMLNode
from leafnode import *
from mdblock import markdown_to_blocks
from parentnode import *
from textnode import *
from utilities import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    blocktypes = []
    nodes = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        node = block_to_html_node(block, blocktype)
        blocktypes.append(blocktype)
        nodes.append(node)
    return blocktypes, nodes


# Other helper functions

def block_to_html_node(blocktext, blocktype):
    if blocktype == "paragraph":
        node = HTMLNode("p", blocktext)
    if blocktype == "heading":
        pass
    if blocktype == "code":
        node = HTMLNode("code", blocktext)
    if blocktype == "quote":
        node = HTMLNode("blockquote", blocktext)
    if blocktype == "unordered_list":
        node = HTMLNode("ul", blocktext)
    if blocktype == "ordered_list":
        node = HTMLNode("ol", blocktext)
    return node



    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
