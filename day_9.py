
lines = open("day_9.txt").read().splitlines()
lines = [[int(t) for t in l.split(" ") if t != ""] for l in lines]

def derive(seq):
    diffs = []
    for i in range(0, len(seq) - 1):
        a = seq[i]
        b = seq[i+1]
        diffs.append(b - a)
    if all(n == diffs[0] for n in diffs):
        return diffs[0]
    else:
        return diffs[-1] + derive(diffs)

def derive_r(seq):
    diffs = []
    for i in range(0, len(seq) - 1):
        a = seq[i]
        b = seq[i+1]
        diffs.append(b - a)
    if all(n == diffs[0] for n in diffs):
        return diffs[0]
    else:
        return diffs[0] - derive_r(diffs)

vals = [l[-1] + derive(l) for l in lines]
vals_r = [l[0] - derive_r(l) for l in lines]


print("star1", sum(vals))  
print("star2", sum(vals_r))