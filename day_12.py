from string import ascii_lowercase as al
input_file = "input-12.txt"


def get_neighbors(loc, height_map):
    column, row = loc
    loc_height = height_map[row][column]
    neighbors = [
        (column - 1, row),
        (column + 1, row),
        (column, row -1),
        (column, row + 1)
    ]

    resp = []

    for ncolumn, nrow in neighbors:
        if ncolumn >= 0 and nrow >= 0:
            try:
                if height_map[nrow][ncolumn] >= (loc_height - 1):
                    resp.append((ncolumn, nrow))
            except IndexError:
                pass

    return resp


def populate(loc, step, steps_away, height_map):
    for neighbor in get_neighbors(loc, height_map):
        if neighbor not in steps_away:
            steps_away[neighbor] = step


def main():
    with open(input_file, "r") as f:
        height_map = [
                        [al.index(letter) if letter.islower() else letter
                        for letter in line.strip()] 
                     for line in f]

    for y, line in enumerate(height_map):
        for x, letter in enumerate(line):
            if letter == "S":
                start = (x,y)
                height_map[y][x] = 0
            elif letter == "E":
                end = (x,y)
                height_map[y][x] = 25

    steps_away = {end: 0}
    step = 1
    while start not in steps_away:
        
        # print(step, steps_away)
        for loc in [
            loc for loc in steps_away
            if steps_away[loc] == step - 1
        ]:
            populate(loc, step, steps_away, height_map)
        step += 1

    print("Part 1: ", steps_away[start])

    starts = []
    for y, line in enumerate(height_map):
        for x, height in enumerate(line):
            if height == 0:
                starts.append((x,y))
    
    steps_away2 = {end: 0}

    step = 1
    growing = True
    while growing:
        start_size = len(steps_away2)

        # print(step, steps_away2)
        for loc in [
            loc for loc in steps_away2
            if steps_away2[loc] == step - 1
        ]:
            populate(loc, step, steps_away2, height_map)
        step += 1

        if len(steps_away2) == start_size:
            growing = False

    print("Part 2: ", min(
        [
            steps_away2[start]
            for start in starts
            if start in steps_away2
        ]
    ))




if __name__ == "__main__":
    main()
