import GPFConfigParser
import math


def main(filename):
    with open("./gpf_files/" + filename + ".gpf", 'r') as reader:
        gpf_lines = reader.readlines()
        # hydrophobic residue lines
        hpr_lines = []
        for line in gpf_lines:
            if line[0] == "A" or line[0] == "V" or line[0] == "F" or line[0] == "P" or line[0] == "M" \
                    or line[0] == "I" or line[0] == "L" or line[0] == "Y" or line[0] == "W":
                hpr_lines.append(line)
        hpr_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for line in hpr_lines:
            words = line.split()
            if words[0] == "A":
                hpr_counts[0] += 1
            if words[0] == "V":
                hpr_counts[1] += 1
            if words[0] == "F":
                hpr_counts[2] += 1
            if words[0] == "P":
                hpr_counts[3] += 1
            if words[0] == "M":
                hpr_counts[4] += 1
            if words[0] == "I":
                hpr_counts[5] += 1
            if words[0] == "L":
                hpr_counts[6] += 1
            if words[0] == "Y":
                hpr_counts[7] += 1
            if words[0] == "W":
                hpr_counts[8] += 1
        # Order is ALWAYS A, V, F, P, M, I, L, Y, W
        return hpr_counts
