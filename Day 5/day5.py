seeds, *maps = open('in.txt').read().split('\n\n')
seeds = list(map(int, seeds.split(': ')[1].split()))
maps = [[list(map(int, x.split())) for x in m.splitlines()[1:]] for m in maps]

# Part 1
res_p1 = set()
for seed in seeds:
    nr = seed
    for m in maps:
        for d, s, r in m:
            if s <= nr <= (s + r - 1):
                nr = d + (nr - s)
                break
    res_p1.add(nr)

print("Part 1:", min(res_p1))

# Part 2
res_p2 = []
seed_ranges = [(seeds[x], seeds[x] + seeds[x + 1]) for x in range(0, len(seeds), 2)]

for m in maps:
    next = []
    while len(seed_ranges) > 0:
        start, end = seed_ranges.pop()
        for d, s, r in m:
            batch_start = max(start, s)
            batch_end = min(end, s + r)
            if batch_start < batch_end:
                # batches outside the "start" and "end" may still contain valid seed ranges. 
                if batch_start > start:
                    seed_ranges.append((start, batch_start))
                if batch_end < end:
                    seed_ranges.append((batch_end, end))
                # these ones are valid seed ranges for the next map, so we give them their destination range numbers.
                next.append((batch_start - s + d, batch_end - s + d))
                break
        else:
            # in case there was no batch overlapping, we check the next map instead.
            next.append((start, end))
    seed_ranges = next
    
print("Part 2:",min(seed_ranges)[0])