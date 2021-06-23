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
    f = open("./gpf_files/" + protein_name + ".gpf", 'w')
    for chain in structure[0]:
        for residue in chain:
            resname = residue.get_resname()
            if resname != "HOH" and resname != "STU" and resname != "EDO" and resname != "ZN" and resname != "GOL":
                print(resname)
                ca_coords = residue['CA'].get_coord()
                f.write(format(ca_coords[0]) + " " + format(ca_coords[1]) + " " + format(ca_coords[2]) + "\n")
        for residue in chain:
            resname = residue.get_resname()
            if resname == "ALA" or resname == "VAL" or resname == "PHE" or resname == "PRO" or resname == "MET" or resname == "ILE" or resname == "LEU":
                if resname == "ALA":
                    f.write("A ")
                if resname == "VAL":
                    f.write("V ")
                if resname == "PHE":
                    f.write("F ")
                if resname == "PRO":
                    f.write("P ")
                if resname == "MET":
                    f.write("M ")
                if resname == "ILE":
                    f.write("I ")
                if resname == "LEU":
                    f.write("L ")
                ca_coords = residue['CA'].get_coord()
                f.write(format(ca_coords[0]) + " " + format(ca_coords[1]) + " " + format(ca_coords[2]))
                cb_coords = residue['CB'].get_coord()
                f.write(format(cb_coords[0]) + " " + format(cb_coords[1]) + " " + format(cb_coords[2]) + "\n")
    f.close()
    return True
