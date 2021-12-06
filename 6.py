from collections import Counter

if __name__ == '__main__':
    with open("6.in") as f:
        c = Counter(int(x) for x in f.readline().split(','))

    for _ in range(80):
        c.update({7: c[0], 9: c[0]})
        c = Counter({k - 1: v for k, v in c.items() if k != 0})
    print(c.total())

    for _ in range(256 - 80):
        c.update({7: c[0], 9: c[0]})
        c = Counter({k - 1: v for k, v in c.items() if k != 0})
    print(c.total())
