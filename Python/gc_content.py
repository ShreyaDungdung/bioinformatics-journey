dna="ATGCGATCGAA"
g=dna.count("G")
c=dna.count("C")
gc=g=c
length=len(dna)
gc_present=(gc/length)*100
print("GC content=",gc_present)
