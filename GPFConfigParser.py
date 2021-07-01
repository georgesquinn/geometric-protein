def main(config):
    with open("./config/" + config + ".cfg", 'r') as reader:
        # Order is ALWAYS A, V, F, P, M, I, L, Y, W
        config_lines = reader.readlines()
        lengths = []
        allowance_constant = .1
        lengths = [0 for i in range(20)]
        lengths = [1.530085265636444, 2.0762536847600463, 2.6979114702040614, 1.4328493516136427, 3.5248065567136107,
                   3.059942527696086, 2.7475912310394075, 2.716511252921925, 2.800000000000000]
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
            if words[0].upper() == "AC":
                allowance_constant = float(words[1])
    return lengths, allowance_constant
