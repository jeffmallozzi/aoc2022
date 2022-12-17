from itertools import pairwise
input_file = "input-15.txt"


def find_gap(row):
    row.sort(key=lambda x: x[0])
    minx, maxx = row[0]
    if minx > 0:
        return 0

    for pair in row[1:]:
        if pair[0] > (maxx + 1):
            return maxx + 1
        maxx = max([maxx, pair[1]])
    
    return None
   

def main():
    # Read file and parse data
    with open(input_file, "r") as f:
        sensors = [
            {
                location.split()[0].lower() : (int(location.split()[-2].strip("x=,")), 
                                        int(location.split()[-1].strip("y=,")))
                for location in line.strip().split(": closest ")
            }
            for line in f
        ]
    # Calculate the manhatten distance for each sensor to nearest beacon
    for sensor in sensors:
        sensor["mdistance"] = abs(
            sensor["sensor"][0] - sensor["beacon"][0]
        ) + abs(
            sensor["sensor"][1] - sensor["beacon"][1]
        )

    # Set the target row
    y = 2000000

    x_in_row_y = set()

    for sensor in sensors:
        rows_away = abs(y - sensor["sensor"][1])
        if rows_away <= sensor["mdistance"]:
            x_reserve = sensor["mdistance"] - rows_away
            for x in range(
                sensor["sensor"][0] - x_reserve, 
                sensor["sensor"][0] + x_reserve + 1
            ):
                x_in_row_y.add(x)
    
    for sensor in sensors:
        if sensor["beacon"][1] == y:
            x_in_row_y.discard(sensor["beacon"][0])
    

    print("Part 1: ", len(x_in_row_y))

    for y in range(0, 4000000 + 1):
        x_in_row_y = []
        for sensor in sensors:
            rows_away = abs(y - sensor["sensor"][1])
            if rows_away <= sensor["mdistance"]:
                x_reserve = sensor["mdistance"] - rows_away
                x_in_row_y.append((
                    max([0, sensor["sensor"][0] - x_reserve]), 
                    min([4000000, sensor["sensor"][0] + x_reserve])
                ))
        gap = find_gap(x_in_row_y)
        if gap is not None:
            print("Part 2: ", (gap * 4000000) + y)
            break


if __name__ == "__main__":
    main()