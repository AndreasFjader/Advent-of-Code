import copy
from collections import deque

_workflows, _parts = open('in.txt').read().split('\n\n')

workflows = {}
for f in _workflows.splitlines():
    n, wf = f.split('{')
    workflows[n] = [x.split(':') for x in wf[:-1].split(',')]

parts = {}
for i, p in enumerate(_parts.splitlines()):
    x, m, a, sym = p[1:-1].split(',')
    parts[i] = {
        "x": int(x.split('=')[1]),
        "m": int(m.split('=')[1]),
        "a": int(a.split('=')[1]),
        "s": int(sym.split('=')[1])
    }
    
    
def evaluate(part, flow):
    for condition in flow:
        if len(condition) == 1:
            if condition[0] == 'R':
                return False
            elif condition[0] == 'A':
                return True
            return evaluate(part, workflows[condition[0]])
        else:
            c, n = condition
            ch = 'x' if 'x' in c else 'm' if 'm' in c else 'a' if 'a' in c else 's'
            fulfilled = eval(c.replace(ch, str(part[ch])))
            
            if fulfilled:
                if n == 'A':
                    return True
                elif n == 'R':
                    return False
                return evaluate(part, workflows[n])
        

# Part 1
t = 0
for part in parts.values():
    if evaluate(part, workflows['in']):
        t += part['x'] + part['m'] + part['a'] + part['s']
        
print("Part 1:", t)

# Part 2
accepted_ranges = 0
queue = deque()

# List indexes for the ranges
start_ranges = {
    'x': [1, 4000],
    'm': [1, 4000],
    'a': [1, 4000],
    's': [1, 4000],
}
queue.append(['in', start_ranges])
seen = []

while queue:
    wfname, ranges = queue.popleft()    
    if wfname == 'A':
        accepted_ranges += (ranges['x'][1] - ranges['x'][0] + 1) * (ranges['m'][1] - ranges['m'][0] + 1) * (ranges['a'][1] - ranges['a'][0] + 1) * (ranges['s'][1] - ranges['s'][0] + 1)
        continue
    if wfname == 'R':
        continue
    
    for flow in workflows[wfname]:
        if len(flow) == 1:
            if flow == 'A':
                accepted_ranges += (ranges['x'][1] - ranges['x'][0] + 1) * (ranges['m'][1] - ranges['m'][0] + 1) * (ranges['a'][1] - ranges['a'][0] + 1) * (ranges['s'][1] - ranges['s'][0] + 1)
                continue
            if flow == 'R':
                continue
            
            queue.append([flow[0], ranges])
            continue
        
        # there is a condition.
        cond, nxt = flow
        true_ranges = copy.deepcopy(ranges)
        
        if '<' in cond:
            sym, num = cond.split('<')
            num = int(num)
            if true_ranges[sym][1] >= num:
                true_ranges[sym][1] = num - 1
            if ranges[sym][0] < num:
                ranges[sym][0] = num
            queue.append([nxt, true_ranges])
            
        elif '>' in cond:
            sym, num = cond.split('>')
            num = int(num)
            if true_ranges[sym][0] <= num:
                true_ranges[sym][0] = num + 1
            if ranges[sym][1] > num:
                ranges[sym][1] = num
            queue.append([nxt, true_ranges])

print("Part 2:", accepted_ranges)