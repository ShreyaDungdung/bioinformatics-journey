# Bioinformatics Journey

> **From learning the basics of bioinformatics to building my first end-to-end analyses.**

Hi! I'm Shreya, a final-year B.Sc. Biotechnology (Honours) student exploring the intersection of biology, programming, and computational analysis.

This repository documents my hands-on journey into bioinformatics — from understanding biological databases and writing my first Python programs to performing sequence analysis, phylogenetics, protein-structure analysis, and disease-gene investigation.

I'm learning by understanding concepts, applying them to biological data, building small projects, and documenting what I learn along the way.

---

## What I'm Learning

* Bioinformatics fundamentals
* Python for biological data
* Linux & command-line basics
* Biological databases
* Sequence analysis
* BLAST & sequence similarity
* Multiple sequence alignment
* Phylogenetic analysis
* Protein structure & visualization
* Protein domains & functional annotation
* Protein-protein interaction networks
* Gene Ontology analysis
* RNA & gene expression concepts
* Scientific literature analysis
* Biopython & computational workflows

---

# My Learning Journey

### Week 1 — Building the Foundation

| Day       | Focus                             | What I Worked On                                                                                                           |
| --------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Day 1** |  Bioinformatics Foundations     | Introduction to bioinformatics, its applications, history, biological data, NCBI and UniProt, and my first Python program. |
| **Day 2** |  Biological Databases + Python | Primary and secondary databases, GenBank, EMBL, UniProt and working with FASTA files using Python/Biopython.               |
| **Day 3** |  Linux & Bash                   | Linux fundamentals, file systems, directories, basic Bash commands and why Linux is important in bioinformatics.           |
| **Day 4** |  Sequence Alignment & BLAST     | Pairwise alignment, global vs local alignment, BLASTn and BLASTp, and interpreting sequence-similarity results.            |
| **Day 5** |  Multiple Sequence Alignment    | Multiple sequence alignment, conserved regions, sequence variation and practical analysis using Clustal Omega.             |
| **Day 6** |  Phylogenetics                  | Evolutionary relationships, phylogenetic terminology and construction/interpreting my first phylogenetic tree.             |
| **Day 7** |  Protein Structure              | From DNA → RNA → protein → 3D structure; explored human insulin structure using PyMOL and PDB data.                        |

---

### Week 2 — Applying the Concepts

| Day        | Focus                            | What I Worked On                                                                                                                 |
| ---------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Day 8**  |  Mini Project 1                | **Comparative analysis of human insulin** — sequence retrieval → BLAST → MSA → phylogeny → protein structure → Python analysis.  |
| **Day 9**  |  Genomic Organization          | Genome, chromosomes, gene loci, exons, introns, transcripts and isoforms.                                                        |
| **Day 10** |  PCR & Molecular Biology       | PCR fundamentals, thermal cycling, primers, amplification and the connection between wet-lab biology and computational analysis. |
| **Day 11** |  Protein Domains               | Protein domains, motifs, functional regions and domain analysis using **InterPro**.                                              |
| **Day 12** |  Gene Expression & RNA-Seq     | Gene expression, central dogma, RNA-Seq concepts and basic Python data visualization.                                            |
| **Day 13** |  Mini Project 2                | Began a **TP53 disease-gene analysis**, combining sequence, evolutionary and functional information.                             |
| **Day 14** |  Protein Interaction Networks | Protein-protein interactions, interactomes and visualization/analysis of the TP53 network using **STRING**.                      |

---

### Week 3 — Functional & Research-Level Analysis

| Day        | Focus                  | What I Worked On                                                                                                                          |
| ---------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Day 15** |  Gene Ontology       | Molecular Function, Biological Process and Cellular Component; performed GO analysis of TP53.                                             |
| **Day 16** |  RNA Structure       | DNA vs RNA, RNA folding and secondary-structure prediction using RNAfold.                                                             |
| **Day 17** |  Scientific Research | Learned how to read and analyse bioinformatics research papers, including datasets, methods, results, limitations and scientific writing. |
| **Day 18** |  Entrez & Automation | Learned about NCBI Entrez, programmatic data retrieval and how Biopython can automate biological sequence workflows.                      |

