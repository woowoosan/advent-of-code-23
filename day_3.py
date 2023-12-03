import re

lines = open("day_3.txt").read().splitlines()
w = len(lines[0])
h = len(lines)

def lookup(x, y, default=".") -> str:
    return lines[y][x] if x >= 0 and x < w and y > 0 and y < h else default

nums = []
for y, l in enumerate(lines):
    for m in re.finditer(r"[0-9]+", l):
        nums.append((int(m.group()), y, m.span()))

part_nums = []
gears = {}
for num, y, span in nums:
    is_partnum = False
    gear = None
    for x in range(*span):
        around = [
            (x-1, y-1),
            (x  , y-1),
            (x+1, y-1),
            (x-1, y+1),
            (x  , y+1),
            (x+1, y+1),
            (x-1, y  ),
            (x+1, y  ),
        ]
        around = [(xy, lookup(xy[0], xy[1])) for xy in around]
        is_partnum = is_partnum or any(c != "." and not c.isdigit() for _, c in around)
        gear = next((xy for xy, c in around if c == "*"), gear)
    if is_partnum:
        part_nums.append(num)
    if gear:
        arr = gears.get(gear, [])
        arr.append(num)
        gears[gear] = arr

print("star1", sum(part_nums))  
print("star2", sum(nums[0] * nums[1] for g, nums in gears.items() if len(nums) == 2))