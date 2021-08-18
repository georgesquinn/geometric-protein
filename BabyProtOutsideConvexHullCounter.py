import GPFToOutsideConvexHullCount
import os


def take_second_element(e):
    return e[1]


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
agnostic_relative_frequencies = {'A': 0.0854376670810326, 'V': 0.077531607706879, 'F': 0.042222249645948035, 'P': 0.0474138027636771, 'M': 0.021809843345397605, 'I': 0.06030348141246031, 'L': 0.0953185916220778, 'D': 0.06139054775445695, 'E': 0.06933441284874296, 'K': 0.07021716830392948, 'R': 0.054474600470546336, 'S': 0.06521003721929342, 'T': 0.06109185233033144, 'Y': 0.03747078378127289, 'H': 0.02195858924334445, 'C': 0.01987685544999906, 'N': 0.0516101742995614, 'Q': 0.04106231828591018, 'W': 0.016265416435141126}
scaled_outside_counts = {}
for residue in outside_dict:
    scaled_outside_counts[residue] = outside_dict[residue] / agnostic_relative_frequencies[residue]
print(format(scaled_outside_counts))
scaled_counts_array = []
for residue in scaled_outside_counts:
    scaled_counts_array.append((residue, scaled_outside_counts[residue]))
scaled_counts_array.sort(key=take_second_element)
print(format(scaled_counts_array))