def main(filename):
    with open("./gpf_files/" + filename + ".gpf", 'r') as reader:
        gpf_lines = reader.readlines()
        # hydrophobic residue lines
        backbone_points = []
        for line in gpf_lines:
            if line[0].isalpha():
                continue
            words = line.split()
            backbone_points.append((words[0], words[1], words[2]))
        # Order is ALWAYS A, V, F, P, M, I, L, Y, W
        return backbone_points
