
def do(lines: list[str]):
    games = {}
    for l in lines:
        id = l.split(":")[0].split(" ")[1]
        s = []
        for sets in l.split(":")[1].split("; "):
            cubes = (0, 0, 0)
            for c in sets.split(", "):
                num, color = c.strip().split(" ")
                num = int(num)
                if color == "red":
                    cubes = (cubes[0] + num, cubes[1], cubes[2])
                if color == "green":
                    cubes = (cubes[0], cubes[1] + num, cubes[2])
                if color == "blue":
                    cubes = (cubes[0], cubes[1], cubes[2] + num)
            s.append(cubes)

        games[id] = s

    possible = [int(id) for id, set in games.items() if all(cubes[0] <= 12 and cubes[1] <= 13 and cubes[2] <= 14 for cubes in set)]
    print("star1", sum(possible))

    powers = []
    for _, sets in games.items():
        maxr = 0
        maxg = 0
        maxb = 0
        for s in sets:
            maxr = max(maxr, s[0])
            maxg = max(maxg, s[1])
            maxb = max(maxb, s[2])
        powers.append(maxr * maxg * maxb)
    print("star2", sum(powers))


do(open("day_2.txt").read().splitlines())