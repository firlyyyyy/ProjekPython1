import random
import string

def random_string(panjang:int) -> str:
    hasil_random_string = ''.join(random.choice(string.ascii_uppercase) for i in range(panjang))
    return hasil_random_string