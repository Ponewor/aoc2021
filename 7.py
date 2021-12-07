with open("7.in") as f:
    crabs = [int(x) for x in f.readline().split(',')]

print(min(sum(abs(i - crab) for crab in crabs) for i in range(min(crabs), max(crabs))))
print(min(sum((x := abs(i - crab)) * (x + 1) // 2 for crab in crabs) for i in range(min(crabs), max(crabs))))
