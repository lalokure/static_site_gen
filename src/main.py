import os
import shutil
from textnode import TextType, TextNode


def main():
    #node = TextNode("Test node", TextType.TEXT)
    #print(node)
    cmds_testing()
    static_to_public()


def cmds_testing():
    path_test = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/static"
    #print(os.path.exists(path_test))
    path_contents = os.listdir(path_test)
    #print(path_contents)
    #for content in path_contents:
    #    print(os.path.isfile(f"{path_test}/{content}"))


def static_to_public():
    static_path = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/static"
    public_path = "/Users/lalobec/workspace/github.com/lalokure/static_site_gen/public"
    shutil.rmtree(public_path, ignore_errors = True)
    os.mkdir(public_path)
    copy_files_and_directories(static_path, public_path)


def copy_files_and_directories(current_path, target_path):
    for content in os.listdir(current_path):
        print(content)
        path_to_copy = os.path.join(current_path, content)
        if os.path.isfile(path_to_copy):
            shutil.copy(path_to_copy, target_path)
            continue
        new_path = os.path.join(target_path, content)
        os.mkdir(new_path)
        copy_files_and_directories(path_to_copy, new_path)
    return


if __name__ == "__main__":
    main()


