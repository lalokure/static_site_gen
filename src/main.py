import os
import sys

from generate_page import *  
from textnode import TextType, TextNode

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"
print(basepath)


def main():
    #node = TextNode("Test node", TextType.TEXT)
    #print(node)
    static_to_docs()
    md_path = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/content"
    template_path ="/Users/lalobec/workspace/github.com/lalokure/static_site_gen/template.html"
    dest_path = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/docs"
    generate_pages_recursive(md_path, template_path, dest_path, basepath)


def static_to_docs():
    static_path = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/static"
    public_path = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/docs"
    shutil.rmtree(public_path, ignore_errors = True)
    os.mkdir(public_path)
    copy_files_and_directories(static_path, public_path)

if __name__ == "__main__":
    main()


