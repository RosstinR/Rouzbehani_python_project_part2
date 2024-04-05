#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Bio import SeqIO
import csv


# In[4]:


ruddi = ["GCA_000287275.1_genomic.fna"]

ruddi_data = []


def reverse_complement(seq):
    replace_letters = {"A": "T", "C": "G", "G": "C", "T": "A"}
    return "".join(replace_letters.get(i, i) for i in (record.seq[::-1]))


for f in ruddi:
    with open(f, "r") as file:
        records = SeqIO.parse(file, "fasta")
        for record in records:
            length_of_genome = len(record.seq)
            gc_content = (
                (record.seq.count("C") + record.seq.count("G")) / len(record.seq) * 100
            )
            ATG_forward = record.seq.count("ATG")
            ATG_reverse = reverse_complement(record.seq).count("ATG")

            ruddi_data.append([length_of_genome, gc_content, ATG_forward, ATG_reverse])

with open("ruddi_analysis.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Length_of_Genome", "GC_content", "ATG_forward", "ATG_reverse"])
    writer.writerows(ruddi_data)


# In[ ]:
