def main(config):
    with open("./config/" + config + ".cfg", 'r') as reader:
        # Order is ALWAYS A, V, F, P, M, I, L, Y, W
        config_lines = reader.readlines()
        lengths = []
        lengths = [0 for i in range(20)]
        for line in config_lines:
            words = line.split()
            if words[0] == "A":
                lengths[0] = float(words[1])
            if words[0] == "V":
                lengths[1] = float(words[1])
            if words[0] == "F":
                lengths[2] = float(words[1])
            if words[0] == "P":
                lengths[3] = float(words[1])
            if words[0] == "M":
                lengths[4] = float(words[1])
            if words[0] == "I":
                lengths[5] = float(words[1])
            if words[0] == "L":
                lengths[6] = float(words[1])
            if words[0] == "Y":
                lengths[7] = float(words[1])
            if words[0] == "W":
                lengths[8] = float(words[1])
    return lengths