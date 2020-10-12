
str = ['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't']

def reverse_string(strlist):
    # reverse All String
    strlist.reverse()

    # initialize two pointer
    s = 0
    l = 0

    # loop through every char
    for i, c in enumerate(strlist):
        # perform word swap operation when encounter a space
        if c == " ":
            # last char position of word
            l = i - 1
            # swap char between s and l
            swap(strlist, s, l)
            # update start position for next word
            s = i + 1
    # swap the last word with no space at then end
    swap(strlist, s, len(strlist)-1)
    print(strlist)

def swap(arr, s, l):
    while s < l:
        temp = arr[s]
        arr[s] = arr[l]
        arr[l] = temp
        s += 1
        l -= 1


if __name__ == '__main__':
    reverse_string(str)
