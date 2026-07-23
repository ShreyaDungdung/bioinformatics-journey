# Script to translate an RNA codon to an amino acid
# AUG is the standard start codon for translation
rna_codon = "AUG"

codon_table = {
    "AUG": "Methionine (Start)",
    "UUU": "Phenylalanine",
    "UUA": "Leucine",
    "GGU": "Glycine"
}

if rna_codon in codon_table:
    protein = codon_table[rna_codon]
    print(f"Codon: {rna_codon} translates to -> {protein}")
else:
    print(f"Codon {rna_codon} not found in this basic table.")
