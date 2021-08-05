import FarthestHydrophobicResidue
import json
from os.path import exists

protein_dict = {}
radius_by_ec = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if exists("./annealbabyprots.json"):
    with open("./annealbabyprots.json", 'r') as f:
        protein_dict = json.load(f)
i = 0
for protein_name in protein_dict:
    protein = protein_dict[protein_name]
    print(format(FarthestHydrophobicResidue.main(protein_name, "default", protein[2][10])))
