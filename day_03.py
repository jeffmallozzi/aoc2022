from string import ascii_lowercase, ascii_uppercase
from itertools import islice

input_file = "input-03.txt"

def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch

def bisect(word):
    return word[0:len(word)//2], word[len(word)//2:]


def main():
    priority = {
        letter : value 
        for letter, value in zip(ascii_lowercase+ascii_uppercase, range(1,53))
    }

    with open(input_file, "r") as f:
        print(sum(
            [priority[set(lines[0].strip()).intersection(
                set(lines[1].strip())).intersection(set(lines[2].strip())).pop()]
            for lines in batched(f, 3)]   
            )        
        )
    
    

    


if __name__ == "__main__":
    main()