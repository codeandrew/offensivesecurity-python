import string
import random

char = string.ascii_letters + string.digits

def random(char):
    return random.choice(list(char))


