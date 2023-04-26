ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    ]
def encode(plain_text, key):
    output = list(
        map(
            lambda x: 
                ALPHABET[(ALPHABET.index(x.lower())+key)%len(ALPHABET)], 
            plain_text
        )
    )
    return output

def decode(crypted_text, key):
    output = list(
        map(
            lambda x: 
                ALPHABET[(ALPHABET.index(x.lower())-key)%len(ALPHABET)], 
            crypted_text
        )
    )
    return output

def run_example():
    plain_text = input('Enter your text to encode: ')
    key = int(input('Enter shift value: '))
    result = encode(plain_text, key)
    print(f'Encoded: {result}')
    print(f'Decoded: {decode(result, key)}')

run_example()