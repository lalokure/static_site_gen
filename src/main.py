import os
from textnode import TextType, TextNode


def main():
    #node = TextNode("Test node", TextType.TEXT)
    #print(node)
    cmds_testing()

def cmds_testing():
    path_test = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/static"
    print(os.path.exists(path_test))
    path_contents = os.listdir(path_test)
    print(path_contents)
    for content in path_contents:
        print(os.path.isfile(f"{path_test}/{content}"))

def static_to_public():
    shutil.rmtree()


if __name__ == "__main__":
    main()


