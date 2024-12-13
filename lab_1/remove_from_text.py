# Importing the re module
import re

with open('/home/alex/projects/python_labs/lab_1/example_text.txt', 'r') as f:
    text = f.read()


def remove_from_text(example_text: str, repl: str) -> str:
    return example_text.replace(repl, '').lstrip().rstrip()


def remove_from_text_re(example_text: str, repl: str) -> str:
    return re.sub(repl, '',example_text).lstrip().rstrip()


version_1 = remove_from_text(text, 'abc')
version_2 = remove_from_text_re(text, 'abc')
print('Text:', text)
print('Removed 1: ',version_1)
print('Removed 2:', version_2)

if version_1 == version_2:
    print('Good !!!')
else:
    print('Bad ;(')
