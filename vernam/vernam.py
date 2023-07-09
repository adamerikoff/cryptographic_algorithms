def xor(a, b):
    c = int(a)+int(b)
    if c == 2:
        return "0"
    else:
        return str(c)

def binary_element(element):
    binary_code = bin(ord(element))[2:]
    if len(binary_code) < 8:
        binary_code =  ("0"*(8-len(binary_code))) + binary_code
    return "".join(binary_code)
     
def binary_list(lst):
    binary_list = []
    for i in lst:
        binary_list.append(binary_element(i))
    return binary_list

def extend_key(key, text_len):
    if len(key) > text_len:
        return key[0:text_len-1]
    else:
        key = key*(text_len//len(key)) + key[0:(text_len%len(key))]
        return key

def encode(plain_text, key):
    encoded = []
    binary_text = binary_list(plain_text)
    binary_key = extend_key(binary_list(key), len(binary_text))

    stacked_binary_text = "".join(binary_text)
    stacked_binary_key = "".join(binary_key)

    for i in zip(stacked_binary_text, stacked_binary_key):
        encoded.append(xor(i[0],i[1]))
    encoded = "".join(encoded)
    encoded = [encoded[i:i+8] for i in range(0, len(encoded), 8)]

    result = []
    for e in encoded:
        char = chr(int(e, 2)).replace("\n","")
        result.append(char)
    return "".join(result)

def decode(crypted_text, key):
    decoded = []
    binary_text = binary_list(crypted_text)
    binary_key = extend_key(binary_list(key), len(binary_text))

    stacked_binary_text = "".join(binary_text)
    stacked_binary_key = "".join(binary_key)

    for i in zip(stacked_binary_text, stacked_binary_key):
        decoded.append(xor(i[0],i[1]))
    decoded = "".join(decoded)
    decoded = [decoded[i:i+8] for i in range(0, len(decoded), 8)]

    result = []
    for e in decoded:
        char = chr(int(e, 2)).replace("\n","")
        result.append(char)
    return "".join(result)

def run_example():
    #plain_text = input('Enter your text to encode: ')
    key = "SECRET_WORD"
    result = encode("When pride comes, then comes disgrace, but with humility comes wisdom!", key)
    print(f'Encoded: {result}')
    dresult = decode(result, key)
    print(f'Decoded: {dresult}')

run_example()
