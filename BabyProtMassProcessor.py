import json
from os.path import exists
import os
import GPFToMESByEC
import concurrent.futures
import multiprocessing as mp

global protein_dict
protein_dict = {}
if exists("./babyprots.json"):
    with open("./babyprots.json", 'r') as f:
        protein_dict = json.load(f)


def process_protein(protein_name, lock):
    hydrophobic_residues = 0
    with open("./gpf_files/" + protein_name + ".gpf", 'r') as reader:
        gpf_lines = reader.readlines()
        for line in gpf_lines:
            if line[0] == "A" or line[0] == "V" or line[0] == "F" or line[0] == "P" or line[0] == "M" \
                    or line[0] == "I" or line[0] == "L" or line[0] == "Y":
                hydrophobic_residues += 1
    # print("Now checking protein " + protein_name)
    if hydrophobic_residues < 42 or hydrophobic_residues > 85:
        return None
    print("Now processing protein " + protein_name)
    mes_array = GPFToMESByEC.main(protein_name)
    lock.acquire()
    # print("Lock acquired by process on protein " + protein_name)
    if exists("./babyprots.json"):
        with open("./babyprots.json", 'r') as f:
            protein_dict = json.load(f)
    protein_dict[protein_name] = (hydrophobic_residues, mes_array)
    # print("Dict modified by process on protein " + protein_name)
    with open("./babyprots.json", 'w') as f:
        # print("File opened by process on protein " + protein_name)
        json.dump(protein_dict, f)
        print("Protein " + protein_name + " processed.")
    lock.release()
    # print("Lock released by process on protein " + protein_name)


if __name__ == '__main__':
    filenames = os.scandir("./gpf_files")
    m = mp.Manager()
    lock = m.Lock()
    protein_names = []
    for filename in filenames:
        if filename.is_file() and filename.name[-4:] == ".gpf" and filename.name[:-4:] not in protein_dict:
            protein_names.append(filename.name[:-4])
    # print(format(protein_names))
    if mp.cpu_count() < 4:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = executor.map(process_protein, protein_names, [lock] * len(protein_names))
            list(futures)
    else:
        with concurrent.futures.ProcessPoolExecutor(max_workers=(mp.cpu_count() - 3)) as executor:
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
#                         or line[0] == "I" or line[0] == "L" or line[0] == "Y":`   1
#                     hydrophobic_residues += 1
#         protein_dict[protein_name] = (hydrophobic_residues, GPFToMESByEC.main(protein_name))
#         with open("./babyprots.json", 'w') as f:
#             json.dump(protein_dict, f)
#             print("Protein " + protein_name + " processed.")
