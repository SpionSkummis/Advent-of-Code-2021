
with open("Erik/inputs/input14-t.txt", "r") as f:
    polymer_start = f.readline().strip()
    f.readline() #Fulhack hela dagen
    ins_dict = dict()
    for instr in f.readlines():
        key, val = instr.strip().split(" -> ")
        ins_dict[key] = val


def age_polymer(start_pol, pol_dict):
    #test_pol = list(start_pol)
    #for i in range(len(start_pol)-1):
    newchars = ""
    new_pol = ""
    for i in range(len(start_pol)-1):
        newchars += pol_dict[start_pol[i:i+2]]
    
    for i in range(len(newchars)):
        new_pol += start_pol[i] + newchars[i]
    new_pol += start_pol[-1]
    
    return new_pol

def age_generations(start_pol, pol_dict, generations):
    new_pol = start_pol
    for _ in range(generations):
        new_pol = age_polymer(new_pol, pol_dict)
    return new_pol

def part_one_counter(in_str):
    all_chars = set(in_str)
    max_count = -1
    max_char = ""
    min_count = len(in_str)
    min_char = ""
    for char in all_chars:
        curr_count = in_str.count(char)
        if curr_count > max_count:
            max_count = curr_count
            max_char = char
        if curr_count < min_count:
            min_count = curr_count
            min_char = char
    print(max_count, max_char, min_count,min_char)
    return max_count - min_count

#Part 1:
part1_polymer = age_generations(polymer_start, ins_dict, 10)
print(part_one_counter(part1_polymer))
###

print(polymer_start)

"""
# Testin: NNCB
p1 = age_generations("NN", ins_dict, 40)
p2 = age_generations("NC", ins_dict, 10)
p3 = age_generations("CB", ins_dict, 10)

testmerge = p1 + p2[1:] + p3[1:]

print(part_one_counter(testmerge))
"""
"""
for i in range(7):
    print(age_generations("CB", ins_dict, i))
"""




def age_polymer2(start_pol, pol_dict):
    #test_pol = list(start_pol)
    #for i in range(len(start_pol)-1):
    newchars = ""
    new_pol = ""
    for i in range(len(start_pol)-1):
        new_pol += pol_dict[start_pol[i:i+2]]
    
    return new_pol

def age_generations2(start_pol, pol_dict, generations):
    new_pol = start_pol
    for _ in range(generations):
        new_pol = age_polymer2(new_pol, pol_dict)
    return new_pol


test_dict = dict()
for key in ins_dict:
    test_dict[key] = age_generations(key, ins_dict, 10)
test_dict2 = dict()
for key in test_dict:
    test_dict2[key] = age_generations2(key, test_dict, 2)
test_dict3 = dict()
for key in test_dict:
    test_dict3[key] = age_generations2(key, test_dict2, 2)

#test = age_generations2(polymer_start, test_dict, 1)
test = age_generations2(polymer_start, test_dict3, 1)
#for key in test_dict:
#    print(len(test_dict[key]))

print(part_one_counter(test))