# BRCA1 Protein Sequence Analysis Using BLAST

## Overview

This project presents a comparative protein sequence analysis of the **Breast Cancer Type 1 Susceptibility Protein (BRCA1)** in three primate species.

The analysis was performed using protein sequences obtained from the **NCBI Protein database** and compared using **NCBI BLASTP**.

The three species analyzed were:

- *Pan troglodytes* — Chimpanzee
- *Gorilla gorilla gorilla* — Gorilla
- *Pongo abelii* — Sumatran orangutan

The purpose of the analysis was to investigate the sequence conservation of BRCA1 among these three closely related primate species.

---

## Objectives

1. Obtain BRCA1 protein sequences from NCBI.
2. Perform BLAST protein sequence analysis.
3. Identify homologous BRCA1 sequences.
4. Compare sequence identity and similarity between the selected species.
5. Analyze BLAST alignment scores, E-values, and gaps.
6. Determine the degree of BRCA1 sequence conservation among the three species.

---

## Protein Sequences

| Species | Protein Accession | Protein Length |
|---|---|---:|
| *Pan troglodytes* (Chimpanzee) | Q9GKK8.2 | 1863 aa |
| *Gorilla gorilla gorilla* (Gorilla) | Q6J6I8.1 | 1863 aa |
| *Pongo abelii* (Sumatran orangutan) | XP_003778880.3 | 1863 aa |

All three analyzed BRCA1 proteins contain **1863 amino acids**.

---

## BLAST Results

| Species | Accession | Identity | Positives | Gaps | Bit Score | E-value |
|---|---|---:|---:|---:|---:|---:|
| Chimpanzee | Q9GKK8.2 | 1834/1863 (98%) | 1842/1863 (98%) | 0/1863 (0%) | 3773 bits | 0.0 |
| Gorilla | Q6J6I8.1 | 1826/1863 (98%) | 1840/1863 (98%) | 0/1863 (0%) | 3757 bits | 0.0 |
| *Pongo abelii* | XP_003778880.3 | 1804/1863 (97%) | 1823/1863 (97%) | 0/1863 (0%) | 3700 bits | 0.0 |

---

## Results and Interpretation

The BLAST analysis showed a very high degree of conservation of the BRCA1 protein among the three selected primates.

The chimpanzee sequence showed **98% identity**, with 1834 identical residues out of 1863. The gorilla sequence also showed **98% identity**, with 1826 identical residues. The Sumatran orangutan sequence showed **97% identity**, with 1804 identical residues.

All three alignments covered the complete 1863-amino-acid sequence and contained **0 gaps**. The E-value was **0.0** for all three results, indicating extremely significant sequence similarity.

The high percentage of identical and positive residues suggests that BRCA1 is highly conserved among these primate species.

The chimpanzee result had the highest reported bit score (**3773 bits**), followed by gorilla (**3757 bits**) and *Pongo abelii* (**3700 bits**).

Overall, the results demonstrate strong evolutionary conservation of BRCA1 among chimpanzee, gorilla, and Sumatran orangutan.

---

## Screenshots

BLAST result screenshots are provided in the `blast_results/` directory.

### Chimpanzee

![Chimpanzee BLAST Result](blast_results/chimpanzee_blast.png)

### Gorilla

![Gorilla BLAST Result](blast_results/gorilla_blast.png)

### Sumatran Orangutan

![Pongo abelii BLAST Result](blast_results/pongo_abelii_blast.png)

---

## Files and Directory Structure

```text
BRCA1-BLAST-Analysis/
│
├── README.md
├── report/
│   └── BRCA1_BLAST_Analysis_Report.pdf
│
├── sequences/
│   ├── chimpanzee_Q9GKK8.2.fasta
│   ├── gorilla_Q6J6I8.1.fasta
│   └── pongo_abelii_XP_003778880.3.fasta
│
├── blast_results/
│   ├── chimpanzee_blast.png
│   ├── gorilla_blast.png
│   └── pongo_abelii_blast.png
│
└── results/
    └── blast_results_summary.csv
```

---

## Database and Tool

**Database:** NCBI Protein Database

**Sequence similarity tool:** NCBI BLASTP

**Protein analyzed:** Breast Cancer Type 1 Susceptibility Protein (BRCA1)

---

## Conclusion

The comparative BLAST analysis demonstrates that BRCA1 protein sequences are highly conserved among chimpanzee, gorilla, and Sumatran orangutan. Sequence identities of **97–98%**, absence of alignment gaps, and E-values of **0.0** indicate strong sequence conservation and highly significant homology among the analyzed proteins.

This analysis illustrates the use of sequence databases and BLAST for comparative protein sequence analysis in bioinformatics.

---

## References

1. National Center for Biotechnology Information (NCBI), Protein Database.
2. NCBI BLAST — Basic Local Alignment Search Tool.
3. NCBI Protein accession Q9GKK8.2 — *Pan troglodytes* BRCA1 homolog.
4. NCBI Protein accession Q6J6I8.1 — *Gorilla gorilla gorilla* BRCA1 homolog.
5. NCBI Protein accession XP_003778880.3 — *Pongo abelii* BRCA1 isoform X1.
