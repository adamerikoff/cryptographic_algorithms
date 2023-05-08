import re

def xor(a, b):
    c = int(a)+int(b)
    if c == 2:
        return "0"
    else:
        return str(c)
        
def encode(plain_text, key):
    pass

def decode(crypted_text):
    pass

def run_example():
    plain_text = input('Enter your text to encode: ')
    result = encode(plain_text)
    print(f'Encoded: {result}')
    print(f'Decoded: {decode(result)}')

run_example()
