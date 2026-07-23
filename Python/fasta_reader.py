# Script to simulate reading a FASTA file layout string
fasta_data = """>insulin_sequence
AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGC"""

lines = fasta_data.split("\n")

for line in lines:
    if line.startswith(">"):
        print(f"Header Found: {line[1:]}")
    else:
        print(f"Sequence Length: {len(line)} bases long")
