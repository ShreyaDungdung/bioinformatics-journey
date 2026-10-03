#  Mini Project 2: Disease Gene Analysis of TP53

An end-to-end, sequence-to-network bioinformatics workflow exploring the evolutionary, structural and interaction biology of the human tumor suppressor gene **TP53**, the *"Guardian of the Genome."*

This project shows how conserved sequence features, protein domains and interaction networks help explain why variation in this gene is so strongly linked to cancer.

---

##  Objectives
- **Pipeline integration:** Chain NCBI, UniProt, BLAST, Clustal Omega, InterPro, Pfam, Gene Ontology and STRING into one analytical workflow.
- **Evolutionary and structural mapping:** Measure sequence conservation across vertebrates and map functional protein domains.
- **Biological interpretation:** Move from collecting database records to interpreting what they mean for protein function and cancer biology.

---

##  Workflow

```text
  [ Sequence Retrieval ] ──► [ Similarity Search ] ──► [ Multiple Alignment ]
     (NCBI, UniProt)           (BLASTn, BLASTp)          (Clustal Omega)
                                                                │
                                                                ▼
  [ Interaction Network ] ◄── [ Gene Ontology ] ◄── [ Domain Identification ]
        (STRING)                (GO terms)             (InterPro, Pfam)
```

---

##  Tools Used
| Step | Tool / Database |
|---|---|
| Sequence retrieval | NCBI, UniProt |
| Similarity search | BLASTn, BLASTp |
| Multiple alignment & tree | Clustal Omega (Neighbor-Joining) |
| Domains | InterPro, Pfam |
| Functional annotation | Gene Ontology |
| Interactions | STRING |
| Scripting | Python (`analyze_fasta.py`) |

---

##  Results by Phase

### Phase 1: Sequence Retrieval and Inspection (`Data/`, `Scripts/`)
- Retrieved the human TP53 reference transcript `NM_000546.6` (2,512 bp) and TP53 protein sequences from five species: human (`P04637`), chimpanzee (`P13481`), mouse (`P02340`), cow (`P53028`) and zebrafish (`O42344`).
- Wrote a standalone Python script (`analyze_fasta.py`, no external dependencies) that parses FASTA headers and reports sequence length, GC content and residue composition.

### Phase 2: Similarity Search and Evolutionary Conservation (`BLAST/`, `Alignment/`, `Phylogeny/`)
- Ran BLAST pairwise local alignments and a Clustal Omega multiple sequence alignment across the five species.
- **Findings:**
  - The chimpanzee protein is over 98% identical to human.
  - The central core region (residues 102–292) has no gaps across all species tested, consistent with strong negative (purifying) selection.
  - The Neighbor-Joining tree groups the mammals together and places zebrafish (*Danio rerio*) as the outgroup, matching known vertebrate evolution.

### Phase 3: Domains and Functional Annotation (`Domains/`, `GO/`)
- Used Pfam/InterPro to identify functional regions, then linked them to Gene Ontology terms.
- **Findings:**
  - **Transactivation domain:** residues 1–40
  - **DNA-binding core domain:** residues 102–292
  - **Tetramerization domain:** residues 325–356
  - The DNA-binding core maps to sequence-specific DNA-binding transcription factor activity (`GO:0003700`) in the nucleus (`GO:0005634`).
- **Context from the literature:** Most cancer-associated TP53 mutations are reported in the DNA-binding domain, which fits the conservation pattern seen in Phase 2. This project did not analyse patient variant data directly.

### Phase 4: Protein Interaction Network (`STRING/`)
- Queried STRING for the immediate interaction partners of p53.
- **Findings:**
  - Interactors include damage-signalling proteins (**ATM, CHEK2**), a repair-associated protein (**BRCA1**) and the main negative regulator (**MDM2**).
  - The MDM2–p53 interaction is a known target for small-molecule inhibitors in cancer research.

---

## 💡 Key Takeaway
Bioinformatics is more than running tools. Combining retrieval, alignment, domain mapping and network analysis lets you build a coherent biological story about one gene, and see why a conserved region matters for disease.

