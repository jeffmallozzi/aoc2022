input_file = "input-02.txt"


def main():
    points_for_choice = {
        "X" : 0,
        "Y" : 3,
        "Z" : 6
    }

    points_for_match = {
        ("A","X") : 3,
        ("A", "Y") : 1,
        ("A", "Z") : 2,
        ("B","X") : 1,
        ("B", "Y") : 2,
        ("B", "Z") : 3,
        ("C","X") : 2,
        ("C", "Y") : 3,
        ("C", "Z") : 1
    }

    total_score = 0

    with open(input_file, "r") as f:
        for line in f.readlines():
            opp, me = line.strip().split()
            total_score += (points_for_choice[me] + points_for_match[(opp,me)])

    print(total_score)



if __name__ == "__main__":
    main()