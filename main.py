import encrypt

a = input("Enter some text:\n")
b,c = encrypt.e_1(a)
print(b)
print(c)
print(encrypt.decrypt_1(b,c))
