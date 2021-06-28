import GPFMESInterface
print("Please input the PDB name of the GPF file you want to find the MES for: ")
protein_name = str(input())
print("Please input the name of the config file you want to use (Leave blank for default) :")
config_name = str(input())
if config_name == "":
    config_name = "default"
sphere = GPFMESInterface.main(protein_name, config_name)
print("Sphere radius is: " + format(sphere[0]))
print("Sphere center is: " + format(sphere[1]))