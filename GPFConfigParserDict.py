def main(config):
    with open("./config/" + config + ".cfg", 'r') as reader:
        config_lines = reader.readlines()
        exemption_constant = .2
        lengths = {"A": 153.00852691566212, "V": 207.83155509108312, "F": 325.43163330791896, "P": 190.59187096044056,
                   "M": 352.4806556713611, "I": 305.9942527696086, "L": 325.0487957278382, "D": 290.35484399575074,
                   "E": 368.98452459464187, "K": 514.4691291658706, "R": 502.07609700112437, "S": 191.84926510062857,
                   "T": 206.88348151835658, "Y": 383.8982301110155, "H": 304.36530135863535, "C": 225.56657779064628,
                   "N": 286.4986470641814, "Q": 350.8501937768497, "W": 334.6099101398435}
        for line in config_lines:
            words = line.split()
            upperchar = words[0].upper()
            # Using upper to make it case-insensitive!
            if upperchar in lengths:
                lengths[upperchar] = float(words[1])
            if upperchar == "EC":
                exemption_constant = float(words[1])
    return lengths, exemption_constant
