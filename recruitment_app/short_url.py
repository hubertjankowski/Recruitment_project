import random
import string


def shorten_url():
    stringLength = 6
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

