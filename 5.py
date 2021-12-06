from collections import Counter


def g():
    d = Counter()

    for c1, c2, direction in vectors:
        if direction in legal_directions:
            while c1 != c2:
                d[c1] += 1
                c1 += direction
            d[c2] += 1
    print(sum(v > 1 for v in d.values()))


if __name__ == '__main__':
    vectors = []
    with open("5.in") as f:
        for line in f:
            t1, t2 = line.split(' -> ')
            a, b = [int(x) for x in t1.split(',')]
            p, q = [int(x) for x in t2.split(',')]

            c1 = a + b * 1j
            c2 = p + q * 1j
            r = c2 - c1
            direction = r / max(abs(r.real), abs(r.imag))
            vectors.append((c1, c2, direction))

    legal_directions = {1, -1, 1j, -1j}
    g()
    legal_directions.update((1+1j, 1-1j, -1+1j, -1-1j))
    g()
