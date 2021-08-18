import GPFToOutsideConvexHullCount
import os

global protein_dict
protein_dict = {}
residue_identities = ["A", "V", "F", "P", "M", "I", "L", "D", "E", "K", "R", "S", "T", "Y", "H", "C", "N", "Q", "W"]
outside_dict = {}
for residue in residue_identities:
    outside_dict[residue] = 0
for filename in os.scandir("./gpf_files"):
    if filename.is_file() and filename.name[-4:] == ".gpf":
        protein_name = filename.name[:-4]
        individual_outside_dict = GPFToOutsideConvexHullCount.main(protein_name)
        for residue in residue_identities:
            outside_dict[residue] += individual_outside_dict[residue]
print(format(outside_dict))