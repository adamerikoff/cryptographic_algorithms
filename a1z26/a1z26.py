ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
def encode(plain_text):
    result = []
    for i in plain_text:
        result.append(ALPHA.index(i.upper())+1)
    return result

def decode(crypted_text):
    result = []
    for i in crypted_text:
        result.append(ALPHA[int(i)-1])
    return result

def run_example():
    plain_text = input('Enter your text to encode: ')
    result = encode(plain_text)
    print(f'Encoded: {result}')
    print(f'Decoded: {decode(result)}')

run_example()