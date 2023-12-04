#!/usr/bin/python3
"""text indentent module"""

def text_indentation(text):
    """function that prints a text with 2 lines after each of these chars: ",?:"
    Args:
        text: string
    Raises:
        TypeError: if text is not string
   """ 
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
