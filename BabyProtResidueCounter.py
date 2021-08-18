import GPFResisdueCounter
import os


residue_identities = ["A", "V", "F", "P", "M", "I", "L", "D", "E", "K", "R", "S", "T", "Y", "H", "C", "N", "Q", "W"]
absolute_frequency_dict = {}
relative_frequency_dict = {}
for residue in residue_identities:
    absolute_frequency_dict[residue] = 0
    relative_frequency_dict[residue] = 0
filenames = os.scandir("./gpf_files")
protein_count = 0
for filename in filenames:
    if filename.is_file() and filename.name[-4:] == ".gpf":
        protein_count += 1
        # print(format(filename.name))
        individual_frequency_dict = GPFResisdueCounter.main(filename.name[:-4], residue_identities)
        # print(protein_hpr_counts)
        for residue in individual_frequency_dict:
            absolute_frequency_dict[residue] += individual_frequency_dict[residue]
        residue_count = 0
        for residue in individual_frequency_dict:
            residue_count += individual_frequency_dict[residue]
        for residue in individual_frequency_dict:
            individual_frequency_dict[residue] /= residue_count
            relative_frequency_dict[residue] += individual_frequency_dict[residue]
for residue in relative_frequency_dict:
    relative_frequency_dict[residue] /= protein_count
total_count = 0
print("Absolute Occurances: " + format(absolute_frequency_dict))
for residue in absolute_frequency_dict:
    total_count += absolute_frequency_dict[residue]
for residue in absolute_frequency_dict:
    absolute_frequency_dict[residue] /= total_count
print("Religious Relative Frequencies: " + format(absolute_frequency_dict))
print("Agnostic Relative Frequencies: " + format(relative_frequency_dict))
