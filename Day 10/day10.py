def get_next_possible_step(r, c, t):
    up = "|F7"
    down = "|JL"
    left = "-FL"
    right = "-7J"
    steps = []
    if t == 'S':
        steps.extend([(r + 1, c, tp) for tp in down])
        steps.extend([(r - 1, c, tp) for tp in up])
        steps.extend([(r, c + 1, tp) for tp in right])
        steps.extend([(r, c - 1, tp) for tp in left])
        return steps
    if t == '|':
        steps.extend([(r + 1, c, tp) for tp in down])
        steps.extend([(r - 1, c, tp) for tp in up])
        return steps
    if t == '-':
        steps.extend([(r, c + 1, tp) for tp in right])
        steps.extend([(r, c - 1, tp) for tp in left])
        return steps
    if t == 'L':
        steps.extend([(r, c + 1, tp) for tp in right])
        steps.extend([(r - 1, c, tp) for tp in up])
        return steps
    if t == 'J':
        steps.extend([(r, c - 1, tp) for tp in left])
        steps.extend([(r - 1, c, tp) for tp in up])
        return steps
    if t == '7':
        steps.extend([(r + 1, c, tp) for tp in down])
        steps.extend([(r, c - 1, tp) for tp in left])
        return steps
    if t == 'F':
        steps.extend([(r + 1, c, tp) for tp in down])
        steps.extend([(r, c + 1, tp) for tp in right])
        return steps
    
    raise Exception('Unaccepted symbol.')
    
    
    
pipes = open('in.txt').read().splitlines()
seen = set()
m = set()
n = None
for r, row in enumerate(pipes):
    for c, col in enumerate(row):
        s = pipes[r][c]
        if s == 'S':
            n = (r, c, s)
        elif s in "|-FJL7S":
            m.add((r, c, s))
        
# Part 1
steps = 0
while n:
    steps += 1
    seen.add(n)
    (r, c, t) = n
    for nr, nc, nt in get_next_possible_step(r, c, t):
        if (nr, nc, nt) in m and (nr, nc, nt) not in seen:
            n = (nr, nc, nt)
            break
    else:
        n = None
print("Part 1:", steps // 2)

# Part 2
