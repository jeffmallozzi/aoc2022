input_file = "input-07.txt"

class folder():
    def __init__(self, name, parent=None) -> None:
        self.files = {}
        self.folders = {}
        self.parent = parent
        self.name = name

    def mkdir(self, name):
        if name not in self.folders:
            self.folders[name] = folder(name, self)

    def cd(self, name):
        if name == "..":
            return self.parent
        return self.folders.get(name, self.mkdir(name))

    def tree_walk(self):
        for fold in self.folders:
            for sub in self.folders.get(fold).tree_walk():
                yield sub
            #yield self.folders.get(fold)
        yield self

    def add_file(self, name, size):
        self.files[name] = size

    def get_size(self):
        return sum(self.files.values()) + sum([fold.get_size() for fold in self.folders.values()])


def main():
    root = folder("/")
    cwd = root

    with open(input_file, "r") as f:
        f.readline()
        for line in f:
            line = line.strip().split()
            if line[0] == "dir":
                cwd.mkdir(line[1])
            elif line[0].isnumeric():
                cwd.add_file(line[1], int(line[0]))
            elif line[0] == "$" and line[1] == "cd":
                cwd = cwd.cd(line[2])

    total = 0
    for fold in root.tree_walk():
        if fold.get_size() <= 100000:
            total += fold.get_size()

    print("Part 1: ", total)

    disk_total = 70000000
    disk_used = root.get_size()
    disk_free = disk_total - disk_used
    space_needed = 30000000
    space_to_free = space_needed - disk_free

    print("Part 2:",
        min(
            [fold.get_size() for 
            fold in root.tree_walk() if
            fold.get_size() >= space_to_free]
        )
    )

if __name__ == "__main__":
    main()