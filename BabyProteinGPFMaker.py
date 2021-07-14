import csv
import GPFMaker

results = []
with open("baby_protein_ids.txt") as csvfile:
    reader = csv.reader(csvfile)  # change contents to floats
    for row in reader:  # each row is a list
        for element in row:
            results.append(element)
print(format(results))
for protein_id in results:
    GPFMaker.main(protein_id)
