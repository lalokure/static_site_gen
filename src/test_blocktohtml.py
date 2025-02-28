import unittest

from blocktohtml import *

class TestBlockToHTML(unittest.TestCase):
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
"""
        result = markdown_to_html_node(md)
        print(result)

'''
    def test_lanetest(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        result = markdown_to_html_node(md)
        print(result)
'''


