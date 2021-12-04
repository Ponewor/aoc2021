if __name__ == '__main__':
    with open("2.in") as f:
        steps = [((elem := line.split())[0], int(elem[1])) for line in f]

    hor = 0
    dep = 0
    for command, num in steps:
        if command == "forward":
            hor += num
        elif command == "down":
            dep += num
        else:
            dep -= num
    print(hor * dep)

    hor = 0
    dep = 0
    aim = 0
    for command, num in steps:
        if command == "forward":
            hor += num
            dep += aim * num
        elif command == "down":
            aim += num
        else:
            aim -= num
    print(hor * dep)
