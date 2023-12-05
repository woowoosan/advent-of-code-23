
lines = open("day_4.txt").read().splitlines()

def star1(lines):
    worth = []
    for l in lines:
        l = l.split(": ")[1]
        winning = l.split(" | ")[0].strip()
        winning = [int(t.strip()) for t in winning.split(" ") if t != ""]
        my = l.split(" | ")[1].strip()
        my = [int(t.strip()) for t in my.split(" ") if t != ""]
        exp = (sum(1 for c in my if c in winning) - 1)
        worth.append(0 if exp < 0 else 2 ** exp)
    return sum(worth)

def star2(lines: list[str]):
    cards = []
    for l in lines:
        l = l.split(": ")[1]
        winning = l.split(" | ")[0].strip()
        winning = [int(t.strip()) for t in winning.split(" ") if t != ""]
        my = l.split(" | ")[1].strip()
        my = [int(t.strip()) for t in my.split(" ") if t != ""]
        cards.append([(winning, my)])

    for i, cs in enumerate(cards):
        for my, winning in cs:
            wins = sum(1 for m in my if m in winning)
            for n in range(1, wins + 1):
                cards[i + n] += [cards[i+n][0]]

    return sum(1 for cs in cards for c in cs)


print("star1", star1(lines))
print("star2", star2(lines))