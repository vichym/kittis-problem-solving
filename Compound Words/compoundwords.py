from itertools import permutations
import sys

def compound(wordsList):
    compoundList = permutations(wordsList, 2)
    result = []
    for i in compoundList:
        word = i[0] + i[1]
        if word not in result:
            result.append(word)
    result.sort()
    for i in result:
        print(i)

if __name__ == '__main__':

    input = sys.stdin.read()
    words = input.split()
    compound(words)
