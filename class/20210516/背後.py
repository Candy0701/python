sts = [1, 10, 10, 1000, 0, 0]

def write_file(sts):
    path = 'output.txt'
    f = open(path, 'w')
    for i in sts:
        f.write(str(i) + "\n")
    f.close()
def read_file():
    f = open(path, 'r')
    text = []
    for line in f:
        text.append(int(line))
    print(text)
    f.close()
    return text