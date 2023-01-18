import pandas as pd
from Bio import pairwise2

# Read the CSV file into a dataframe
df = pd.read_csv("filename2nd.csv")

# Extract the sequences from the dataframe
sequences = df['Seq'].tolist()

print(sequences)

# globalxx - matches score 1, mismatches 0 and no gap penalty.
alignments = pairwise2.align.globalxx(sequences[0], sequences[1])
for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))