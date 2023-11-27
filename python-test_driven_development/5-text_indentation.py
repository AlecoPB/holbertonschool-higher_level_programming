#!/usr/bin/python3
"""
This is module documentation
"""


def text_indentation(text):
    """
    This is function documentation
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    text = text.replace('\n\n  ', '\n\n')
    text = text.replace('\n\n ', '\n\n')
    print(text, end="")
