def read_input():
    try:
        x, y = list(map(int,input().split()))
        num_step = int(input())
    except Exception:
        raise Exception.__class__

    steps = []
    for _ in range(num_step):
        steps.append(input().lower())
    return [x,y,steps]

def debug():
    # inputs
    x,y,steps = read_input()

    # Generate alternative options for each steps
    alternate = generate_alternate(steps)

    # run simulation: change every step with either option from alternative list
    for o in range(len(steps)):
        # choose between alternative list
        for a in range(2):
            # replace 'o' step with its alternative
            temp = steps[:o] + [alternate[o][a]] + steps[o+1:]
            # run simulation
            sx,sy = simulation(temp)
            # compare simulation
            if (sx,sy) == (x,y):
                # print the pos = index + 1 and correct alternative step
                print(o+1, alternate[o][a])
                return
    return -1

def simulation(steps):
    y = 0
    x = 0
    heading = 0 # 0: North, 1: East,2:South,3:West
    for i in steps:
        x,y, heading = simulation_move(x, y, heading, i)
    return (x,y)

def simulation_move(x,y, heading, instruction):
    if instruction == "forward":
        # heading North, + y
        if heading == 0:
            y += 1
        # heading South, - y
        elif heading == 2:
            y -= 1
        # heading East, + x
        elif heading == 1:
            x += 1
        # heading West, - x
        else:
            x -= 1
    elif instruction == "right":
        heading = (heading + 1)%4
    elif instruction == "left":
        heading = (heading - 1)%4
    return (x, y, heading)

def generate_alternate(steps):
    alternate = []
    for s in steps:
        if s == "right":
            alternate.append(("left", "forward"))
        elif s == "left":
            alternate.append(("right", "forward"))
        elif s == "forward":
            alternate.append(("left", "right"))
    return alternate
if __name__ == '__main__':
    debug()
