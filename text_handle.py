#file handaling

def save(data, filename):
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    file = open(filename, "w")
    file.write(data)

def load(filename):
    if not filename.endswith(".txt"):
        filename += ".txt"
    file = open(filename, "r")
    return file.readline()
