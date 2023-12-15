grid = open('in.txt').read().splitlines()
rocks = set()
solid = set()

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'O':
            rocks.add((r, c))
        elif grid[r][c] == '#':
            solid.add((r, c))

def get_score(rocks: set):
    l = len(grid)
    sc = 0
    for r, c in rocks:
        sc += l - r
        
    return sc

def run_cycle(rocks: set, first_part: bool):
    for i, (nr, nc) in enumerate([(-1, 0), (0, -1), (1, 0), (0, 1)]):
        moved = True
        while moved:
            moved = False
            moved_rocks = set()
            for (r, c) in rocks:
                if (r == 0 and i == 0) or (c == 0 and i == 1) or (r >= len(grid) - 1 and i == 2) or (c >= len(grid[0]) - 1 and i == 3):
                    moved_rocks.add((r, c))
                    continue
                n = (r + nr, c + nc)
                if n in rocks or n in solid:
                    moved_rocks.add((r, c))
                    continue
                
                moved_rocks.add(n)
                moved = True
            rocks = moved_rocks.copy()
        if first_part:
            return rocks
    
    return rocks

p1 = run_cycle(rocks, True)
print("Part 1:", get_score(p1))

# Part 2
MAX_CYCLES = 1000000000
cycle = 0
seen = set(tuple(rocks))
grids = [rocks]

while True:
    rocks = run_cycle(rocks, False)
    cycle += 1
    
    if tuple(rocks) in seen:
        first_found_index = grids.index(rocks)
        rep_len = cycle - first_found_index
        last_grid = grids[((MAX_CYCLES - first_found_index) % rep_len) + first_found_index]
        print("Part 2:", get_score(last_grid))
        exit()
    
    grids.append(rocks)
    seen.add(tuple(rocks))
    