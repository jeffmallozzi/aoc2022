from itertools import pairwise

input_file = "input-14.txt"


def drop_sand(scan, abyss):
    sand = (500, 0)

    while sand[1] <= abyss:
        # Try to move down
        if (sand[0], sand[1] + 1) not in scan:
            sand = (sand[0], sand[1] + 1)
        # Try to move down and left
        elif (sand[0] -1, sand[1] + 1) not in scan:
            sand = (sand[0] -1, sand[1] + 1)
        # Try to move down and right
        elif (sand[0]+1, sand[1] + 1) not in scan:
            sand = (sand[0]+1, sand[1] + 1)
        # Sand has come to rest
        else:
            scan.add(sand)
            return True

    # Sand has fallen into the abyss
    return False


def drop_sand_floor(scan, floor):
    sand = (500, 0)

    while sand not in scan:
        # if sand has hit the floor
        if sand[1] == floor -1:
            scan.add(sand)
            return True
        
        # Try to move down
        if (sand[0], sand[1] + 1) not in scan:
            sand = (sand[0], sand[1] + 1)
        # Try to move down and left
        elif (sand[0] -1, sand[1] + 1) not in scan:
            sand = (sand[0] -1, sand[1] + 1)
        # Try to move down and right
        elif (sand[0]+1, sand[1] + 1) not in scan:
            sand = (sand[0]+1, sand[1] + 1)
        # Sand has come to rest
        else:
            scan.add(sand)
            return True

    # Sand has filled up to the top
    return False



def draw_path(a, b, scan):
    ax, ay = a
    bx, by = b

    if ax == bx:
        for y in range(
            min([ay, by]),
            max([ay, by]) + 1
        ):
            scan.add((ax, y))
    elif ay == by:
        for x in range(
            min([ax, bx]),
            max([ax, bx]) + 1
        ):
            scan.add((x, ay))

    return max([ay, by])



def main():
    with open(input_file, "r") as f:
        paths = [
            [
                tuple(int(x) for x in point.split(","))
                for point in line.strip().split(" -> ")
            ]
            for line in f
        ]

    scan = set()
    abyss = 0
    for path in paths:
        for a, b in pairwise(path):
            abyss = max([abyss, draw_path(a, b, scan)])

    sand_count = 0
    while drop_sand(scan, abyss):
        sand_count += 1

    print("Part 1: ", sand_count)

    while drop_sand_floor(scan, abyss + 2):
        sand_count +=1

    print("Part 2: ", sand_count)



if __name__ == "__main__":
    main()