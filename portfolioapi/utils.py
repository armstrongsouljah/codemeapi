import random
import string


def gen_code(size, chars=string.ascii_lowercase+string.digits):
    return "".join(random.choice(chars) for _ in range(size))
