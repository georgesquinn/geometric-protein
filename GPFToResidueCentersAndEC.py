import math
import GPFConfigParserDict


def main(filename, config="default", desired_residues=None):
    # residues_array should be an array of single characters corresponding to the residues you want! This makes things
    # easy to change!
    if desired_residues is None:
        desired_residues = ["A", "V", "F", "P", "M", "I", "L", "Y", "W"]
    with open("./gpf_files/" + filename + ".gpf", 'r') as reader:
        gpf_lines = reader.readlines()
        # hydrophobic residue lines
        hpr_lines = []
        for line in gpf_lines:
            if line[0] in desired_residues:
                hpr_lines.append(line)
        config_results = GPFConfigParserDict.main(config)
        residue_lengths = config_results[0]
        exemption_constant = config_results[1]
        hp_points = []
        for line in hpr_lines:
            words = line.split()
            xvec = float(words[4]) - float(words[1])
            yvec = float(words[5]) - float(words[2])
            zvec = float(words[6]) - float(words[3])
            veclength = math.sqrt(xvec * xvec + yvec * yvec + zvec * zvec)
            normvec = (xvec / veclength, yvec / veclength, zvec / veclength)
            scaledvec = (0, 0, 0)
            residue_length = residue_lengths[words[0]]
            scaledvec = (normvec[0] * residue_length), normvec[1] * residue_length, normvec[2] * residue_length
            hp_points.append(
                (float(words[1]) + scaledvec[0], float(words[2]) + scaledvec[1], float(words[3]) + scaledvec[2]))
        # Order is ALWAYS A, V, F, P, M, I, L, Y, W
        return hp_points, exemption_constant
