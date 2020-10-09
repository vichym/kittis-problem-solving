import sys

def convert(x):
    return round(x*1000*5280/4854)

if __name__ == '__main__':
    input = sys.stdin.read()
    convert(input)