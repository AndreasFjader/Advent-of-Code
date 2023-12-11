empty_row = set()
empty_col = set()
galaxies = []

spacemap = open('in.txt').read().splitlines()

for r, row in enumerate(spacemap):
        if all(i == '.' for i in row):
            empty_row.add(r)

for c in range(len(spacemap)):
    for r in range(len(spacemap[0])):
        if spacemap[r][c] == '#':
            break
    else:
        empty_col.add(c)

for r, row in enumerate(spacemap):
    for c, col in enumerate(row):
        if spacemap[r][c] == '#':
            # 1 for part 1, 999_999 for part 2
            cr = sum(999999 for num in empty_row if num < r)
            cc = sum(999999 for num in empty_col if num < c)
            galaxies.append((r + cr, c + cc))
    
min_dist = []        
while len(galaxies) > 1:
    g = galaxies.pop()
    
    for g2 in galaxies:
        d = abs(g2[0] - g[0]) + abs(g2[1] - g[1])
        min_dist.append(d)
    
print(sum(min_dist))