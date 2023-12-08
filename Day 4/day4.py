cards = open('in.txt').read().splitlines()

# Part 1
wn = []
decks = {}
for i, deck in enumerate(cards):
    winning, mine = deck.strip().split(':')[1].split(' | ')
    ws = set([int(x.strip()) for x in winning.split()])
    ms = set([int(x.strip()) for x in mine.split()])
    
    cc = len(ws & ms)
    decks[i + 1] = {
        "cc": cc,
        "instances": 1
    }

    if cc == 0:
        continue    
    
    points = 1
    for _ in range(1, cc):
        points *= 2
    wn.append(points)
print("Part 1:", sum(wn))

# Part 2
for id, deck in decks.items():
    i = deck["instances"]
    for c in range(id + 1, id + deck["cc"] + 1):
        if c in decks:
            decks[c]["instances"] += deck["instances"]

print("Part 2:", sum([v["instances"] for k, v in decks.items()]))
