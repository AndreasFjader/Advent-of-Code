# I don't even care to clean this up.

def rotate_90(grid):
    row_count = len(grid)
    col_count = len(grid[0])
    
    rv = [['' for _ in range(row_count)] for _ in range(col_count)]
    for r in range(row_count):
        for c in range(col_count):
            rv[c][row_count - r - 1] = grid[r][c]
    
    return ["".join(x) for x in rv]

def find(grid: list):
    for i in range(1, len(grid)):
        a = grid[:i][::-1]
        b = grid[i:]
                
        if a[:len(b)] == b[:len(a)]:
            return i
    return 0

def find_p2(grid: list, line: int):
    for i in range(1, len(grid)):
        a = grid[:i][::-1]
        b = grid[i:]
        
        ab = list(zip(a, b))
        differences = [0 if x == y else 1 for aa, bb in ab for x, y in zip(aa, bb)]
        if sum(differences) == 1:
            return i
    return 0

th = 0
tth = 0
tv = 0
ttv = 0
pattern_map = {}
for i, pattern in enumerate(open('in.txt').read().split('\n\n')):
    p = pattern.splitlines()
    t = find(p)
    
    if t > 0:
        th += t
        pattern_map[i] = {
            "pattern": p,
            "line": t,
        }
        continue
    # check vertically as well
    pv = rotate_90(p)
    
    t2 = find(pv)
    if t2 > 0:
        pattern_map[i] = {
            "pattern": p,
            "line": t2,
        }
        tv += t2
        
print("Part 1:", tv + th * 100)


for pattern in pattern_map.values():
    p = pattern['pattern']
    l = pattern['line']
    
    tt = find_p2(p, l)
    if tt > 0:
        tth += tt
        continue
    
    pv = rotate_90(p)
    tt2 = find_p2(pv, l)
    if tt2 > 0:
        ttv += tt2
        

print("Part 2:", ttv + tth * 100)