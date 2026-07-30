# BLAST Analysis Summary
This directory documents the local alignment database searches performed to investigate the sequence conservation of the Human Insulin (`INS`) gene and protein across vertebrate lineages.

## Part 1: Nucleotide BLAST (BLASTn) Analysis
* **Query Sequence:** Human Insulin (*Homo sapiens*) mRNA (`NM_000207.3`)
* **Database / Program:** `core_nt` / Megablast (Highly similar sequences)
* **Raw Data Reference:** `dna_blast_results.txt`

### Analytical Questionnaire:
* **What organism gives the best hit?**
  * Excluding the 100% self-match to *Homo sapiens*, the top animal matches belong to non-human higher primates like ***Pan troglodytes* (Chimpanzee)** and ***Pan paniscus* (Bonobo)**.
* **Identity:** `98.28%` to `100.00%` (depending on the specific evolutionary transcript variant matched).
* **Query Coverage:** `100%` (The alignment length spans all 465 nucleotides of the input query sequence).
* **E-value:** `0.0` (Statistically absolute match; zero possibility that this sequence similarity occurred by random chance).

## Part 2: Protein BLAST (BLASTp) Analysis
* **Query Sequence:** Human Insulin (*Homo sapiens*) Precursor Protein (`P01308`)
* **Database / Program:** `nr` / BLASTp (Protein-protein BLAST)
* **Raw Data Reference:** `protein_blast_results.txt`

### Comparative Sequence Conservation Metrics:
The table below tracks how effectively the human master insulin protein query aligns with the specific comparative target species investigated in this research project:

| Organism Taxonomy | Common Name | Accession ID | Query Coverage | E-Value | Percent Identity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *Pan troglodytes* | Chimpanzee | `P61899.1` | 100% | 6.0e-75 | 100.00% |
| *Bos taurus* | Cow | `P01317.1` | 100% | 1.0e-61 | 83.64% |
| *Mus musculus* | Mouse | `P01309.1` | 100% | 4.0e-60 | 82.73% |
| *Danio rerio* | Zebrafish | `O73727.1` | 98% | 2.0e-33 | 47.22% |

## 🔬 Core Biological Insights
* **Primate Lineage Conservation:** The 100% sequence identity between human and chimpanzee insulin proteins indicates strict evolutionary constraints, showing no amino acid deviations since divergence.
* **Evolutionary Gradient:** Sequence identity declines uniformly with increasing evolutionary distance from mammals down to teleost fish (*Zebrafish* at 47.22%).
* **Functional Integrity:** Despite the sequence mutations found in more distant species, all E-values remain functionally near zero, showing that the core structural shape of the insulin molecule remains intact across species lines.
