print('Advent of Code 2021 - December 12 - Olof\n')
input = list(open('Olof\day12_input.txt','r').read().splitlines())

# Skapa först en dict fylld med tomma sets
cavesystem = dict()
for i in input:
    cavesystem[i.split('-')[0]] = set()
    cavesystem[i.split('-')[1]] = set()
for i in input:
    k = i.split('-')[0]
    v = i.split('-')[1]
    cavesystem[k].add(v)
    cavesystem[v].add(k)

#--------------------------------------------------------------------
# Part 1
part1paths = []

def visitCaves(node, pathSoFar):
    pathSoFar.append(node)

    for cave in pathSoFar:
        if cave.islower() and pathSoFar.count(cave) > 1:
            return

    if node == 'end':
        part1paths.append(pathSoFar)
        return
    
    for connection in cavesystem[node]:
        newPath = pathSoFar.copy()
        visitCaves(connection, newPath)
        
visitCaves('start', [])
print('Part 1: ' + str(len(part1paths)))
#--------------------------------------------------------------------
# Part 2
part2paths = []
#rekursiv funktion:
def visitCaves2(node, pathSoFar):
    pathSoFar.append(node)

    if pathSoFar.count('start') > 1:
        return

    smallsVisitedTwice = 0
    for cave in cavesystem.keys():
        if cave.islower():
            if pathSoFar.count(cave) > 2:
                return
            elif pathSoFar.count(cave) == 2:
                smallsVisitedTwice +=1
                if smallsVisitedTwice > 1:
                    return

    if node == 'end':
        part2paths.append(pathSoFar)
        return
    
    for connection in cavesystem[node]:
        newPath = pathSoFar.copy()
        visitCaves2(connection, newPath)
        
visitCaves2('start', [])
print('Part 2: ' + str(len(part2paths)))