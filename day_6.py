
lines = open("day_6.txt").read().splitlines()
ts = [int(t.strip()) for t in lines[0].replace("Time:", "").split(" ") if t != ""]
ds = [int(t.strip()) for t in lines[1].replace("Distance:", "").split(" ") if t != ""]

def star1():
    wins = []
    for i in range(0, len(ts)):
        t = ts[i]
        d = ds[i]
        poss = (1 for hold in range(0, t) if hold * (t - hold) > d)
        wins.append(sum(poss))

    score = 1
    for w in wins:
        score *= w

    return score

def star2():
    t = int("".join(str(t) for t in ts))
    d = int("".join(str(d) for d in ds))
    
    def test(r):
        for n in r:
            if not n * (t-n) > d:
                return n

    upper = test(range(int(t/2), t)) - 1
    lower = test(range(int(t/2), 0, -1)) + 1
    return  upper - lower + 1

print("star1", star1())
print("star2", star2())
