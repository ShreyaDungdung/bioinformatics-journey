#  Structural Comparison of Normal and Sickle Cell Hemoglobin

### A molecular visualization study of the β6 Glu→Val substitution associated with sickle hemoglobin

[![Tool](https://img.shields.io/badge/Tool-PyMOL-blue)]
[![Database](https://img.shields.io/badge/Database-RCSB%20PDB-green)]
[![Field](https://img.shields.io/badge/Field-Structural%20Bioinformatics-purple)]

---

> Exploring how a single amino-acid substitution can be investigated at the three-dimensional structural level.


##  Project Overview

Sickle cell disease is associated with a single amino-acid substitution in the
β-globin chain of hemoglobin: glutamic acid (Glu) at position 6 is replaced
by valine (Val).

In this project, I used molecular visualization and structural analysis to
examine this substitution in three dimensions.

The analysis was performed using PyMOL and experimentally determined protein
structures obtained from the Protein Data Bank (PDB).

Rather than focusing only on the sequence-level mutation, this project explores
the structural environment surrounding the substituted residue.

##  Research Question

**How can the β6 Glu→Val substitution associated with sickle hemoglobin
be visualized and examined at the protein-structure level?**


##  Objectives

- Visualize the three-dimensional structure of normal hemoglobin.
- Identify the β-globin chain.
- Locate residue 6 within the β-globin chain.
- Visualize Glu6 in normal hemoglobin.
- Visualize Val6 in the HbS structure.
- Examine the local structural environment surrounding the substituted residue.
- Compare the two residue environments using molecular visualization.


  ##  Workflow

```text
PDB structure retrieval
        ↓
Structure preparation
        ↓
Load structures into PyMOL
        ↓
Identify β-globin chain
        ↓
Locate residue 6
        ↓
Visualize Glu6 / Val6
        ↓
Examine local environment
        ↓
Compare structures
        ↓
Generate final figures


````
## **Structural Analysis**

### Normal Hemoglobin

The normal hemoglobin structure was visualized using a cartoon representation
to examine its overall three-dimensional organization.

The β-globin chain was then isolated for residue-level analysis.

![Normal Hemoglobin](https://github.com/ShreyaDungdung/bioinformatics-journey/blob/76a7fdd6cd40026e0306fc5a727dd56d26144c7b/Hemoglobin_structure_analysis/2HHB_initial_structure.png.png)


### Glu6 in Normal Hemoglobin

Residue 6 of the β-globin chain was examined and identified as glutamic acid
(Glu6).

The residue was displayed using a stick representation to make its local
structural environment easier to inspect.

![Glu6 Environment](https://github.com/ShreyaDungdung/bioinformatics-journey/blob/9cc48dba10f1f7e0e8c57a2bbca6c0593e93b57b/Hemoglobin_structure_analysis/HBA_GLU6.png)


### Val6 in HbS

The corresponding position in the HbS structure contains valine (Val6).

The residue was visualized in PyMOL and examined together with its surrounding
structural environment.

![Val6 Environment](https://github.com/ShreyaDungdung/bioinformatics-journey/blob/d1ab84264ab45a7e146a8a4a843d790e7dd4df3a/Hemoglobin_structure_analysis/HBS_VAL6.png)


##  Glu6 vs Val6

| Feature | Normal Hemoglobin | HbS |
|---|---|---|
| β-globin position | 6 | 6 |
| Amino acid | Glutamic acid | Valine |
| Three-letter code | GLU | VAL |
| Residue type | Charged/polar | Nonpolar |
| Analysis | Structural visualization | Structural visualization |


![Glu6 vs Val6](https://github.com/ShreyaDungdung/bioinformatics-journey/blob/9b843263e18940e59bb9baffc3180ac075c85896/Hemoglobin_structure_analysis/Glu6_vs_Val6_comparison.png)


## Key Findings

1. The β6 position differs between the two hemoglobin forms examined.

2. Normal hemoglobin contains **Glu6** at the β-globin position 6.

3. HbS contains **Val6** at the corresponding position.

4. PyMOL allowed the substituted residues to be visualized directly within
   their three-dimensional structural environments.

5. The Glu→Val substitution represents a change from a charged/polar residue
   to a nonpolar residue, providing a structural basis for investigating how
   a single sequence change can alter the molecular environment.


The observed substitution is associated with the molecular basis of sickle
cell disease. This project focuses specifically on visualizing and comparing
the structural context of the β6 residue rather than experimentally
demonstrating the mechanism of hemoglobin polymerization.


##  Skills Demonstrated

### Structural Bioinformatics
- Protein structure visualization
- Residue-level structural analysis
- Chain and residue selection
- Structural comparison
- Molecular visualization

### Computational Skills
- Working with PDB structural data
- PyMOL command-line operations
- Creating reproducible visualization workflows
- Preparing scientific figures

### Scientific Communication
- Translating structural observations into biological context
- Documenting computational workflows
- Presenting results using figures and tables


##  Limitations

This project is primarily a structural visualization study.

It does not include:

- Molecular dynamics simulations
- Energy calculations
- Quantitative binding analysis
- Experimental validation
- Direct measurement of HbS polymerization

Therefore, the structural observations should be interpreted as
visualization-based observations rather than experimental evidence of
functional effects.


##  Future Work

Possible extensions of this project include:

- Structural superposition of normal Hb and HbS
- Quantitative measurement of residue distances
- Surface-property analysis around the β6 site
- Investigation of intermolecular contacts
- Analysis of HbS polymerization interfaces
- Molecular dynamics simulations
- Comparison of additional hemoglobin variants
