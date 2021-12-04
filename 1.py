from more_itertools import windowed

if __name__ == '__main__':
    with open("1.in") as f:
        nums = [int(line) for line in f]

    print(sum(a < b for a, b in windowed(nums, 2)))

    print(sum(a + b + c < p + q + r for (a, b, c), (p, q, r) in windowed(windowed(nums, 3), 2)))
