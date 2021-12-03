with open("Erik/inputs/input03.txt", "r") as f:
    diag_report = [x.strip() for x in f]


gamma_rate = ""
epsilon_rate = ""

for i in range(0, len(diag_report[0])):
    one_count = 0
    for bin in diag_report:
        if bin[i] == "1":
            one_count += 1
    if one_count > (len(diag_report) / 2):
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))


# Part 2
oxygen_gen_rate = diag_report.copy() # Most common
co_scrubber_rate = diag_report.copy() # Least common

for i in range(0, len(diag_report[0])):
    if len(oxygen_gen_rate) == 1:
        break
    one_count = 0
    for bin in oxygen_gen_rate:
        if bin[i] == "1":
            one_count += 1
    if one_count >= (len(oxygen_gen_rate) / 2):
        most_common = "1"
    else:
        most_common = "0"
    oxygen_gen_rate = [x for x in oxygen_gen_rate if x[i] == most_common]

for i in range(0, len(diag_report[0])):
    if len(co_scrubber_rate) == 1:
        break
    one_count = 0
    for bin in co_scrubber_rate:
        if bin[i] == "1":
            one_count += 1
    if one_count >= (len(co_scrubber_rate) / 2):
        least_common = "0"
    else:
        least_common = "1"
    co_scrubber_rate = [x for x in co_scrubber_rate if x[i] == least_common]

print(oxygen_gen_rate, co_scrubber_rate)
print(int(oxygen_gen_rate[0], 2), int(co_scrubber_rate[0],2))
print(int(oxygen_gen_rate[0], 2) * int(co_scrubber_rate[0],2))