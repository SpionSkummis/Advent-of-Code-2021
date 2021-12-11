display = []
with open("Erik/inputs/input08-t.txt", "r") as f:
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
print(sum([nr_dict[key] for key in nr_dict]))




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
        #beräkna vad som är vad i denna specifika input
    # Hitta alla treor och sexor
    for sign in disp[0]:
        #tre
        if (len(sign) == 5) and ((sign.issuperset(sign_key[1]) and sign_key[1]) or (sign.issuperset(sign_key[7]) and sign_key[7])):
            sign_key[3].update(sign)
        #sex
        if (len(sign) == 6) and ((sign))
    print(sign_key)
    for sign in disp[1]:
        pass
        #beräkna vad som är vad i outputraden
        #print(sign_key)

