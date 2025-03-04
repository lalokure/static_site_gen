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
    return ParentNode("div", nodes)


# Other helper functions

def block_to_html_node(blocktext, blocktype):
    if blocktype == "paragraph":
        #node = HTMLNode("p", blocktext)
        node = ParentNode("p", text_to_children(blocktext.replace("\n", " ").strip()))
    if blocktype == "heading":
        count = 0
        while count < len(blocktext) and blocktext[count] == "#":
            count += 1
        blockhead = blocktext[count:].strip()
        node = ParentNode(f"h{count}", text_to_children(blockhead))
    if blocktype == "code":
        blocktext = "\n".join(blocktext.split("\n")[1:-1])
        node = ParentNode("pre", [LeafNode("code", blocktext)])
    if blocktype == "quote":
        quote_text = ""
        lines = blocktext.splitlines()
        for line in lines:
            if line.startswith("> "):
                quote_text += line[1:]
            else:
                pass
        node = ParentNode("blockquote", text_to_children(quote_text.strip()))
    if blocktype == "unordered_list":
        items = blocktext.splitlines()
        ulist = []
        for item in items:
            ulist.append(ParentNode("li", text_to_children(item[1:].strip())))
        node = ParentNode("ul", ulist)
    if blocktype == "ordered_list":
        items = blocktext.splitlines()
        olist = []
        for item in items:
            olist.append(ParentNode("li", text_to_children(item[2:].strip())))
        node = ParentNode("ol", olist)
    return node

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    #print(textnodes)
    htmlnodes = []
    for textnode in textnodes:
        htmlnodes.append(text_node_to_html_node(textnode))
    return htmlnodes

   
