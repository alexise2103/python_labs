import os


def directories_tree(directory: str) -> int:
    count = 0
    for sub_dir in os.scandir(directory):
        if sub_dir.is_file():
            print(sub_dir.path)
            count +=1
        elif sub_dir.is_dir():
            directories_tree(sub_dir.path)

print(directories_tree('/home/alex/test'))
