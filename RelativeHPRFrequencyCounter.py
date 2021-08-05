import HydrophobicResidueCount
import os


hpr_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
per_protein_frequency_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
filenames = os.scandir("./gpf_files")
protein_count = 0
for filename in filenames:
    if filename.is_file() and filename.name[-4:] == ".gpf":
        protein_count += 1
        # print(format(filename.name))
        protein_hpr_counts = HydrophobicResidueCount.main(filename.name[:-4])
        # print(protein_hpr_counts)
        total_count = 0
        for residue_type in protein_hpr_counts:
            total_count += residue_type
        for i in range(0, 9):
            per_protein_frequency_count[i] += protein_hpr_counts[i] / total_count
        for i in range(0, 9):
            # print(format(i))
            hpr_counts[i] += protein_hpr_counts[i]
# Order is ALWAYS A, V, F, P, M, I, L, Y, W
for i in range(0, 9):
    per_protein_frequency_count[i] /= protein_count
absolute_frequencies = [0, 0, 0, 0, 0, 0, 0, 0, 0]
total_count = 0
for residue_type in hpr_counts:
    total_count += residue_type
for i in range(0, 9):
    absolute_frequencies[i] = hpr_counts[i] / total_count
print("Alanine count: " + format(hpr_counts[0]) + ", Absolute frequency: " + format(absolute_frequencies[0]) + ", Relative frequency: " + format(per_protein_frequency_count[0]))
print("Valine count: " + format(hpr_counts[1]) + ", Absolute frequency: " + format(absolute_frequencies[1]) + ", Relative frequency: " + format(per_protein_frequency_count[1]))
print("Phenylalanine count: " + format(hpr_counts[2]) + ", Absolute frequency: " + format(absolute_frequencies[2]) + ", Relative frequency: " + format(per_protein_frequency_count[2]))
print("Proline count: " + format(hpr_counts[3]) + ", Absolute frequency: " + format(absolute_frequencies[3]) + ", Relative frequency: " + format(per_protein_frequency_count[3]))
print("Methionine count: " + format(hpr_counts[4]) + ", Absolute frequency: " + format(absolute_frequencies[4]) + ", Relative frequency: " + format(per_protein_frequency_count[4]))
print("Isoleucine count: " + format(hpr_counts[5]) + ", Absolute frequency: " + format(absolute_frequencies[5]) + ", Relative frequency: " + format(per_protein_frequency_count[5]))
print("Leucine count: " + format(hpr_counts[6]) + ", Absolute frequency: " + format(absolute_frequencies[6]) + ", Relative frequency: " + format(per_protein_frequency_count[6]))
print("Tyrosine count: " + format(hpr_counts[7]) + ", Absolute frequency: " + format(absolute_frequencies[7]) + ", Relative frequency: " + format(per_protein_frequency_count[7]))
print("Tryptophan count: " + format(hpr_counts[8]) + ", Absolute frequency: " + format(absolute_frequencies[8]) + ", Relative frequency: " + format(per_protein_frequency_count[8]))
