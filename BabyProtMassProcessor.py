import json
from os.path import exists
import os
import GPFToMESByEC
protein_dict = {}
if exists("./babyprots.json"):
    with open("./babyprots.json", 'r') as f:
        protein_dict = json.load(f)
for filename in os.scandir("./gpf_files"):
    if filename.is_file() and filename.name[-4:] == ".gpf":
        protein_name = filename.name[:-4]
        if protein_name in protein_dict:
            continue
        hydrophobic_residues = 0
        with open("./gpf_files/" + filename + ".gpf", 'r') as reader:
            gpf_lines = reader.readlines()
            for line in gpf_lines:
                if line[0] == "A" or line[0] == "V" or line[0] == "F" or line[0] == "P" or line[0] == "M" \
                        or line[0] == "I" or line[0] == "L" or line[0] == "Y":
                    hydrophobic_residues += 1
        protein_dict[protein_name] = (hydrophobic_residues, GPFToMESByEC.main(protein_name))
        with open("./babyprots.json", 'w') as f:
            json.dump(protein_dict, f)
            print("Protein " + protein_name + " processed.")

