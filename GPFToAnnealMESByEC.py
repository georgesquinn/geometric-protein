import GPFMESAnnealInterface


def main(protein_name):
    ex10 = GPFMESAnnealInterface.main(protein_name, "10")
    ex11 = GPFMESAnnealInterface.main(protein_name, "11")
    ex12 = GPFMESAnnealInterface.main(protein_name, "12")
    ex13 = GPFMESAnnealInterface.main(protein_name, "13")
    ex14 = GPFMESAnnealInterface.main(protein_name, "14")
    ex15 = GPFMESAnnealInterface.main(protein_name, "15")
    ex16 = GPFMESAnnealInterface.main(protein_name, "16")
    ex17 = GPFMESAnnealInterface.main(protein_name, "17")
    ex18 = GPFMESAnnealInterface.main(protein_name, "18")
    ex19 = GPFMESAnnealInterface.main(protein_name, "19")
    ex20 = GPFMESAnnealInterface.main(protein_name, "20")
    return (ex10[0], ex11[0], ex12[0], ex13[0], ex14[0], ex15[0], ex16[0], ex17[0], ex18[0], ex19[0], ex20[0]), (ex10[1], ex11[1], ex12[1], ex13[1], ex14[1], ex15[1], ex16[1], ex17[1], ex18[1], ex19[1], ex20[1])
