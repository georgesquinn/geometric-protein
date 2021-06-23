# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:10:56 2021

@author: Peter
"""
import LengthFinderAla
import LengthFinderVal
protein_name = "2dn2"
print("Ala length is: " + format(LengthFinderAla.main(protein_name)))
print("Val length is: " + format(LengthFinderVal.main(protein_name)))