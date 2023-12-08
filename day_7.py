
lines = open("day_7.txt").read().splitlines()


hands = []
for l in lines:
    hands.append(tuple(t for t in l.split(" ")))
hands = [(list(h), int(r)) for h, r in hands]

def stat(h):
    return dict((c, h.count(c)) for c in h)

def single_card_value(h, V):
    return tuple(V.index(c) for c in h)

def value_tuple(n, h, V):
    return tuple([n] + list(single_card_value(h, V)))

def star1():
    def value(h, V):
        s = stat(h)
        s = list(s.values())
        if 5 in s:
            return value_tuple(7, h, V)
        if 4 in s:
            return value_tuple(6, h, V)
        if 3 in s and 2 in s:
            return value_tuple(5, h, V)
        if 3 in s:
            return value_tuple(4, h, V)
        if s.count(2) == 2:
            return value_tuple(3, h, V)
        if 2 in s:
            return value_tuple(2, h, V)
        return value_tuple(1, h, V)
    
    V = list("AKQJT98765432")
    V.reverse()
    values = [(h, r, value(h,V)) for h, r in hands]
    values = sorted(values, key=lambda t: t[2], reverse=True)
    values = [(h,r,(len(values)-i)*r) for i, (h, r, v) in enumerate(values)]
    return sum(v for _, _, v in values)

def star2():
    def value(h: list[str], V):
        s = stat(h)
        js = s.get("J", 0)
        if js:
            del s["J"]
        s = list(s.values())
        if (5 in s) or (4 in s and js == 1) or (3 in s and js == 2) or (2 in s and js == 3) or (1 in s and js == 4) or (js == 5):
            return value_tuple(7, h, V)
        if (4 in s) or (3 in s and js == 1) or (2 in s and js == 2) or (1 in s and js == 3):
            return value_tuple(6, h, V)
        if (3 in s and 2 in s) or (3 in s and 1 in s and js == 1) or (s.count(2) == 2 and js == 1):
            return value_tuple(5, h, V)
        if (3 in s) or (2 in s and js == 1) or (1 in s and js == 2):
            return value_tuple(4, h, V)
        if (s.count(2) == 2) or (2 in s and 1 in s and js == 1):
            return value_tuple(3, h, V)
        if (2 in s) or (1 in s and js == 1):
            return value_tuple(2, h, V)
        return value_tuple(1, h, V)
    
    V = list("AKQT98765432J")
    V.reverse()
    values = [(h, r, value(h,V)) for h, r in hands]
    values = sorted(values, key=lambda t: t[2], reverse=True)
    values = [(h,r,(len(values)-i)*r) for i, (h, r, v) in enumerate(values)]
    return sum(v for _, _, v in values)

print("star1", star1()) 
print("star2", star2())