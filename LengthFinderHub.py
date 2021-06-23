# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:10:56 2021

@author: Peter
"""
import LengthFinderAla
import LengthFinderVal
import LengthFinderLeu
import LengthFinderIle
import LengthFinderMet
import LengthFinderPhe
import LengthFinderPro
protein_name = "7AKO"
print("Ala length is: " + format(LengthFinderAla.main(protein_name)))
print("Val length is: " + format(LengthFinderVal.main(protein_name)))
print("Leu length is: " + format(LengthFinderLeu.main(protein_name)))
print("Ile length is: " + format(LengthFinderIle.main(protein_name)))
print("Met length is: " + format(LengthFinderMet.main(protein_name)))
print("Phe length is: " + format(LengthFinderPhe.main(protein_name)))
print("Pro length is: " + format(LengthFinderPro.main(protein_name)))

