from math import prod
input_file = "input-11.txt"

class Monkey():
    def __init__(self, operation, test, true_monkey, false_monkey, monkey_list, items=None) -> None:
        self.items = items if items else []
        self.test = test
        self.operation = operation
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect_count = 0
        self.monkey_list = monkey_list

    def throw_items(self):
        while self.items:
            item = self.items.pop(0)
            item = self.operation(item)  // 3
            if item%self.test == 0:
                self.monkey_list[self.true_monkey].catch(item)
            else:
                self.monkey_list[self.false_monkey].catch(item)
            self.inspect_count += 1

    def catch(self, item):
        self.items.append(item % prod([monkey.test for monkey in self.monkey_list]))

    def items_inspected(self):
        return self.inspect_count


def main():
    monkey_list = []

    with open(input_file, "r") as f:
        while f:
            monkey = f.readline().strip().split()
            if not monkey:
                break
            items = f.readline().strip().split()
            operation = f.readline().strip().split()
            test = f.readline().strip().split()
            true_monkey = f.readline().strip().split()
            false_monkey = f.readline().strip().split()

            items = [int(item.strip(",")) for item in items[2:]]
            operation = "lambda old: " + " ".join(operation[3:])
            operation = eval(operation)
            test = int(test[-1])
            true_monkey = int(true_monkey[-1])
            false_monkey = int(false_monkey[-1])

            monkey_list.append(
                Monkey(operation, test, true_monkey, false_monkey, monkey_list, items)
            )

            f.readline()

    
    for _ in range(20):
        for monkey in monkey_list:
            monkey.throw_items()

    print("Part 2: ", prod(sorted(
        [monkey.items_inspected() for monkey in monkey_list], reverse=True
    )[:2]))



if __name__ == "__main__":
    main()