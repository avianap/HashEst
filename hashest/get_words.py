import re

def tokenize(text):
    """Tokenize a string, expand known contractions, if unknown contraction, take first half of word

    :param str text: the string of text to be tokenized

    :rtype: list
    """
    return re.findall("[\'\w\-]+", text.lower())

