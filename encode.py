from baseN_to_int import baseN_to_int
from int_to_baseN import int_to_baseN
from Loader import load_charsets

char_set, d62 = load_charsets()

def encode(text):
    text = text.strip()
    if not text:
        raise ValueError("Input is empty.")
    if text.isdigit():
        num = int(text)
    else:
        num = baseN_to_int(text, char_set)
    return int_to_baseN(num, d62)