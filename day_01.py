def get_input(input_file = "input-01-a.txt"):
    calories = [[]]

    with open(input_file, "r") as file:
        for line in file.readlines():
            if line.strip():
                calories[-1].append(int(line.strip()))
            else:
                calories.append([])

    return calories

def main():
    calories = get_input()
    
    print(
        sum(
            sorted(
                [sum(x) for x in calories], reverse=True
            )[0:3]
        )           
    )


if __name__ == "__main__":
    main()