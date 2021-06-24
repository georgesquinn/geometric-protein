import GeoProtFileMaker

protein_names = ["3DLW", "3ELI", "3EKC", "3EKJ", "3EG4", "3EA8", "3DZ1"]
for protein_name in protein_names:
    GeoProtFileMaker.main(protein_name)