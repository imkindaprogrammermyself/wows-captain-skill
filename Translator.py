skill_list = [
    ["PT", "PM", "EL", "AS", "DCF", "IEB", "IFA", "LG"],
    ["HA", "JOAT", "EM", "TA", "SSE", "IE", "AR", "LS"],
    ["BOS", "SE", "TAE", "AA", "BFT", "SI", "DE", "VL"],
    ["MFCSA", "FP", "IFHE", "SS", "AFT", "MAAF", "RPF", "CE"]
]
in_str = "PT,PM,AR,EM,SI,BFT,MFCSA"
in_str = list(set("".join(in_str.split()).split(',')))
encoded_skills = ','.join(
    map(str, [int(''.join(["1" if x in [skill_group.index(c) for c in in_str if c in skill_group] else "0" for x
                           in range(8)]), 2) for skill_group in skill_list]))
print(format("https://wows-captain-skill.herokuapp.com/%s" % encoded_skills))
