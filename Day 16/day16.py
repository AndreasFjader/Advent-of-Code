from collections import deque

grid = open('in.txt').read().splitlines()
mirrors = dict()

for r, row in enumerate(grid):
    for c, _ in enumerate(row):
        if grid[r][c] != '.':
            mirrors[(r, c)] = grid[r][c]
            
def is_outside_border(r, c):
    return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])

def get_starting_positions():
    Mr = len(grid)
    Mc = len(grid[0])
    sp = []
    
    sp.extend([(r, -1, 1) for r in range(Mr)])
    sp.extend([(r, Mc, 3) for r in range(Mr)])
    sp.extend([(-1, c, 2) for c in range(1, Mc)])
    sp.extend([(Mr, c, 0) for c in range(1, Mc)])
    return sp

flows = []
# print(get_starting_positions())
for sp in get_starting_positions():
    lava = deque()
    lava.append(sp)
    energized = set()
    seen = set()
    # lava.append((0, -1, 1)) # This is for part 1
    while lava:
        r, c, dir = lava.popleft()
        if (r, c, dir) in seen:
            continue
        seen.add((r, c, dir))
        energized.add((r, c))

        # Figure out next flow.
        nr = r
        nc = c

        if dir == 0: # Up
            nr -= 1
        elif dir == 1: # Right
            nc += 1
        elif dir == 2: # Down
            nr += 1
        elif dir == 3: # Left
            nc -= 1
            
        if is_outside_border(nr, nc):
            continue
        
        # If not collide with a mirror, continue as normal.
        if (nr, nc) not in mirrors:
            lava.append((nr, nc, dir))
            continue
            
        m = mirrors[(nr, nc)]
        if m == '|':
            if dir == 0 or dir == 2:
                lava.append((nr, nc, dir))
            else:
                lava.append((nr, nc, 0))
                lava.append((nr, nc, 2))
                
        elif m == '-':
            if dir == 1 or dir == 3:
                lava.append((nr, nc, dir))
            else:
                lava.append((nr, nc, 1))
                lava.append((nr, nc, 3))
        
        elif m == '/':
            if dir == 0:
                lava.append((nr, nc, 1))
            elif dir == 1:
                lava.append((nr, nc, 0))
            elif dir == 2:
                lava.append((nr, nc, 3))
            else:
                lava.append((nr, nc, 2))
                
        else:
            if dir == 0:
                lava.append((nr, nc, 3))
            elif dir == 1:
                lava.append((nr, nc, 2))
            elif dir == 2:
                lava.append((nr, nc, 1))
            else:
                lava.append((nr, nc, 0))
    flows.append((sp, len(energized)))

# print(flows)
print("Part 2:", max([(lambda x: x[1])(x) for x in flows]) - 1)