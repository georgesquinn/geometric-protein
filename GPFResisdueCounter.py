import GPFConfigParser
import math


def main(filename, desired_residues):
    with open("./gpf_files/" + filename + ".gpf", 'r') as reader:
        gpf_lines = reader.readlines()
        # hydrophobic residue lines
        desired_lines = []
        residue_counts = {}
        for line in gpf_lines:
            if line[0] in desired_residues:
                desired_lines.append(line)
        for residue in desired_residues:
            residue_counts[residue] = 0
        for line in desired_lines:
            words = line.split()
            residue_counts[words[0]] += 1
        return residue_counts
