input_file = "input-04.txt"

def main():
    count = 0

    with open(input_file, "r") as f:
        for line in f:
            elf1, elf2 = line.strip().split(",")
            start1, stop1 = [int(num) for num in elf1.split("-")]
            start2, stop2 = [int(num) for num in elf2.split("-")]

            if start1 == start2:
                count += 1
            elif start1 < start2:
                if stop2 <= stop1:
                    count += 1
            else:
                if stop2 >= stop1:
                    count += 1

    print("Part 1: ", count)


if __name__ == "__main__":
    main()