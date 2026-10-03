#  InterPro Domain Analysis: Human p53 (UniProt P04637)

## Objective
Identify the conserved domains and functional regions of human p53 using InterPro, and link them to the conservation pattern seen in the multiple sequence alignment.

## Method
1. Opened InterPro (EMBL-EBI) and searched with UniProt accession **P04637** (393 aa).
2. Reviewed the domain architecture view, the member-database signatures (Pfam among them) and the residue ranges.
3. Compared the domain boundaries with the conserved region from the Clustal Omega alignment.

## Domains Identified

| Region | Approx. residues | InterPro / Pfam entry | Function |
|---|---|---|---|
| Transactivation domain | [e.g. 1–40] | [InterPro ID / Pfam ID] | Binds the transcriptional machinery and MDM2 |
| DNA-binding core domain | [e.g. 102–292] | [InterPro ID / Pfam ID] | Sequence-specific DNA binding |
| Tetramerization domain | [e.g. 325–356] | [InterPro ID / Pfam ID] | Assembly of p53 into tetramers |

*Copy the exact accession numbers and residue ranges from your InterPro results page. Boundaries differ slightly between member databases, so write the ranges as reported, not rounded.*

## Key Observations
- The DNA-binding core domain overlaps the region that stayed gap-free across all five species in the alignment, which fits strong functional constraint.
- The N-terminal and C-terminal regions are more variable, which is consistent with them being less structurally constrained.
- [Add anything else you noticed, such as a protein family entry, GO terms shown by InterPro, or disordered regions.]


## What I Learned
- InterPro combines signatures from several databases into one view, so it can be cross-checked against Pfam directly.
- Domain boundaries are predictions, and member databases don't always agree on exact positions.
- Linking domain position to alignment conservation gives a stronger argument than either alone.

## Limitations
- InterPro predicts domains from sequence signatures. This project did not use experimental structure data.
- Conservation was measured on only five species.

## Links
- InterPro: https://www.ebi.ac.uk/interpro/
- UniProt P04637: https://www.uniprot.org/uniprotkb/P04637
