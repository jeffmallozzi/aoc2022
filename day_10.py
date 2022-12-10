input_file = "input-10.txt"


def main():
    cycles = [1]

    with open(input_file, "r") as f:
        for line in f:
            line = line.strip().split()
            if line[0] == "addx":
                cycles.extend([0, int(line[1])])
            elif line[0] == "noop":
                cycles.append(0)


    print(cycles)

    interesting_signals = [20, 60, 100, 140, 180, 220]
    
    print("Part 1: ", sum(
        [signal * sum(cycles[:signal])
        for signal in interesting_signals]
    ))

    screen = [
        "#" if ((i%40 - 1) <= sum(cycles[:i+1]) <= (i%40 + 1)) else "."
        for i in range(len(cycles))
    ]

    print("".join(screen[:40]))
    print("".join(screen[40:80]))
    print("".join(screen[80:120]))
    print("".join(screen[120:160]))
    print("".join(screen[160:200]))
    print("".join(screen[200:240]))



if __name__ == "__main__":
    main()