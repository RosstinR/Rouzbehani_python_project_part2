#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Bio import SeqIO
import csv


# In[5]:


gb_files = [
    "sequence.gb",
    "sequence_1.gb",
    "sequence_2.gb",
    "sequence_3.gb",
    "sequence_4.gb",
]

gb_data = []

for f in gb_files:
    with open(f, "r") as file:
        records = SeqIO.parse(file, "genbank")
        for record in records:
            accession = record.annotations.get("accessions", [""])[0]
            family = record.annotations.get("taxonomy", [""])[2]
            genus = record.annotations.get("taxonomy", [""])[3]
            species = record.annotations.get("taxonomy", [""])[4]
            source = record.annotations.get("source", "")
            num_features = len(record.features)

            gb_data.append([accession, family, genus, species, num_features, source])

with open("genbank_parse.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        ["Accession", "Family", "Genus", "Species", "Num_Features", "Source"]
    )
    writer.writerows(gb_data)


# In[ ]:
