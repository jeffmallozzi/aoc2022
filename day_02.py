input_file = "input-02.txt"


def main():
    points_for_choice = {
        "X" : 1,
        "Y" : 2,
        "Z" : 3
    }

    points_for_match = {
        ("A","X") : 3,
        ("A", "Y") : 6,
        ("A", "Z") : 0,
        ("B","X") : 0,
        ("B", "Y") : 3,
        ("B", "Z") : 6,
        ("C","X") : 6,
        ("C", "Y") : 0,
        ("C", "Z") : 3
    }

    total_score = 0

    with open(input_file, "r") as f:
        for line in f.readlines():
            opp, me = line.strip().split()
            total_score += (points_for_choice[me] + points_for_match[(opp,me)])

    print(total_score)



if __name__ == "__main__":
    main()