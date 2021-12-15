with open("inputs/day12.txt") as f:
    cave = {}
    for d in f.readlines():
        conn = d.strip().split("-")
        for i in [0,1]:
            if conn[i] in cave:
                cave[conn[i]].append(conn[i-1])
            else:
                cave[conn[i]] = [conn[i-1]]
            
def possible_nodes(node, path, part2 = False):
    possible_steps = []
    for c in cave[node]:
        if c.isupper() or c not in path or (part2 and c != "start"):
            possible_steps.append(c)
    return possible_steps

def find_paths(node, prev_path = [], part2 = False):
    path = prev_path.copy()
    path.append(node)
    if node == "end":
        return path
    possible_steps = possible_nodes(node, prev_path, part2) 
    paths = []
    for c in possible_steps:
        if c.islower() and c in path:
            paths.extend(find_paths(c, path, False))
        else:
            paths.extend(find_paths(c, path, part2))
    return paths
    
res1 = find_paths("start").count("end")
print(f"Part 1: The number of paths through the cave is {res1}")

res2 = find_paths("start", part2 = True).count("end")
print(f"Part 2: The number of paths through the cave is {res2}")

