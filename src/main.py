import os

from generate_page import *  
from textnode import TextType, TextNode


def main():
    #node = TextNode("Test node", TextType.TEXT)
    #print(node)
    static_to_public()
    md_path = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/content"
    template_path ="/Users/lalobec/workspace/github.com/lalokure/static_site_gen/template.html"
    dest_path = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/public"
    generate_pages_recursive(md_path, template_path, dest_path)


def static_to_public():
    static_path = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/static"
    public_path = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/public"
    shutil.rmtree(public_path, ignore_errors = True)
    os.mkdir(public_path)
    copy_files_and_directories(static_path, public_path)



if __name__ == "__main__":
    main()


