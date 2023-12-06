
lines = open("day_5.txt").read().splitlines()

def get_seeds1():
    return [int(t) for t in lines[0].split(": ")[1].split(" ")]

def get_seeds2():
    toks = [int(t) for t in lines[0].split(": ")[1].split(" ")]
    starts = toks[0::2]
    lens = toks[1::2]
    seeds = [range(start, start + lens[i]) for i, start in enumerate(starts)]
    return seeds

def get_maps():
    maps = {}
    key = None
    arr = None
    for l in lines[2:]:
        if l == "":
            key = None
            arr = None
        elif "map" in l:
            a, b = l.replace(" map:", "").split("-to-")
            key = (a, b)
            arr = []
            maps[key] = arr
        else:
            tok = tuple(int(s) for s in l.split(" "))
            arr.append(((tok[1], tok[1] + tok[2]), (tok[0], tok[0] + tok[2])))
    return maps

def conv(v, ranges):
    for src, dst in ranges:
        if v in range(*src):
            return  dst[0] + (v - src[0])
    return  v

def convr(v, ranges):
    for src, dst in ranges:
        if v in range(*dst):
            return  src[0] + (v - dst[0])
    return  v

def star1(seeds, maps):
    i = "seed"
    vals = seeds
    while True:
        o = next((b for a, b in maps.keys() if a == i), None)
        if o is None:
            break
        vals = [conv(v, maps[(i, o)]) for v in vals]
        i = o
    return min(vals)

def star2(seeds, maps):
    m = None
    l = 0
    step = 10000000
    while True:
        vals = list(range(l, l+step))
        o = "location"
        while True:
            i = next((a for a, b in maps.keys() if b == o), None)
            if i is None:
                break
            vals = [convr(v, maps[(i, o)]) for v in vals]
            o = i
        m = next((l + i for i, v in enumerate(vals) if any(v in r for r in seeds)), None)
        if m:
            break
        l += step
        print(l, m)
    return m

maps = get_maps()
print("star1", star1(get_seeds1(), maps))
print("star2", star2(get_seeds2(), maps))
