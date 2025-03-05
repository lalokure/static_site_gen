import os
import sys

from generate_page import *  

base_dir = os.path.dirname(os.path.abspath(__file__))
print(base_dir)

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"
print(basepath)


def main():
    #node = TextNode("Test node", TextType.TEXT)
    #print(node)
    static_to_docs()
    md_path = os.path.join(base_dir, "..", "content")
    template_path = os.path.join(base_dir, "..", "template.html")
    dest_path = os.path.join(base_dir, "..", "docs") 
    generate_pages_recursive(md_path, template_path, dest_path, basepath)


def static_to_docs():
    static_path = os.path.join(base_dir, "..", "static") 
    public_path = os.path.join(base_dir, "..", "docs", "static")
    print(f"Copying from {static_path} to {public_path}")
    #shutil.rmtree(public_path, ignore_errors = True)
    os.mkdir(public_path)
    copy_files_and_directories(static_path, public_path)

if __name__ == "__main__":
    main()


