input_file = "input-05.txt"

def main():
    crates = {}
    input_lines = []

    with open(input_file, "r") as f:
        line = f.readline()
        while line.strip():
            if line[0] == "[":
                input_lines.append(line.strip())
            else:
                for x in line.split():
                    crates[int(x)] = []
            line = f.readline()

        print(crates)
        print(input_lines)

        for input_line in input_lines[::-1]:
            for index, crate in enumerate(input_line[1::4]):
                if crate.isalpha():
                    crates[index+1].append(crate)

        for move in f:
            _, count, _, start, _, finish = move.strip().split()
            for _ in range(int(count)):
                crates[int(finish)].append(crates[int(start)].pop(-1))


    for stack, crate in crates.items():
        print(f"{stack} : {crate[-1]}")

        


if __name__ == "__main__":
    main()