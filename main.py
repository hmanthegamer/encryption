from encrypt import encrypt_1, decrypt_1
from text_handle import save_text, save_numbers, load_text, load_numbers

def encrypt_file(filename):
    text = load_text(filename)
    encrypted, key = encrypt_1(text)
    save_numbers(encrypted, filename)
    return key

def decrypt_file(filename, key):
    numbers = load_numbers(filename)
    numbers = list(numbers)
    num_list = []
    for i in numbers:
        num_list.append(int(i))
    save_text(decrypt_1(num_list, key), "test")
