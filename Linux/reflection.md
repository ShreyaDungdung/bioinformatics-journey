# Linux Reflection Questions

### 1. Why is Linux preferred for bioinformatics research?
Almost all professional bioinformatics software (like BWA, SAMtools, and GATK) is built exclusively for Linux. Linux handles massive next-generation sequencing data much faster, handles memory efficiently, and powers the High-Performance Computing (HPC) clusters used in research labs.

### 2. What's the difference between `cp` and `mv`?
- `cp` creates an identical copy of a file in a new location, leaving the original file completely untouched.
- `mv` shifts the original file to a new location or changes its name, meaning the original file disappears from its old location.

### 3. When would `head` be more useful than opening a file in a text editor?
Genomic sequencing files (like FASTQ or FASTA) can be gigabytes in size. Opening them in a regular text editor would crash the computer. `head` lets you check the file format or quality control metrics instantly by printing just the first few lines without loading the whole file into memory.

### 4. Why is `grep` especially valuable when working with biological data?
`grep` allows you to instantly search through millions of lines of sequence data to find specific sequence patterns (like a start codon `ATG`), restriction sites, or specific gene ID headers without manual looking.

### 5. What precautions should you take before using `rm`?
Linux does not have a "Recycle Bin." Once you run `rm`, the file is permanently gone. You should always double-check your current location with `pwd` and use `ls` to ensure you are deleting the correct file.
