import sys

def read_input1():

    # read inputs
    w, l = input().split()
    if int(w)!=0 | int(l)!=0 :
        return [int(w),int(l),True]
    return [0,0,False]

def read_input2():
    steps = []
    num_step = int(input())
    # read steps
    for i in range(num_step):
        x, y = input().split()
        steps.append((x, int(y)))
    return steps

def calculate():
    while True:
        w,l,flag = read_input1()
        if not flag:
            break
        else:
            steps = read_input2()
            update_position(w, l, steps)

def update_actual(dist, max, current_position):
    distance = dist + current_position
    if distance < 0:
        return 0
    elif distance - max >= 0:
        return max-1
    elif distance - max < 0:
        return distance

def update_position(w, l,steps):
    sum_horizontal = 0
    sum_vertical = 0
    actual_horizontal = 0
    actual_vertical = 0
    for i, j in steps:
        if i == "u":
            sum_vertical += j
            actual_vertical = update_actual(j,l,actual_vertical)
        elif i == 'd':
            sum_vertical += -j
            actual_vertical = update_actual(-j, l ,actual_vertical)
        elif i == 'l':
            sum_horizontal += -j
            actual_horizontal= update_actual(-j, w, actual_horizontal)
        elif i == 'r':
            sum_horizontal += +j
            print(actual_horizontal)
            actual_horizontal = update_actual(j, w,actual_horizontal)
    print("Robot thinks ", sum_horizontal, sum_vertical)
    print("Actually at ",actual_horizontal, actual_vertical)
if __name__ == '__main__':
    calculate()
