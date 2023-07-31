from collections import defaultdict

stacks = list(range(1, 18+1))
stacks.extend([
    20,
    21,
    22,
    23,
    24,
    25,
    29,
    30,
    38,
    39,
    40,
    41,
    46,
    47,
    50,
    51,
    53,
    57,
    64,
])
valid = set(stacks)

freq = defaultdict(set)
for i, a in enumerate(stacks):
    for b in stacks[i:]:
        prod = a * b
        if prod < 128:
            freq[prod].add(a)
            freq[prod].add(b)

fl = [list(x) for x in list(freq.items())]
fl.sort(key=lambda x: len(x[1]))

counter = 1
while fl:
    num, multiples = fl.pop()
    print(counter, num, multiples)
    counter += 1

    # Update fl to remove popped multiples
    for i, group in enumerate(fl):
        fl[i][1] -= multiples

    fl.sort(key=lambda x: len(x[1]))
