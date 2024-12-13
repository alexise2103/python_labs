# Importing the re module
import re

with open('/home/alex/projects/python_labs/lab_1/example_text.txt', 'r') as f:
    text = f.read()

words = {'abc': '1', 'dzien': '2'}


def replace_in_text(example_text: str, words: dict) -> str:
    for key in words:
        example_text = example_text.replace(key, words[key])
    return example_text.lstrip().rstrip()


def replace_in_text_re(example_text: str, words: dict) -> str:
    for key in words:
        example_text = re.sub(key, words[key], example_text)
    return example_text.lstrip().rstrip()


version_1 = replace_in_text(text, words)
version_2 = replace_in_text_re(text, words)
print('Text:', text)
print('Removed 1: ', version_1)
print('Removed 2:', version_2)

if version_1 == version_2:
    print('Good !!!')
else:
    print('Bad ;(')
