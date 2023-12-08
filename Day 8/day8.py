from math import gcd

directions, nodes = open('in.txt').read().split('\n\n')
network = {}
sn = [] # Part 2
for node in nodes.split('\n'):
    p, n = node.split(' = ')
    l, r = n[1:-1].split(', ')
    network[p] = { 'L': l.strip(), 'R': r.strip() }
    
    if p[-1] == 'A':
        sn.append(p)

# Part 1
c = 'AAA'
t = 0
s = 0
while c != 'ZZZ':
    if s >= len(directions):
        s = 0
    d = directions[s]
    n = network[c][d]
    t += 1
    s += 1
    c = n
    
print("Part 1:", t)

# Part 2
s = 0
t = 0
seen = {}
l = True
while l:
    nn = []
    if s >= len(directions):
        s = 0
    d = directions[s]
    s += 1
    t += 1
    for node in sn:
        next = network[node][d]
        
        nn.append(next)
        if next[-1] == 'Z':
            if node not in seen:
                seen[node] = t
            
            if len(seen.keys()) == 6:
                l = False
    sn = nn

nrs = list(seen.values())
l = nrs.pop()
for nr in nrs:
    l = l * nr // gcd(l, nr)
    
print("Part 2:", l)