input_file = "input-06.txt"

def main():
    with open(input_file, "r") as f:
        buffer = f.readline().strip()

    for i in range(4,len(buffer)+1):
        if len(set(buffer[i-4:i])) == 4:
            print("Part 1: ", i)
            break

    for i in range(14,len(buffer)+1):
        if len(set(buffer[i-14:i])) == 14:
            print("Part 2: ", i)
            break


if __name__ == "__main__":
    main()