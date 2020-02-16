
def checkLine(line):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    line = line.lower()
    for i in line:
        if i in alphabet:
            alphabet = alphabet.replace(i,'')
    if(len(alphabet) ==0):
        print("pangram")
    else:
        print("missing "+ alphabet)

if __name__ == '__main__':
    num_line = input()
    for i in range(int(num_line)):
        line = input()
        checkLine(line)