#  Structural Analysis of the Glu6Val Mutation in Hemoglobin

### A PyMOL-based comparison of normal hemoglobin (HbA) and sickle hemoglobin (HbS)

---

##  Overview

Sickle cell disease is associated with a single amino acid substitution in the β-chain of hemoglobin: **glutamic acid (Glu6) is replaced by valine (Val6)**.

Although this is a single-residue change, the difference in the chemical properties of these amino acids has important structural consequences.

In this mini-project, I used experimentally determined protein structures from the **RCSB Protein Data Bank (PDB)** and **PyMOL** to visualize and compare the β6 mutation in normal hemoglobin and sickle hemoglobin.

The analysis focuses on:

- Overall hemoglobin structure
- Identification of the β6 residue
- Comparison of Glu6 and Val6
- Local structural environment around the mutation
- Structural interpretation of the Glu6 → Val6 substitution

---

##  Objective

To investigate the structural difference between normal hemoglobin (HbA) and sickle hemoglobin (HbS) by:

1. Visualizing their three-dimensional structures.
2. Identifying the β-chain residue at position 6.
3. Comparing **Glu6 in HbA** with **Val6 in HbS**.
4. Examining the local environment surrounding the mutation.
5. Relating the structural difference to the known molecular basis of HbS polymerization.

---

##  Biological Background

Hemoglobin is a tetrameric protein responsible for transporting oxygen in red blood cells.

Normal adult hemoglobin (HbA) consists of:

**α₂β₂**

The β-chain normally contains **glutamic acid at position 6 (β6 Glu)**.

In sickle hemoglobin (HbS), this residue is replaced by **valine**:

**β6 Glu → β6 Val**

This substitution changes the chemical character of the side chain:

| Property | Glu6 | Val6 |
|---|---|---|
| Amino acid | Glutamic acid | Valine |
| One-letter code | E | V |
| Side-chain character | Charged/polar | Non-polar/hydrophobic |
| Charge at physiological pH | Negative | Neutral |
| Side-chain type | Carboxylate-containing | Branched hydrocarbon |

The change from a negatively charged residue to a hydrophobic residue is central to understanding the molecular behavior of HbS.

---

#  Structures Used

| Structure | PDB ID | Description |
|---|---|---|
| Normal hemoglobin | **2HHB** | Human deoxyhemoglobin |
| Sickle hemoglobin | **2HBS** | Deoxyhemoglobin S |

The 2HHB structure is an experimentally determined human deoxyhemoglobin structure solved by X-ray diffraction at 1.74 Å resolution. The entry contains α- and β-chain components of the hemoglobin tetramer. 

The 2HBS structure is a high-resolution crystal structure of deoxyhemoglobin S. It specifically represents the **β Glu6 → Val mutation** and provides structural information about the intermolecular contacts associated with HbS polymerization. 

---

#  Tools & Resources

### Software

- **PyMOL** — protein structure visualization and structural analysis

### Database

- **RCSB Protein Data Bank (RCSB PDB)**

### Structures

- **2HHB** — normal human deoxyhemoglobin
- **2HBS** — sickle hemoglobin

---

#  Methodology

The analysis was performed using the following workflow:

```text
RCSB Protein Data Bank
          ↓
Download 2HHB and 2HBS structures
          ↓
Open structures in PyMOL
          ↓
Visualize overall hemoglobin structure
          ↓
Identify β-chain residue 6
          ↓
Highlight Glu6 in HbA
          ↓
Highlight Val6 in HbS
          ↓
Visualize surrounding residues
          ↓
Compare local structural environments
          ↓
Interpret structural significance
