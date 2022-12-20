from itertools import product


input_file = "input-16.txt"


def pressure_release(path, time, valves):
    return sum(
        [
            valves[step.split()[-1]]["flow"] * (time - i)
            for i, step in enumerate(path.split("->"))
            if step.startswith("open")
        ]
    )


def pressure_release_2(paths, time, valves):
    return sum(
        [pressure_release(path, time, valves)
        for path in paths]
    )


def get_moves(path, valves):
    moves = []
    path = path.split("->")
    current_valve = path[-1].split()[-1]

    if valves[current_valve]["flow"] > 0 and f"open {current_valve}" not in path:
        moves.append(f"open {current_valve}")

    for valve in valves[current_valve]["tunnels"]:
        moves.append(f"move to {valve}")

    return moves


def get_moves_2(paths, valves):
    
    path_santa = paths[0]
    path_elephant = paths[1]

    # Prepend the opposite person's moves before calling get_moves
    # to ensure that there is no double opening of a valve
    moves_santa = get_moves(f"{path_elephant}->{path_santa}", valves)
    moves_elephant = get_moves(f"{path_santa}->{path_elephant}", valves)

    return (moves_santa, moves_elephant)



def build_paths(valves, move_limit, start_valve="AA", path=None):

    
    if path is None:
        path = start_valve
    
 
    if path.count("->") == move_limit:
        yield path
    else:
        for move in get_moves(path, valves):
            for p in build_paths(valves, move_limit, path=f"{path}->{move}"):
                yield p


def build_paths_2(valves, move_limit, start_valve="AA", paths=None):

    if paths is None:
        paths = (start_valve, start_valve)

    if paths[0].count("->") == move_limit:
        yield paths
    else:
        santa_path, elephant_path = paths
        santa_moves, elephant_moves = get_moves_2(paths, valves)
        for santa_move, elephant_move in product(santa_moves, elephant_moves):
            if santa_move != elephant_move:
                for p in build_paths_2(
                    valves, move_limit, start_valve, (
                        f"{santa_path}->{santa_move}",
                        f"{elephant_path}->{elephant_move}"
                    )
                ):
                    yield p


def main():
    with open(input_file, "r") as f:
        valves = {
            line.strip().split()[1]: {
                "flow" : int(line.strip().split()[4].strip("rate=;")),
                "tunnels" : [
                                valve.strip(",") 
                                for valve in line.strip().split()[9:]
                            ]
            } 
            for line in f
        }

    path_candidates = [
        (path, pressure_release(path, 30, valves))
        for path in build_paths(valves, 10,)
    ]

    path_candidates.sort(key=lambda x: x[1], reverse=True)
   
    path_candidates_2 = []
    for path in path_candidates[:len(path_candidates)//10000]:
        path_candidates_2.extend([
            (path, pressure_release(path, 30, valves))
            for path in build_paths(valves, 20, path=path[0])
        ])

    path_candidates_2.sort(key=lambda x: x[1], reverse=True)

    path_candidates_3 =[]
    for path in path_candidates_2[:len(path_candidates_2)//10000]:
        path_candidates_3.extend([
            (path, pressure_release(path, 30, valves))
            for path in build_paths(valves, 29, path=path[0])
        ])

    path_candidates_3.sort(key=lambda x: x[1], reverse=True)
    print("Part 1: ", path_candidates_3[0][1])


    path_candidates = [
        (paths, pressure_release_2(paths, 26, valves))
        for paths in build_paths_2(valves, 5)
    ]

    for time in range(6,26):
        print(f"Round: {time}")
        path_candidates.sort(key=lambda x: x[1], reverse=True)
        if len(path_candidates) > 10000:
            path_candidates = path_candidates[:500]

        for paths in path_candidates:
            path_candidates.extend([
                (paths, pressure_release_2(paths, 26, valves))
                for paths in build_paths_2(valves, time, paths=paths[0])
            ])
            path_candidates.remove(paths)

    path_candidates.sort(key=lambda x: x[1], reverse=True)
    print("Part 2: ", path_candidates[0])
        



if __name__ == "__main__":
    main()