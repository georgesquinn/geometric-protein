# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 10:59:30 2021

@author: Peter
"""
from Bio.PDB import *
import os


# This will be for parsing the PDB files
def main(protein_name):
    print("Now processing protein: " + protein_name)
    pdb1 = PDBList()
    pdb1.retrieve_pdb_file(protein_name, pdir='./protein_files', file_format='mmCif')
    parser = MMCIFParser(QUIET=True)
    try:
        structure = parser.get_structure(protein_name, "./protein_files\\" + protein_name + '.cif')
    except:
        print("Protein " + protein_name + " skipped for throwing error in structure step")
        return False
    f = open("./gpf_files/" + protein_name + ".gpf", 'w')
    for chain in structure[0]:
        for residue in chain:
            resname = residue.get_resname()
            troublemakers = ["HOH", "STU", "EDO", "ZN", "GOL", "CRO", "MG", "AZI", "MPD", "GLC"]
            if resname not in troublemakers:
                # print(resname)
                try:
                    ca_coords = residue['CA'].get_coord()
                except:
                    f.close()
                    os.remove("./gpf_files/" + protein_name + ".gpf")
                    print("Protein " + protein_name + " skipped for throwing error in alpha backbone step")
                    print("Residue that caused error: " + resname)
                    return False
                f.write(format(ca_coords[0] * 100) + " " + format(ca_coords[1] * 100) + " " + format(
                    ca_coords[2] * 100) + "\n")
        for residue in chain:
            resname = residue.get_resname()
            residue_identities = ["ALA", "VAL", "PHE", "PRO", "MET", "ILE", "LEU", "ASP", "GLU", "LYS", "ARG", "SER",
                                  "THR", "TYR", "HIS", "CYS", "ASN", "GLN", "TRP", "G2F", "NAG"]
            if resname in residue_identities:
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
                if resname == "ASP":
                    f.write("D ")
                if resname == "GLU":
                    f.write("E ")
                if resname == "LYS":
                    f.write("K ")
                if resname == "ARG":
                    f.write("R ")
                if resname == "SER":
                    f.write("S ")
                if resname == "THR":
                    f.write("T ")
                if resname == "TYR":
                    f.write("Y ")
                if resname == "HIS":
                    f.write("H ")
                if resname == "CYS":
                    f.write("C ")
                if resname == "ASN":
                    f.write("N ")
                if resname == "GLN":
                    f.write("Q ")
                if resname == "TRP":
                    f.write("W ")
                try:
                    ca_coords = residue['CA'].get_coord()
                    f.write(format(ca_coords[0] * 100) + " " + format(ca_coords[1] * 100) + " " + format(
                        ca_coords[2] * 100) + " ")
                    cb_coords = residue['CB'].get_coord()
                    f.write(format(cb_coords[0] * 100) + " " + format(cb_coords[1] * 100) + " " + format(
                        cb_coords[2] * 100) + "\n")
                except:
                    f.close()
                    os.remove("./gpf_files/" + protein_name + ".gpf")
                    print("Protein " + protein_name + " skipped for throwing error in hydrophobic step")
                    print("Residue that caused error: " + resname)
                    return False
    print("GPF file of protein " + protein_name + " successfully created.")
    f.close()
    return True
