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
    pdb1.retrieve_pdb_file(protein_name)
    parser = PDBParser()

    # structure = parser.get_structure(protein)
    # f = open('Files/' + fileName, 'r')
    # text = f.read()
    # f.close()
    # #Off-by-one-line error on this splitting - must include TER
    # #line on prior array
    # dataLines = []
    # for line in text:
    #     if("ATOM" in line or "TER" in line and "REMARK" not in line):
    #         dataLines.append(line)
    # subunitsArray = str(dataLines).split('TER')
    # print(format(len(subunitsArray)))
    # for subunit in subunitsArray:
    #     atomsArray = subunit.split('\n')
    #     #print(format(atomsArray))
    #     print(format(len(atomsArray)))
    #     print(format(atomsArray[len(atomsArray) - 1]))
    #     #TODO: Make it make seperate lists for each subunit
    #     #TODO: Make sure there's no issues with numbers
    #     peptideNumber = int((re.findall('[\S]+', atomsArray[len(atomsArray) - 1]))[5])
    #     print(format(peptideNumber))
    #     peptidesArray = []
    #     for i in range (0, peptideNumber):
    #         peptidesArray.append([])
    #     print(format(len(peptidesArray)))
    #     for atom in atomsArray:
    #         number = int((re.findall('[\S]+', atom))[5])
    #         peptidesArray[number - 1].append(atom)
    #     print(format(peptidesArray))
