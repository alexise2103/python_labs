import os


def calculate_directories(directory:str) -> int:
    return len([sub_dir for sub_dir in os.scandir(directory) if sub_dir.is_dir()])


print(calculate_directories('/home/alex/test'))