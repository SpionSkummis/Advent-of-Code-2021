import math

hex2bin = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
           "4": "0100", "5": "0101", "6": "0110", "7": "0111",
           "8": "1000", "9": "1001", "A": "1010", "B": "1011",
           "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

def string2bits(bitstring):
    return "".join([hex2bin[x] for x in bitstring])

def bits2int(bits):
    s = 0
    n = len(bits) - 1
    for i, x in enumerate(bits):
        s += int(x)*2**(n - i)
    return s

def parse_packet(bits):
    packet = {}
    packet["version"] = bits2int(bits[0:3])
    packet["type_id"] = bits2int(bits[3:6])
    packet["size"] = 6

    if packet["type_id"] == 4: # Literal value
        value = ""
        i = 6
        while bits[i] == "1":
            value += bits[i + 1: i + 5]
            i += 5
        value += bits[i + 1: i + 5]
        packet["value"] = bits2int(value)
        packet["size"] += len(value) // 4 * 5
    else: # Operator packet
        packet["subpackets"] = []
        total_subpackets_length = 16
        
        if bits[6] == "0": #Length type ID 0
            subpacket_length = bits2int(bits[7:22])
            subpacket_bits = bits[22:22 + subpacket_length]
            while len(subpacket_bits) > 0:
                new_packet = parse_packet(subpacket_bits)
                packet["subpackets"].append(new_packet)
                subpacket_bits = subpacket_bits[new_packet["size"]:]
                total_subpackets_length += new_packet["size"]

        else:
            number_of_subpackets = bits2int(bits[7:18])
            total_subpackets_length = 12
            subpacket_bits = bits[18:]
            while len(packet["subpackets"]) < number_of_subpackets \
                  and len(subpacket_bits) >= 11:
                new_packet = parse_packet(subpacket_bits)
                packet["subpackets"].append(new_packet)
                subpacket_bits = subpacket_bits[new_packet["size"]:]
                total_subpackets_length += new_packet["size"]
            
        packet["size"] += total_subpackets_length
    return packet    

def version_sum(packet_list):
    s = 0
    for p in packet_list:
        if "subpackets" in p:
            subpacket_sum = version_sum(p["subpackets"])
            s += subpacket_sum
        s += p["version"]
    return s

def packet_value(packet):
    if packet["type_id"] == 0: # Sum
        pval = 0
        for p in packet["subpackets"]:
            pval += packet_value(p)
    elif packet["type_id"] == 1: # Product
        pval = 1
        for p in packet["subpackets"]:
            pval *= packet_value(p)
    elif packet["type_id"] == 2: # Minimum
        pval = min(packet_value(p) for p in packet["subpackets"])
    elif packet["type_id"] == 3: # Maximum
        pval = max(packet_value(p) for p in packet["subpackets"])
    elif packet["type_id"] == 4: # Literal
        pval = packet["value"]
    elif packet["type_id"] == 5: # Greater than
        subpackets = packet["subpackets"]
        pval = 1 if packet_value(subpackets[0]) > packet_value(subpackets[1]) else 0
    elif packet["type_id"] == 6: # Less than
        subpackets = packet["subpackets"]
        pval = 1 if packet_value(subpackets[0]) < packet_value(subpackets[1]) else 0
    elif packet["type_id"] == 7: # Equal to
        subpackets = packet["subpackets"]
        pval = 1 if packet_value(subpackets[0]) == packet_value(subpackets[1]) else 0
    return pval

# INPUT

with open("inputs/day16.txt") as f:
    input = f.readlines()[0][:-1]

packet_structure = parse_packet(string2bits(input))

# PART ONE

res1 = version_sum([packet_structure])
    
print(f"Part 1: The sum of all versions is {res1}")

# PART TWO

res2 = packet_value(packet_structure)

print(f"Part 2: The value of the packet is {res2}")
