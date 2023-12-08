_h = [x.split() for x in open('in.txt').readlines()]
hands = [tuple((h[0], int(h[1]))) for h in _h]

def num_to_val(item):
    # for part 1, J == 11, part 2 J == 1
    v = { 'T': 10, 'J': 1, 'Q': 11, 'K': 12, 'A': 13 }
    t = []
    for i in item:
        if i.isdigit():
            t.append(int(i))
        else:
            t.append(v[i])
    return tuple(t)

def flatten_list(l: list) -> list:
    f = []
    for r in l:
        f.extend(r)
    return f

# def insert_jokers(d: list, jokers: int):
#     deck = d.copy()
#     if jokers == 5:
#         return [5]
    
#     for _ in range(jokers):
#         if deck == [1, 1, 1, 1, 1]: # High card
#             deck = [1, 1, 1, 2]
#         elif deck == [1, 1, 1, 2]: # One pair
#             deck = [1, 1, 3]
#         elif deck == [1, 2, 2]: # Two pairs
#             deck = [2, 3]
#         elif deck == [1, 1, 3]: # Three of a kind
#             deck = [1, 4]
#         elif deck == [2, 3]: #Full house
#             deck = [1, 4]
#         elif deck == [1, 4]: #Four of a kind
#             deck = [5]
    
#     return deck

def insert_jokers(d: list, jokers: int):  
    if jokers == 1:
        if d == [1, 1, 1, 1, 1]:
            return [1, 1, 1, 2]
        elif d  == [1, 1, 1, 2]:
            return [1, 1, 3]
        elif d == [1, 1, 3]:
            return [1, 4]
        elif d == [1, 2, 2]:
            return [2, 3]
        elif d == [1, 4]:
            return [5]
    elif jokers == 2:
        if d  == [1, 1, 1, 2]:
            return [1, 1, 3]
        elif d == [2, 3]:
            return [5]
        elif d == [1, 2, 2]:
            return [1, 4]
    elif jokers == 3:
        if d  == [1, 1, 3]:
            return [1, 4]
        elif d == [2, 3]:
            return [5]
    elif jokers == 4 or jokers == 5:
        return [5]

five = []
four = []
full = []
three = []
two = []
one = []
high = []

for h in hands:
    cards = num_to_val(h[0])
    cc = {}
    for c in list(cards):
        if not c in cc:
            cc[c] = 1
        else:
            cc[c] += 1
    
    # Categorize hand
    t = list(cc.values())
    t.sort()

    # Part 2, why so serious?
    jokers = 0
    if 1 in cc.keys():
        jokers = cc[1]
        
    if jokers > 0:
        t = insert_jokers(t, jokers)
    t.sort()
    # figure out the best possible deck based on number of jokers.    
    if t == [1, 1, 1, 1, 1]:
        high.append((cards, h[1]))
    elif t == [1, 1, 1, 2]:
        one.append((cards, h[1]))
    elif t == [1, 2, 2]:
        two.append((cards, h[1]))
    elif t == [1, 1, 3]:
        three.append((cards, h[1]))
    elif t == [2, 3]:
        full.append((cards, h[1]))
    elif t == [1, 4]:
        four.append((cards, h[1]))
    elif t == [5]:
        five.append((cards, h[1]))

a = [high, one, two, three, full, four, five]

for i, pair in enumerate(a):
    a[i] = sorted(pair, key=lambda x: x[0])
    
a = flatten_list(a)
total = 0
for i, hand in enumerate(a):
    total += hand[1] * (i + 1)

print("Part 2:", total)