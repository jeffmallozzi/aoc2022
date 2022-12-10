input_file = "input-08.txt"

def viewing_distance(tree, grid):
    x,y = tree
    tree_height = grid[y][x]

    up, down, left, right = 0,0,0,0

    above = y-1
    while above >= 0:
        if grid[above][x] < tree_height:
            up += 1
            above -= 1
        else:
            up += 1
            break

    below = y+1
    while below < len(grid):
        if grid[below][x] < tree_height:
            down += 1
            below += 1
        else:
            down +=1
            break


    to_left = x-1
    while to_left >= 0:
        if grid[y][to_left] < tree_height:
            left += 1
            to_left -= 1
        else:
            left += 1
            break


    to_right = x+1
    while to_right < len(grid[0]):
        if grid[y][to_right] < tree_height:
            right += 1
            to_right += 1
        else:
            right += 1
            break


    return up*down*left*right


def main():
    with open(input_file, "r") as f:
        grid = [
            [int(x) for x in line.strip()]
            for line in f
        ]

    visible_trees = set()

    for row_num, row in enumerate(grid):
        highest = -1
        for col_num, height in enumerate(row):
            if height > highest:
                visible_trees.add((row_num, col_num))
                highest = height

        highest = -1
        for col_num, height in zip(range(len(row)-1,-1,-1), row[::-1]):
            if height > highest:
                visible_trees.add((row_num, col_num))
                highest = height


    grid = [list(x) for x in zip(*grid)]

    for row_num, row in enumerate(grid):
        highest = -1
        for col_num, height in enumerate(row):
            if height > highest:
                visible_trees.add((col_num, row_num))
                highest = height

        highest = -1
        for col_num, height in zip(range(len(row)-1,-1,-1), row[::-1]):
            if height > highest:
                visible_trees.add((col_num, row_num))
                highest = height


    print("Part 1: ", len(visible_trees))

    print("Part 2: ", max(
        [viewing_distance((x,y), grid)
        for x in range(len(grid[0])) for y in range(len(grid))]
    ))







if __name__ == "__main__":
    main()