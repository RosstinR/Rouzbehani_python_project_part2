#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio import SeqIO
import csv


# In[2]:


fasta_files = [
    "sequence.fasta",
    "sequence_1.fasta",
    "sequence_2.fasta",
    "sequence_3.fasta",
]

fasta_data = []

for f in fasta_files:
    with open(f, "r") as file:
        records = SeqIO.parse(file, "fasta")
        for record in records:
            ID = record.id
            First_10_AA = record.seq[:10]
            Length = len(record.seq)
            Number_Cs = record.seq.count("C")

            fasta_data.append([ID, First_10_AA, Length, Number_Cs])

with open("protein_info.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "First_10_AA", "Length", "Number_Cs"])
    writer.writerows(fasta_data)
