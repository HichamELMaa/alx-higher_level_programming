#!/usr/bin/python3
def text_indentation(text):
    """
    Prints the given text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    indent_text = ""

    for char in text:
        indent_text += char
        if char in punctuation:
            indent_text += "\n\n"

    print(indent_text.strip())
