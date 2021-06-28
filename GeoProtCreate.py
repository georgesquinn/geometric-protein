import GeoProtFileMaker
print("Enter the PDB code of the protein you want to make a GPF for: ")
protein_name = str(input())
GeoProtFileMaker.main(protein_name)