#file handaling
def file_extention(filename):
    if not filename.endswith(".txt"):
        filename += ".txt"
    return filename

def save_text(text, filename):
    file = open(file_extention(filename), "w")
    file.write(text)

def save_numbers(num_list, filename):
    file = open(file_extention(filename), "w")
    for n in num_list:
        file.write(str(n) + "\n")
def load_text(filename):
    file = open(file_extention(filename), "r")
    return file.readline()

def load_numbers(filename):
    file = open(file_extention(filename), "r")
    num_list = []
    for line in file:
        num_list.append(line[0:-1])
    return num_list
