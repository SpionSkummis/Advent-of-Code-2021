display = []
with open("Erik/inputs/input08.txt", "r") as f:
    for line in f:
        sign_in, sign_out = line.split("|")
        display.append([[set(x) for x in sign_in.strip().split()], [set(y) for y in sign_out.strip().split()]])

# nr 1 = len 2, nr 4 = len 4, nr 7 = len 3, nr 8 = len 7

nr_dict = {i:0 for i in range(10)}
for disp in display:
    for sign in disp[1]:
        if len(sign) == 2:
            nr_dict[1] += 1
        elif len(sign) == 4:
            nr_dict[4] += 1
        elif len(sign) == 3:
            nr_dict[7] += 1
        elif len(sign) == 7:
            nr_dict[8] += 1
print(f"1, 4, 7, or 8 appears {sum([nr_dict[key] for key in nr_dict])} times")


# Part 2:
output_values = []
for disp in display:
    sign_key = [set() for x in range(10)]
    # Hitta alla säkra kort
    for sign in disp[0]:
        if len(sign) == 2:
            sign_key[1].update(sign)
        elif len(sign) == 4:
            sign_key[4].update(sign)
        elif len(sign) == 3:
            sign_key[7].update(sign)
        elif len(sign) == 7:
            sign_key[8].update(sign)

    # Hitta alla treor, sexor, nior och tvåor
    for sign in disp[0]:
        #tre
        if (len(sign) == 5) and ((sign.issuperset(sign_key[1]) and sign_key[1]) or (sign.issuperset(sign_key[7]) and sign_key[7])):
            sign_key[3].update(sign)
        #sex
        if (len(sign) == 6) and (((len(sign_key[1].difference(sign)) == 1) and sign_key[1]) or ((len(sign_key[7].difference(sign)) == 1) and sign_key[7])):
            sign_key[6].update(sign)
        #nio
        if (len(sign) == 6) and ((len(sign_key[4].difference(sign)) == 0) and sign_key[4]):
            sign_key[9].update(sign)
        #två
        if (len(sign) == 5) and ((len(sign_key[4].difference(sign)) == 2) and sign_key[4]):
            sign_key[2].update(sign)
    for sign in disp[0]:
        #fem?
        if (len(sign) == 5) and (sign != sign_key[2]) and (sign != sign_key[3]):
            sign_key[5].update(sign)
        #noll?
        if (len(sign) == 6) and (sign != sign_key[6]) and (sign != sign_key[9]):
            sign_key[0].update(sign)

    for sign in disp[1]:
        for i in range(len(sign_key)):
            if sign_key[i] == sign:
                output_values.append(i)

part2_ans = []
for i in range(0,len(output_values),4):
    part2_ans.append(output_values[i:i+4])

part2_ans = [int(str(x).replace(", ","").strip("[]")) for x in part2_ans]

print(f"The sum of all outputs is: {sum(part2_ans)}")
