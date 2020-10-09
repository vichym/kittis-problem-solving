
def prison():
    r = input()
    c = input()
    hl = input()
    h = []
    for i in range(hl):
        h.append(input())
    vl = input()
    v = []
    for i in range(hl):
        v.append(input())
    prison(r, c, h, v)
    row = [i for i in range(r + 1)]
    col = [i for i in range(c + 1)]

    for x in h:
        row.remove(x)
    for y in v:
        col.remove(y)
    diffX = max([ row[i+1]-row[i] for i in range(0, r-1)])
    diffY = max([ col[i+1]-col[i] for i in range(0, c-1)])

    print(row, col, diffX, diffY,diffX*diffY)
    return diffX*diffY

if __name__ == '__main__':
    r = input()
    c = input()
    hl = input()
    h = []
    for i in range(hl):
        h.append(input())
    vl = input()
    v=[]
    for i in range(hl):
        v.append(input())
    prison(r,c,h,v)


