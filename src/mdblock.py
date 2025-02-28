
def markdown_to_blocks(markdown): # markdown is a string written in md
    block_list = markdown.split("\n\n")
    blocks = []
    for block in block_list:
        block = block.strip()
        if block:
            if "\n" in block:
                block = "\n".join(map(lambda x: x.strip(), block.split("\n")))
                blocks.append(block)
                continue
        blocks.append(block)
    return blocks

