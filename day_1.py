digs = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def do(lines: list[str]):
    def s1(lines: list[str]):
        s = 0
        for l in lines:
            ds = []
            for c in l:
                if c.isdigit():
                    ds.append(int(c))
            s += int(f"{ds[0]}{ds[-1]}")
        print("star1", s)

    def s2(lines: list[str]):
        s = 0
        for l in lines:
            ds = []
            for i, c in enumerate(l):
                n = None
                for dig in digs.keys():
                    if l[i:].startswith(dig):
                        n = int(digs[dig])
                        break
                if n is None and c.isdigit():
                    n = int(c)
                if n is not None:
                    ds.append(n)
            s += int(f"{ds[0]}{ds[-1]}")
        print("star2", s)

    s1(lines)
    s2(lines)


do(open("day_1.txt").read().splitlines())