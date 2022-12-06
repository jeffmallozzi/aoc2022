input_file = "input-06.txt"

def unique_sequence(buffer, number):
    for i in range(number, len(buffer) + 1):
        if len(set(buffer[i-number:i])) == number:
            return i


def main():
    with open(input_file, "r") as f:
        buffer = f.readline().strip()

    print("Part 1: ", unique_sequence(buffer, 4))
    print("Part 2: ", unique_sequence(buffer, 14))


if __name__ == "__main__":
    main()