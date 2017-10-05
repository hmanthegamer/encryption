
#converts string of characters to a list of numbers
def char_to_num(string):
    string = string.lower()
    key = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    result = []
    for char in string:
        try:
            result.append(key.index(char))
        except ValueError:
            continue
    return (result)

#converts list of numbers to string
def num_to_char(num_list):
    key = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    result = []
    for num in num_list:
        result.append(key[num])
    return "".join(result)

def encrypt(num_list, encrypt_key):
    for count, n in enumerate(num_list):
        num_list[count] = n * int(encrypt_key[count])
    return num_list

def decrypt(num_list, encrypt_key):
    for count, n in enumerate(num_list):
        num_list[count] = n // int(encrypt_key[count])
    return num_list

