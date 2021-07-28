import math

import GPFConfigParser
import PermissiveSphereJiggleFinder


def main(filename):
    main(filename, "default")


def main(filename, config):
    with open("./gpf_files/" + filename + ".gpf", 'r') as reader:
        gpf_lines = reader.readlines()
        # hydrophobic residue lines
        hpr_lines = []
        for line in gpf_lines:
            if line[0] == "A" or line[0] == "V" or line[0] == "F" or line[0] == "P" or line[0] == "M" \
                    or line[0] == "I" or line[0] == "L" or line[0] == "Y":
                hpr_lines.append(line)
        config_results = GPFConfigParser.main(config)
        res_lengths = config_results[0]
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
            if words[0] == "A":
                scaledvec = (normvec[0] * res_lengths[0], normvec[1] * res_lengths[0], normvec[2] * res_lengths[0])
            if words[0] == "V":
                scaledvec = (normvec[0] * res_lengths[1], normvec[1] * res_lengths[1], normvec[2] * res_lengths[1])
            if words[0] == "F":
                scaledvec = (normvec[0] * res_lengths[2], normvec[1] * res_lengths[2], normvec[2] * res_lengths[2])
            if words[0] == "P":
                scaledvec = (normvec[0] * res_lengths[3], normvec[1] * res_lengths[3], normvec[2] * res_lengths[3])
            if words[0] == "M":
                scaledvec = (normvec[0] * res_lengths[4], normvec[1] * res_lengths[4], normvec[2] * res_lengths[4])
            if words[0] == "I":
                scaledvec = (normvec[0] * res_lengths[5], normvec[1] * res_lengths[5], normvec[2] * res_lengths[5])
            if words[0] == "L":
                scaledvec = (normvec[0] * res_lengths[6], normvec[1] * res_lengths[6], normvec[2] * res_lengths[6])
            if words[0] == "Y":
                scaledvec = (normvec[0] * res_lengths[7], normvec[1] * res_lengths[7], normvec[2] * res_lengths[7])
            if words[0] == "W":
                scaledvec = (normvec[0] * res_lengths[8], normvec[1] * res_lengths[8], normvec[2] * res_lengths[8])
            hp_points.append((float(words[1]) + scaledvec[0], float(words[2]) + scaledvec[1], float(words[3]) + scaledvec[2]))
        # Order is ALWAYS A, V, F, P, M, I, L, Y, W
        smallest_sphere = PermissiveSphereJiggleFinder.main(hp_points, exemption_constant)
        return smallest_sphere
