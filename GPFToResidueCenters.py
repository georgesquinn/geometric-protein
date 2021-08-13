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
        hp_points = []
        center_identities = []
        for line in hpr_lines:
            words = line.split()
            x_vector = float(words[4]) - float(words[1])
            y_vector = float(words[5]) - float(words[2])
            z_vector = float(words[6]) - float(words[3])
            vector_length = math.sqrt(x_vector * x_vector + y_vector * y_vector + z_vector * z_vector)
            normal_vector = (x_vector / vector_length, y_vector / vector_length, z_vector / vector_length)
            residue_length = residue_lengths[words[0]]
            scaled_vector = (normal_vector[0] * residue_length), normal_vector[1] * residue_length, normal_vector[2] * residue_length
            hp_points.append(
                (float(words[1]) + scaled_vector[0], float(words[2]) + scaled_vector[1], float(words[3]) + scaled_vector[2]))
            center_identities.append(words[0])
        return hp_points, center_identities
