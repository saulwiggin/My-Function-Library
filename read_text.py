import re
def get_text(map):
    """Read text from a file, normalizing whitespace and stripping HTML markup"""
    text = open(map).read()
    text = re.sub('\s+', ' ', text)
    text = re.sub(r'<.*?>', ' ', text)
    return text
