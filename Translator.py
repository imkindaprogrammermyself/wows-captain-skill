# bits = format(255, "08b")
skill_list = [
    ["PT", "PM", "EL", "AS", "DCF", "IEB", "IFA", "LG"],
    ["HA", "JOAT", "EM", "TA", "SSE", "IE", "AR", "LS"],
    ["BOS", "SE", "TAE", "AA", "BFT", "SI", "DE", "VL"],
    ["MFCSA", "FP", "IFHE", "SS", "AFT", "MAAF", "RPF", "CE"]
]
bits_arr = ["10000001", "00100001", "00010001", "00000011"]
result = [skill_list[s][i] for s, bits in enumerate(bits_arr) for i, v in enumerate(bits) if v == "1"]
print(result)

in_str = "PT,PM,AR,LS,SI,CE,TA"
in_str = "".join(in_str.split()).split(',')
tiered_skills = [int(''.join(["1" if x in [skill_group.index(c) for c in in_str if c in skill_group] else "0" for x
                              in range(8)]), 2) for skill_group in skill_list]
print(tiered_skills)
