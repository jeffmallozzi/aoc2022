from string import ascii_lowercase, ascii_uppercase

input_file = "input-03.txt"


def bisect(word):
    return word[0:len(word)//2], word[len(word)//2:]


def main():
    priority = {
        letter : value 
        for letter, value in zip(ascii_lowercase+ascii_uppercase, range(1,53))
    }

    with open(input_file, "r") as f:
        print(
            sum(
                [priority[
                    set(
                        bisect(line.strip())[0]
                    ).intersection(set(bisect(line.strip())[1])).pop()
                ]
                for line in f.readlines()]
            )
            
        )
    
    

    


if __name__ == "__main__":
    main()