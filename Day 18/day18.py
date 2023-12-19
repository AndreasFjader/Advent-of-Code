cc = (0,0)
boundaries = {cc}
corners = []

def fill_between_points(cc, d, l, part):
    r, c = cc
    for mv in range(l):
        if d == 'U':
            r -= 1
        elif d == 'R':
            c += 1
        elif d == 'D':
            r += 1
        elif d == 'L':
            c -= 1
        
        if part == 1:
            boundaries.add((r, c))
        else:
            boundaries2.add((r, c))      
    if part == 1:
        corners.append((r, c))
    else:
        corners2.append((r, c))
    return (r, c)

# Solve
hex_plan = []
for plan in open('in.txt').read().splitlines():
    d, l, _h = plan.split()
    hex_plan.append(_h[1:-1])
    cc = fill_between_points(cc, d, int(l), 1)

mr = min(boundaries, key=lambda x: x[0])[0]
Mr = max(boundaries, key=lambda x: x[0])[0]
mc = min(boundaries, key=lambda x: x[1])[1]
Mc = max(boundaries, key=lambda x: x[1])[1]

total = 0
b = len(boundaries)

# i = A - (b / 2) + 1
# A = for (r, c) in corners -> abs[x * (c_prev - c_next)]
A = 0
for i, (r, c) in enumerate(corners):
    A += r * (corners[i - 1][1] - corners[(i + 1) % len(corners)][1])

A = abs(A // 2)
i = A - (b // 2) + 1
total = i + b # Inside + outside

print("Part 1:", total)

# Part 2
corners2 = [(0,0)]
boundaries2 = set()
border_length = 0
for hex in hex_plan:
    l, d = int(hex[1:-1], 16), int(hex[-1])
    border_length += l
    dir = "RDLU"[d]
    nr, nc = (0, 1) if dir == 'R' else (1, 0) if dir == 'D' else (0, -1) if dir == 'L' else (-1, 0)
    r, c = corners2[-1]
    corners2.append((r + nr * l, c + nc * l))

total = 0

# i = A - (b / 2) + 1
# A = for (r, c) in corners -> abs[x * (c_prev - c_next)]
A2 = 0
for i, (r, c) in enumerate(corners2):
    A2 += r * (corners2[i - 1][1] - corners2[(i + 1) % len(corners2)][1])

A2 = abs(A2 // 2)
i2 = A2 - (border_length // 2) + 1
total2 = i2 + border_length # Inside + outside

print("Part 2:", total2)