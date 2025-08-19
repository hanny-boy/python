import random
import string
def generate_password(length=8):
    c = list(string.ascii_letters + string.digits + string.punctuation)
    password = ''.join(random.choice(c) for i in range(length))
    return password
print("The random password generated is:", generate_password(8))