from itertools import groupby
from itertools import cycle
from itertools import pairwise

input_file = "input-17.txt"


class Space():
    def __init__(self, width, wind) -> None:
        self.width = width
        self.rock_count = 0
        self.height = 0
        self.occupied = set()
        self.wind_length = len(wind)
        self.wind = cycle(enumerate(wind))
        self.wind_index = 0

    def get_height(self):
        return self.height


    def drop_rocks(self, num):
        repeats = {rock: [] for rock in range(len(Rock.rock_types))}
        for i in range(num):
            if all([
                i > 0,
                self.wind_index == 0
            ]):
                repeats[i%len(Rock.rock_types)].append((i,self.height))
                #print(f"Repeat at rock {i}")
            rock = Rock.rock_types[i % len(Rock.rock_types)](self)
            falling = True
            while falling:
                self.wind_index, direction = next(self.wind)
                rock.blow(direction)
                falling = rock.fall()

            for unit in rock.mass:
                self.occupied.add(unit)

            if rock.get_top() >= self.height:
                self.height = rock.get_top() +1
        
        return repeats


class Rock():
    rock_types = []

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls.rock_types.append(cls)

    def __init__(self, space) -> None:
        self.space = space
        self.mass = []

    def get_top(self):
        return max([unit[1] for unit in self.mass])

    def fall(self):
        temp_mass = [
            (x, y - 1)
            for x,y in self.mass
        ]

        for unit in temp_mass:
            if unit in self.space.occupied or unit[1] < 0:
                return False

        self.mass = temp_mass
        return True            

    def blow(self, wind):

        match wind:
            case "<":
                diff = -1
            case ">":
                diff = 1

        temp_mass = [
            (x + diff, y)
            for x,y in self.mass
        ]

        for unit in temp_mass:
            if unit[0] < 0 or unit[0] >= self.space.width:
                break
            if unit in self.space.occupied:
                break
        else:
            self.mass = temp_mass

class HBar(Rock):
    def __init__(self, space) -> None:
        super().__init__(space)
        self.mass = [
            (2, space.get_height() + 3),
            (3, space.get_height() + 3),
            (4, space.get_height() + 3),
            (5, space.get_height() + 3)
        ]

class Cross(Rock):
    def __init__(self, space) -> None:
        super().__init__(space)
        self.mass = [
            (3, space.get_height() + 3),
            (2, space.get_height() + 4),
            (3, space.get_height() + 4),
            (4, space.get_height() + 4),
            (3, space.get_height() + 5)
        ]

class Ell(Rock):
    def __init__(self, space) -> None:
        super().__init__(space)
        self.mass = [
            (2, space.get_height() + 3),
            (3, space.get_height() + 3),
            (4, space.get_height() + 3),
            (4, space.get_height() + 4),
            (4, space.get_height() + 5)
        ]

class VBar(Rock):
    def __init__(self, space) -> None:
        super().__init__(space)
        self.mass = [
            (2, space.get_height() + 3),
            (2, space.get_height() + 4),
            (2, space.get_height() + 5),
            (2, space.get_height() + 6),
        ]

class Square(Rock):
    def __init__(self, space) -> None:
        super().__init__(space)
        self.mass = [
            (2, space.get_height() + 3),
            (3, space.get_height() + 3),
            (2, space.get_height() + 4),
            (3, space.get_height() + 4),
        ]

def encode_space(space):
    return [
        sum([2**x for x,y in group])
        for k, group in groupby(sorted(space, key=lambda x: x[1]), key=lambda x: x[1])
    ]

def func(n):
    for i in range(6,-1,-1):
        q,r = divmod(n, 2**i)
        n = r
        if q:
            yield i

def decode_space(space):
    return [
        (x,y)
        for y, n in enumerate(space)
        for x in func(n)
    ]


def test_repeat(space_1, space_2):
    coded_1 = encode_space(space_1.occupied)
    coded_2 = encode_space(space_2.occupied)

    for x in range(1,10):
        test = coded_1[x:-x]
        for y in range(len(test), len(coded_2)-len(test)):
            if test == coded_2[y:y+len(test)]:
                print("Repeat found", x, y)
                return True, x

   
    return False, None


def find_period(space):
    coded = encode_space(space.occupied)


        

def main():
    with open(input_file, "r") as f:
        wind = f.read().strip()

    my_space = Space(7, wind)
    my_space.drop_rocks(2022)
    print("Part 1: ", my_space.height)


    my_space = Space(7, wind)
    repeats = my_space.drop_rocks(100000)[0]
    repeat_period = repeats[1][0] - repeats[0][0]
    initial_buffer = repeats[0][0] - repeat_period
    cycles, remainder = divmod((1000000000000 - initial_buffer), repeat_period)
    period_height = repeats[1][1] - repeats[0][1]
    buffer_height = repeats[0][1] - period_height


    print(repeat_period, initial_buffer, cycles, remainder, buffer_height, period_height)

    my_space = Space(7, wind)
    my_space.drop_rocks(initial_buffer + repeat_period + remainder)
    final_height = my_space.height - (buffer_height + period_height)
    print(final_height)
    
    print("Part 2: ", buffer_height + (period_height * cycles) + final_height)






if __name__ == "__main__":
    main()