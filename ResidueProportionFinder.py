import os
import numpy as np
proportions = []
residue_identities = ["A", "V", "F", "P", "M", "I", "L", "D", "E", "K", "R", "S", "T", "Y", "H", "C", "N", "Q", "W"]
for filename in os.scandir("./gpf_files"):
    if filename.is_file() and filename.name[-4:] == ".gpf":
        protein_name = filename.name[:-4]
        hydrophobic_residues = 0
        alpha_carbons = 0
        with open(filename.path, 'r') as reader:
            gpf_lines = reader.readlines()
            for line in gpf_lines:
                if line[0] in residue_identities:
                    hydrophobic_residues += 1
                else:
                    alpha_carbons += 1
        proportions.append(hydrophobic_residues / alpha_carbons)
avg_proportion = 0
for proportion in proportions:
    avg_proportion += proportion
avg_proportion /= len(proportions)
std_dev = np.std(proportions)
print("Average proportion of hydrophobic residues to backbone carbons is: " + format(avg_proportion))
print("Standard deviation is: " + format(std_dev))
