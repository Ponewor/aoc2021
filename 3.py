if __name__ == '__main__':
    with open("3.in") as f:
        lines = f.readlines()

    top = ["0"] * 12
    worst = ["0"] * 12
    for i in range(12):
        ith_digits = [line[i] for line in lines]
        top[i], worst[i] = ("1", "0") if ith_digits.count("1") > ith_digits.count("0") else ("0", "1")
    print(int(''.join(top), 2) * int(''.join(worst), 2))

    copied_lines = lines.copy()
    for i in range(12):
        ith_digits = [line[i] for line in lines]
        top = "1" if ith_digits.count("1") >= ith_digits.count("0") else "0"
        lines = [line for line in lines if line[i] == top]
    ox = int(lines[0], 2)

    lines = copied_lines
    for i in range(12):
        ith_digits = [line[i] for line in lines]
        worst = "0" if ith_digits.count("1") >= ith_digits.count("0") else "1"
        lines = [line for line in lines if line[i] == worst]
        if len(lines) == 1:
            co2 = int(lines[0], 2)
    print(co2 * ox)
