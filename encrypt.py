import convert

def encrypt_1(text):
    num_list = convert.char_to_num(text)
    encrypt_key_short = input("Enter a encryption key(make it long):\n")
    encrypt_key = encrypt_key_short
    while len(encrypt_key) < len(num_list):
        encrypt_key += encrypt_key
    
    for count, n in enumerate(num_list):
        num_list[count] = n * int(encrypt_key[count])
    
    return num_list, encrypt_key_short

def decrypt_1(num_list, encrypt_key):
    while len(encrypt_key) < len(num_list):
        encrypt_key += encrypt_key
    
    for count, n in enumerate(num_list):
        num_list[count] = n // int(encrypt_key[count])
    
    return convert.num_to_char(num_list)