---

#  Projects

##  Mini Project 1 — Comparative Analysis of Human Insulin

**Goal:** Investigate the evolutionary conservation and structural characteristics of human insulin across different species.

### Workflow

```text
Sequence Retrieval
       ↓
BLASTn / BLASTp
       ↓
Multiple Sequence Alignment
       ↓
Phylogenetic Analysis
       ↓
Protein Structure Analysis
       ↓
Python Sequence Analysis
       ↓
Biological Interpretation
```

### Tools Used

`NCBI` · `UniProt` · `BLAST` · `Clustal Omega` · `PDB` · `PyMOL` · `Python`

[→ View Mini Project 1](./Projects/Mini_Project_01_Insulin/)

---

##  Mini Project 2 — Disease Gene Analysis: TP53

**Goal:** Explore the human TP53 gene and protein through multiple computational perspectives.

### Analysis Pipeline

```text
Sequence Retrieval
       ↓
BLAST
       ↓
Multiple Sequence Alignment
       ↓
Phylogenetic Analysis
       ↓
Protein Domain Analysis
       ↓
Gene Ontology
       ↓
Protein Interaction Network
       ↓
Biological Interpretation
```

### Tools & Databases

`NCBI` · `UniProt` · `BLAST` · `Clustal Omega` · `InterPro` · `Pfam` · `Gene Ontology` · `STRING`

[→ View Mini Project 2](./Projects/Mini_Project_02_Disease%20Gene%20Analysis/)

---

#  Python Practice

I'm using Python as a tool for solving biological problems rather than learning programming in isolation.

Some of my current scripts include:

* FASTA file reading
* DNA sequence manipulation
* GC-content calculation
* DNA → protein translation
* Nucleotide counting
* Sequence analysis
* Basic data visualization
* Biopython-based workflows

[→ Explore Python practice](./Python/)

---

#  Sequence Data

I've also started building a small collection of biological sequences for practice and analysis.

Current examples include:

* **INS** — Insulin
* **TP53**
* **BRCA1**

[→ Explore sequences](./Sequences/)

---

#  How I'm Learning

My approach is:

**Learn → Practice → Analyze → Build → Document → Reflect**

Rather than collecting tools or certificates, I'm trying to understand:

* What biological question am I solving?
* What kind of data am I working with?
* Why is a particular tool appropriate?
* What does the output actually mean?
* How can the analysis be reproduced or improved?

---
## 🔬 Featured Project

### TEM Beta-Lactamase Sequence Analysis
A comparative bioinformatics project exploring selected TEM-type beta-lactamase gene sequences.

**What I explored:**
- Nucleotide sequence retrieval using NCBI
- Multiple sequence alignment with Clustal Omega
- Pairwise sequence identity using Python and Biopython
- Phylogenetic tree construction
- Nucleotide and amino acid variation analysis

**Tech stack:** Python · Biopython · Pandas · NCBI · Clustal Omega

🔗https://github.com/ShreyaDungdung/bioinformatics-journey/tree/03ba6fe907459c96c4d558bea6e0d4e54a539e0f/tem-beta-lactamase-sequence-analysis

##  My Approach
I focus on understanding the concepts behind the tools, applying them to biological data, and documenting what I learn through practical projects.

---

#  Current Direction

I'm gradually moving from a **biotechnology background toward bioinformatics and computational biology**.

My current areas of interest include:

**Sequence Analysis • Genomics • Computational Biology • Biological Data Analysis • Python • Biotech Data Applications**

This repository will continue to grow as I work on more complex datasets, improve my programming skills, and build larger projects.

---

### ⭐ If you're also learning bioinformatics

Feel free to explore the repository, follow the journey, or connect with me on [LinkedIn](https://www.linkedin.com/in/shreyadungdung).
