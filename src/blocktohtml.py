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
        count = 0
        while count < len(blocktext) and blocktext[count] == "#":
            count += 1
        node = HTMLNode(f"h{count}", blocktext[count:].strip())
    if blocktype == "code":
        blocktext = "\n".join(blocktext.split("\n")[1:-1])
        node = HTMLNode("pre", None, [HTMLNode("code", blocktext)])
    if blocktype == "quote":
        node = HTMLNode("blockquote", blocktext)
    if blocktype == "unordered_list":
        items = blocktext.splitlines()
        ulist = []
        for item in items:
            ulist.append(HTMLNode("li", item))
        node = HTMLNode("ul", None, [ulist])
    if blocktype == "ordered_list":
        items = blocktext.splitlines()
        olist = []
        for item in items:
            olist.append(HTMLNode("li", item))
        node = HTMLNode("ol", None, [olist])
    return node

   
