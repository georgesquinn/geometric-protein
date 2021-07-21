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
import LengthFinderTyr
protein_name = "7AKO"
ala_results = LengthFinderAla.main(protein_name)
val_results = LengthFinderVal.main(protein_name)
leu_results = LengthFinderLeu.main(protein_name)
ile_results = LengthFinderIle.main(protein_name)
met_results = LengthFinderMet.main(protein_name)
phe_results = LengthFinderPhe.main(protein_name)
pro_results = LengthFinderPro.main(protein_name)
tyr_results = LengthFinderTyr.main(protein_name)
print("Ala length is: " + format(ala_results[0]))
print("Val length is: " + format(val_results[0]))
print("Leu length is: " + format(leu_results[0]))
print("Ile length is: " + format(ile_results[0]))
print("Met length is: " + format(met_results[0]))
print("Phe length is: " + format(phe_results[0]))
print("Pro length is: " + format(pro_results[0]))
print("Tyr length is: " + format(tyr_results[0]))

print("Ala std dev is: " + format(ala_results[1]))
print("Val std dev is: " + format(val_results[1]))
print("Leu std dev is: " + format(leu_results[1]))
print("Ile std dev is: " + format(ile_results[1]))
print("Met std dev is: " + format(met_results[1]))
print("Phe std dev is: " + format(phe_results[1]))
print("Pro std dev is: " + format(pro_results[1]))
print("Tyr std dev is: " + format(tyr_results[1]))

