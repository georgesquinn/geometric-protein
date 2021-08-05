import json
from os.path import exists

protein_dict = {}
radius_by_ec = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if exists("./babyprots.json"):
    with open("./babyprots.json", 'r') as f:
        protein_dict = json.load(f)
i = 0
for protein_name in protein_dict:
    i += 1
    if i > 3:
        continue
    protein = protein_dict[protein_name]
    for index in range(0, 11):
        print(format(float(protein[1][index]) / float(protein[0])))
        # radius_by_ec[index] += float(protein[1][index])
    print("Break")
print(format(radius_by_ec))