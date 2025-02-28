from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props) # children is a list of nodes
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("A ParentNode must have a tag")
        if self.children is None:
            raise ValueError("A ParentNode must have a children")
        html_string = f"<{self.tag}>"
        for child in self.children:
            html_string += f"{child.to_html()}"
        html_string += f"</{self.tag}>"
        return html_string

