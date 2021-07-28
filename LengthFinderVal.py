# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:59:30 2021

@author: Peter
"""
import sys
import re
import numpy as np
from Bio.PDB import *


# This will be for parsing the PDB files
def main(protein_name):
    pdb1 = PDBList()
    pdb1.retrieve_pdb_file(protein_name, pdir='./protein_files')
    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure(protein_name, "./protein_files\\" + protein_name + '.cif')
    dist_array = []
    for chain in structure[0]:
        for residue in chain:
            resname = residue.get_resname()
            if resname == "ALA" or resname == "VAL" or resname == "PHE" or resname == "PRO" or resname == "MET" or resname == "ILE" or resname == "LEU":
                ca_vector = residue['CA'].get_vector()
                cb_vector = residue['CB'].get_vector()
                norm_vec = (cb_vector - ca_vector).normalized()
                if resname == "VAL":
                    cg1_vector = residue['CG1'].get_vector() - ca_vector
                    cg1_projdist = cg1_vector * norm_vec
                    cg2_vector = residue['CG2'].get_vector() - ca_vector
                    cg2_projdist = cg2_vector * norm_vec
                    dist_array.append((cg1_projdist + cg2_projdist) / 2)

    avg_length = 0
    for bond_length in dist_array:
        avg_length += bond_length
    avg_length /= len(dist_array)
    std_dev = np.std(dist_array)
    return (avg_length, std_dev)
