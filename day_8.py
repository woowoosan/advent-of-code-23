from math import lcm
lines = open("day_8.txt").read().splitlines()

LR = list(lines[0])
lines = lines[2:]
instr = {}
for l in lines:
    tok = [t.strip() for t in l.split(" = ")]
    instr[tok[0]] = tok[1].replace("(", "").replace(")", "").split(", ")

def star1(start, pred):
    x = start
    i = 0
    steps = 0
    while True:
        l = LR[i] == "L"
        i = (i + 1) % len(LR)
        x = instr[x][0] if l else instr[x][1]
        steps += 1
        if pred(x, i, steps):
            break
    return steps

def star2():
    x = list(k for k in instr.keys() if k.endswith("A"))
    cycles = [None] * len(x)
    for n, e in enumerate(x):
        def pred(x, i, steps):
            if x.endswith("Z") and i == 0:
                cycles[n] = steps
                return True
            return False
        star1(e, pred)

    return lcm(*cycles)

print("star1", star1("AAA", lambda x, _, __: x == "ZZZ"))  
print("star2", star2())