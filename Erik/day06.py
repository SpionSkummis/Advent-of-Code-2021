fishies = dict()
for i in range(0,9):
    fishies[i] = 0

with open("Erik/inputs/input06.txt", "r") as f:
    for fishnum in f.read().strip().split(","):
        fishies[int(fishnum)] += 1

def age_fish(in_dict, age_increase):
    for _ in range(age_increase):
        new_fish = in_dict[0]
        for i in range(0,8):
            in_dict[i] = in_dict[i+1]
        in_dict[8] = new_fish
        in_dict[6] += new_fish
    return in_dict

def count_fish(in_dict):
    return sum([in_dict[key] for key in in_dict])

fish_age1 = 80
fish_age2 = 256

fishies1 = age_fish(fishies.copy(), fish_age1)
fishies2 = age_fish(fishies.copy(), fish_age2)

print(f"Part 1: After {fish_age1} generations there would be {count_fish(fishies1)} fishies")
print(f"Part 2: After {fish_age2} generations there would be {count_fish(fishies2)} fishies")
