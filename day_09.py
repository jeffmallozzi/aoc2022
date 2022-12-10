input_file = "input-09.txt"

class LongRope():
    def __init__(self, start=(0,0), length=10) -> None:
        self.position = [start for i in range(length)]
        self.tail_history = [self.position[-1]]

    def move(self, direction, steps):
        for _ in range(steps):
            match direction:
                case "L":
                    self.position[0] = (self.position[0][0] - 1, self.position[0][1])
                case "R":
                    self.position[0] = (self.position[0][0] + 1, self.position[0][1])
                case "U":
                    self.position[0] = (self.position[0][0], self.position[0][1] + 1)
                case "D":
                    self.position[0] = (self.position[0][0], self.position[0][1] - 1)
            for knot in range(1,len(self.position)):
                self._move_knot(knot)
            self.tail_history.append(self.position[-1])

    def _move_knot(self, knot):
        head, tail = self.position[knot-1], self.position[knot]
        if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
            return

        # Knots are in the same column
        if head[0] == tail[0]:
            x = tail[0]
            if head[1] - tail[1] > 1:
                y = tail[1] + 1
            elif head[1] - tail[1] < -1:
                y = tail[1] - 1

        # knots are in the same row
        elif head[1] == tail[1]:
            y = tail[1]
            if head[0] - tail[0] > 1:
                x = tail[0] + 1
            elif head[0] - tail[0] < -1:
                x = tail[0] - 1

        # knots are not in the same column or row
        else:
            if head[0] > tail[0]:
                x = tail[0] + 1
            else:
                x = tail[0] - 1

            if head[1] > tail[1]:
                y = tail[1] + 1
            else:
                y = tail[1] - 1

        self.position[knot] = (x,y)
            
    def get_tail_history(self):
        return self.tail_history




def main():
    rope = LongRope(length=2)

    with open(input_file, "r") as f:
        for line in f:
            direction, distance = line.strip().split()
            rope.move(direction, int(distance))

    print("Part 1: ", len(set(rope.get_tail_history())))

    rope2 = LongRope(length=10)
    with open(input_file, "r") as f:
        for line in f:
            direction, distance = line.strip().split()
            rope2.move(direction, int(distance))

    print("Part 2: ", len(set(rope2.get_tail_history())))


if __name__ == "__main__":
    main()