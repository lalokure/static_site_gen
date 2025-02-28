import re

from leafnode import LeafNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            if not text_node.text:
                raise ValueError("TextNode for NORMAL must include 'value'.")
            return LeafNode("", text_node.text, None)
        case TextType.BOLD:
            if not text_node.text:
                raise ValueError("TextNode for BOLD must include 'value'.")
            return LeafNode("b", text_node.text, None) 
        case TextType.ITALIC:
            if not text_node.text:
                raise ValueError("TextNode for ITALIC must include 'value'.")
            return LeafNode("i", text_node.text, None)
        case TextType.CODE:
            if not text_node.text:
                raise ValueError("TextNode for CODE must include 'value'.")
            return LeafNode("code", text_node.text, None)
        case TextType.LINK:
            if not text_node.url or not text_node.text:
                raise ValueError("TextNode for LINK must include 'url' and a proper anchor.")
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            if not text_node.url or not text_node.text:
                raise ValueError("TextNode for IMAGE must include both 'url' and 'value'.")
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise TypeError("That is not a valid text type.")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            lines = old_node.text.split(delimiter)
            if len(lines) % 2 == 0:
                raise Exception("Invalid Markdown syntax.")
            elif len(lines) == 1:
                new_nodes.append(TextNode(lines[0], TextType.TEXT))
            else:
                for i in range(0, len(lines)):
                    if i % 2 == 0:
                        txtnode = TextNode(lines[i], TextType.TEXT)
                        new_nodes.append(txtnode)
                    else:
                        txtnode = TextNode(lines[i], text_type)
                        new_nodes.append(txtnode)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        image_md = extract_markdown_images(old_node.text)
        if image_md == [] and old_node.text != "":
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for i in range(len(image_md)):
            image_alt, image_link = image_md[i]
            img_node = TextNode(image_alt, TextType.IMAGE, image_link)
            lines = remaining_text.split(f"![{image_alt}]({image_link})", 1)
            if lines[0] != "":
                new_nodes.append(TextNode(lines[0], TextType.TEXT))
            new_nodes.append(img_node)
            if i == len(image_md)-1 and lines[1] != "":
                new_nodes.append(TextNode(lines[1], TextType.TEXT))
            remaining_text = lines[1]
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        links_md = extract_markdown_links(old_node.text)
        if links_md == [] and old_node.text != "":
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for i in range(len(links_md)):
            link_text, link_itself = links_md[i]
            link_node = TextNode(link_text, TextType.LINK, link_itself)
            lines = remaining_text.split(f"[{link_text}]({link_itself})", 1)
            if lines[0] != "":
                new_nodes.append(TextNode(lines[0], TextType.TEXT))
            new_nodes.append(link_node)
            if i == len(links_md)-1 and lines[1] != "":
                new_nodes.append(TextNode(lines[1], TextType.TEXT))
            remaining_text = lines[1]
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT, None)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes
    



