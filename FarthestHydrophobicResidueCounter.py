import FarthestHydrophobicResidue
import json
from os.path import exists

protein_dict = {}
radius_by_ec = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
if exists("./annealbabyprots.json"):
    with open("./annealbabyprots.json", 'r') as f:
        protein_dict = json.load(f)
print(len(protein_dict))
hpr_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for protein_name in protein_dict:
    protein = protein_dict[protein_name]
    farthest_hpr_identity = FarthestHydrophobicResidue.main(protein_name, "default", protein[2][10])[1]
    if farthest_hpr_identity == "A":
        hpr_counts[0] += 1
    if farthest_hpr_identity == "V":
        hpr_counts[1] += 1
    if farthest_hpr_identity == "F":
        hpr_counts[2] += 1
    if farthest_hpr_identity == "P":
        hpr_counts[3] += 1
    if farthest_hpr_identity == "M":
        hpr_counts[4] += 1
    if farthest_hpr_identity == "I":
        hpr_counts[5] += 1
    if farthest_hpr_identity == "L":
        hpr_counts[6] += 1
    if farthest_hpr_identity == "Y":
        hpr_counts[7] += 1
    if farthest_hpr_identity == "W":
        hpr_counts[8] += 1
    # Order is ALWAYS A, V, F, P, M, I, L, Y, W
print("Alanine count: " + format(hpr_counts[0]))
print("Valine count: " + format(hpr_counts[1]))
print("Phenylalanine count: " + format(hpr_counts[2]))
print("Proline count: " + format(hpr_counts[3]))
print("Methionine count: " + format(hpr_counts[4]))
print("Isoleucine count: " + format(hpr_counts[5]))
print("Leucine count: " + format(hpr_counts[6]))
print("Tyrosine count: " + format(hpr_counts[7]))
print("Tryptophan count: " + format(hpr_counts[8]))
