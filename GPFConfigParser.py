def main(config):
    with open("./config/" + config + ".cfg", 'r') as reader:
        # Order is ALWAYS A, V, F, P, M, I, L, Y, W
        config_lines = reader.readlines()
        lengths = []
        exemption_constant = .1
        lengths = [0 for i in range(20)]
        lengths = [153.0085265636444, 207.62536847600463, 269.79114702040614, 143.28493516136427, 352.48065567136107,
                   305.9942527696086, 274.75912310394075, 271.6511252921925, 280.0000000000000]
        for line in config_lines:
            words = line.split()
            if words[0].upper() == "A":
                lengths[0] = float(words[1])
            if words[0].upper() == "V":
                lengths[1] = float(words[1])
            if words[0].upper() == "F":
                lengths[2] = float(words[1])
            if words[0].upper() == "P":
                lengths[3] = float(words[1])
            if words[0].upper() == "M":
                lengths[4] = float(words[1])
            if words[0].upper() == "I":
                lengths[5] = float(words[1])
            if words[0].upper() == "L":
                lengths[6] = float(words[1])
            if words[0].upper() == "Y":
                lengths[7] = float(words[1])
            if words[0].upper() == "W":
                lengths[8] = float(words[1])
            if words[0].upper() == "EC":
                exemption_constant = float(words[1])
    return lengths, exemption_constant
