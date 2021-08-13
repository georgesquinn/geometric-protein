import sys
import re
import numpy as np
from Bio.PDB import *


def main(protein_name):
    pdb1 = PDBList()
    pdb1.retrieve_pdb_file(protein_name, pdir='./protein_files')
    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure(protein_name, "./protein_files\\" + protein_name + '.cif')
    residue_types = ["ALA", "VAL", "PHE", "PRO", "MET", "ILE", "LEU", "ASP", "GLU", "LYS", "ARG", "SER", "THR", "TYR",
                     "HIS", "CYS", "ASN", "GLN", "TRP"]
    center_distances = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #for residue_type in residue_types:
    for i in range(0, len(residue_types), 1):
        residue_type = residue_types[i]
        residue_instances = 0
        atom_lengths = {}
        for chain in structure[0]:
            for residue in chain:
                resname = residue.get_resname()
                if resname == residue_type:
                    residue_instances += 1
                    # print(format(residue))
                    ca_vector = residue['CA'].get_vector()
                    cb_vector = residue['CB'].get_vector()
                    norm_vec = (cb_vector - ca_vector).normalized()
                    for atom in residue:
                        # print(format(atom))
                        atom_vector = atom.get_vector() - ca_vector
                        atom_projdist = atom_vector * norm_vec
                        atom_name = atom.get_name()
                        if atom_name not in atom_lengths:
                            atom_lengths[atom_name] = atom_projdist
                        else:
                            atom_lengths[atom_name] += atom_projdist
        # atom_lengths.sort(reverse=True)
        for atom in atom_lengths:
            atom_lengths[atom] /= residue_instances
        #print(format(atom_lengths))
        longest_length = 0
        for atom in atom_lengths:
            if atom_lengths[atom] > longest_length:
                longest_length = atom_lengths[atom]
        print(residue_type + ": " + format(longest_length * 100))
        center_distances[i] = longest_length

    return center_distances
