skill_list = [
    ["PT", "PM", "EL", "AS", "DCF", "IEB", "IFA", "LG"],
    ["HA", "JOAT", "EM", "TA", "SSE", "IE", "AR", "LS"],
    ["BOS", "SE", "TAE", "AA", "BFT", "SI", "DE", "VL"],
    ["MFCSA", "FP", "IFHE", "SS", "AFT", "MAAF", "RPF", "CE"]
]
in_str = "PT,PM,AR,EM,SI,BFT,MFCSA"
in_str = list(set("".join(in_str.split()).split(',')))
print(in_str)
# test = [["1" if x in [skill_group.index(c) for c in in_str if c in skill_group] else "0" for x in range(8)] for skill_group in skill_list]
final = []
for skill_group in skill_list:
    bbb = []
    for x in range(8):
        aaa = []
        for c in in_str:
            if c in skill_group:
                aaa.append(skill_group.index(c))
        if x in aaa:
            bbb.append("1")
        else:
            bbb.append("0")
    final.append(bbb)
print(final)
encoded_skills = ','.join(
    map(str, [int(''.join(["1" if x in [skill_group.index(c) for c in in_str if c in skill_group] else "0" for x
                           in range(8)]), 2) for skill_group in skill_list]))
print(format("https://wows-captain-skill.herokuapp.com/%s" % encoded_skills))
