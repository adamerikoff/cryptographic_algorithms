import re

def encode(plain_text):
    plain_text = plain_text.replace(" ", "")
    result = list(map(lambda x: bin(ord(x))[2:].replace("0", "a").replace("1", "b"), plain_text))
    return "".join(result)

def decode(crypted_text):
    result = list(map(lambda x: chr(int(x.replace("a","0").replace("b","1"), 2)), re.findall(r"[ab]{6,7}", crypted_text)))
    return "".join(result)

def run_example():
    plain_text = input('Enter your text to encode: ')
    result = encode(plain_text)
    print(f'Encoded: {result}')
    print(f'Decoded: {decode(result)}')

run_example()
