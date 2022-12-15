from itertools import zip_longest as zl 
from ast import literal_eval
from functools import cmp_to_key

input_file = "input-13.txt"


def compare(left, right):
    # base case, left or right ran out of items
    if left is None:
        return -1
    if right is None:
        return 1

    # base case, both are integers
    if type(left) is int and type(right) is int:
        #print("Comparing atoms")
        if left < right:
            return -1
        if right < left:
            return 1
        return 0

    # if one is an int, trun it into a list
    if type(left) is not list:
        left = [left]
    if type(right) is not list:
        right = [right]

    for l,r in zl(left, right, fillvalue=None):
        comp = compare(l,r)
        if comp == 0:
            continue
        return comp
  
    return 0


def main():
    with open(input_file, "r") as f:
        lists = {index: [literal_eval(x) for x in pair.strip().split("\n")]
        for index, pair in enumerate(f.read().split("\n\n"),start=1)}

    print("Part 1: ", sum(
        [
            index for index, (left, right) in lists.items()
            if compare(left, right) == -1
        ]
    ))

    code_list = []
    for left, right in lists.values():
        code_list.append(left)
        code_list.append(right)

    code_list.append([[2]])
    code_list.append([[6]])

    code_list.sort(key=cmp_to_key(compare))

    print("Part 2: ", (code_list.index([[2]])+1) * (code_list.index([[6]])+1))


if __name__ == "__main__":
    main()