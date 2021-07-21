import json
from os.path import exists
import os
import GPFToMESByEC
import concurrent.futures
import multiprocessing as mp

global protein_dict


def process_protein(protein_name, lock):
    print("Protein " + protein_name + " processing.")
    hydrophobic_residues = 0
    with open("./gpf_files/" + protein_name + ".gpf", 'r') as reader:
        gpf_lines = reader.readlines()
        for line in gpf_lines:
            if line[0] == "A" or line[0] == "V" or line[0] == "F" or line[0] == "P" or line[0] == "M" \
                    or line[0] == "I" or line[0] == "L" or line[0] == "Y":
                hydrophobic_residues += 1
    lock.acquire()
    protein_dict[protein_name] = (hydrophobic_residues, GPFToMESByEC.main(protein_name))
    with open("./babyprots.json", 'w') as f:
        json.dump(protein_dict, f)
        print("Protein " + protein_name + " processed.")
    lock.release()


if __name__ == '__main__':
    protein_dict = {}
    if exists("./babyprots.json"):
        with open("./babyprots.json", 'r') as f:
            protein_dict = json.load(f)
    filenames = os.scandir("./gpf_files")
    m = mp.Manager()
    lock = m.Lock()
    protein_names = []
    for filename in filenames:
        if filename.is_file() and filename.name[-4:] == ".gpf" and filename.name[:-4:] not in protein_dict:
            protein_names.append(filename.name[:-4])
    print(format(protein_names))
    # on Retriever, add max_workers=29 as an argument to ProcessPoolExecutor constructor!!!
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = executor.map(process_protein, protein_names, [lock] * len(protein_names))
        list(futures)
# for filename in os.scandir("./gpf_files"):
#     if filename.is_file() and filename.name[-4:] == ".gpf":
#         protein_name = filename.name[:-4]
#         if protein_name in protein_dict:
#             continue
#         print("Protein " + protein_name + " processing.")
#         hydrophobic_residues = 0
#         with open(filename.path, 'r') as reader:
#             gpf_lines = reader.readlines()
#             for line in gpf_lines:
#                 if line[0] == "A" or line[0] == "V" or line[0] == "F" or line[0] == "P" or line[0] == "M" \
#                         or line[0] == "I" or line[0] == "L" or line[0] == "Y":
#                     hydrophobic_residues += 1
#         protein_dict[protein_name] = (hydrophobic_residues, GPFToMESByEC.main(protein_name))
#         with open("./babyprots.json", 'w') as f:
#             json.dump(protein_dict, f)
#             print("Protein " + protein_name + " processed.")
