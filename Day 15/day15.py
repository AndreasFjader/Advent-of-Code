def hashmap(input, only_label):
    cv = 0
    for c in input:
        if only_label and (c == '-' or c == '='):
            return cv
        cv += ord(c)
        cv *= 17
        cv %= 256
    return cv

steps = open('in.txt').read().split(',')
print("Part 1:", sum([sum(hashmap(step, False) for step in steps)]))

# Part 2
boxes = {}
for step in steps:
    box_nr = hashmap(step, True) + 1
    if box_nr not in boxes:
        boxes[box_nr] = []
    
    op = step[-2]
    if op != '=':
        op = step[-1]

    label, fl = step.split(op)
    lens = (label, fl)
    
    if op == '-':
        if label in [b[0] for b in boxes[box_nr]]:
            index = next((i for i, (l, _) in enumerate(boxes[box_nr]) if l == label), None)
            boxes[box_nr].pop(index)
    
    elif op == '=':
        if label not in [l for l, _ in boxes[box_nr]]:
            boxes[box_nr].append(lens)
        else:
            index = next((i for i, (l, _) in enumerate(boxes[box_nr]) if l == label), None)
            boxes[box_nr][index] = lens

t = 0
for box, lenses in boxes.items():
    for i, (_, f) in enumerate(lenses):
        t += (box * (i + 1) * int(f))
print("Part 2:", t)