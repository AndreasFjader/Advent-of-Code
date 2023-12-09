t1 = 0
t2 = 0
for value in open('in.txt').read().splitlines():
    seq = [int(v) for v in value.split()]
    first, last = [seq[0]], [seq[-1]]
    
    while not all(s == 0 for s in seq):
        seq2 = []
        for i in range(0, len(seq) - 1):
            seq2.append(seq[i + 1] - seq[i])
        last.append(seq2[-1])
        first.append(seq2[0])
        seq = seq2

    # Part 1
    lv = last.pop()
    last.reverse()
    for l in last:
        lv += l
    t1 += lv

    # Part 2
    fv = first.pop()
    first.reverse()
    for f in first:
        fv = (f - fv)
    t2 += fv
    
print("Part 1:", t1)
print("Part 2:", t2)
