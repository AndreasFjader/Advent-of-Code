from heapq import heappop, heappush

grid = open('in.txt').read().splitlines()

UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

# heat loss | x | y | current dir | steps in same dir | seen
heap = [(0, 0, 0, UP, 0)]
seen = set()

# Part 1
while heap:
    hl, r, c, cd, sdr = heappop(heap)
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        print("Part 1:", hl)
        break

    up, right, down, left = (r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)
    if hl == 0:
        next_steps = [down, right]
    elif cd == UP:
        next_steps = [right, left, up] if sdr < 3 else [right, left]
    elif cd == RIGHT:
        next_steps = [up, down, right] if sdr < 3 else [up, down]
    elif cd == DOWN:
        next_steps = [right, left, down] if sdr < 3 else [right, left]
    elif cd == LEFT:
        next_steps = [up, down, left] if sdr < 3 else [up, down]

    for nr, nc in next_steps:
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            continue

        dir = UP if (nr, nc) == up else RIGHT if (nr, nc) == right else DOWN if (nr, nc) == down else LEFT
        same_dir_steps = 1 if dir != cd else sdr + 1
        
        if (r, c, dir, same_dir_steps) in seen:
            continue
        seen.add((r, c, dir, same_dir_steps))

        heat_loss = hl + int(grid[nr][nc])
        heappush(heap, (heat_loss, nr, nc, dir, same_dir_steps))
        
# Part 2
heap2 = [(0, 0, 0, UP, 0)]
seen.clear()
while heap2:
    hl, r, c, cd, sdr = heappop(heap2)
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        print("Part 2:", hl)
        break

    up, right, down, left = (r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)
    if sdr < 4:
        if hl == 0:
            next_steps = [down, right]
        else:
            next_steps = [up if cd == UP else right if cd == RIGHT else down if cd == DOWN else left]
    else:
        if hl == 0:
            next_steps = [down, right]
        elif cd == UP:
            next_steps = [right, left, up] if sdr < 10 else [right, left]
        elif cd == RIGHT:
            next_steps = [up, down, right] if sdr < 10 else [up, down]
        elif cd == DOWN:
            next_steps = [right, left, down] if sdr < 10 else [right, left]
        elif cd == LEFT:
            next_steps = [up, down, left] if sdr < 10 else [up, down]

    for nr, nc in next_steps:
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            continue

        dir = UP if (nr, nc) == up else RIGHT if (nr, nc) == right else DOWN if (nr, nc) == down else LEFT
        same_dir_steps = 1 if dir != cd else sdr + 1
        
        if (r, c, dir, same_dir_steps) in seen:
            continue
        seen.add((r, c, dir, same_dir_steps))

        heat_loss = hl + int(grid[nr][nc])
        heappush(heap2, (heat_loss, nr, nc, dir, same_dir_steps))