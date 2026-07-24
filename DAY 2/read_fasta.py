with open("insulin.fasta") as file:
    for line in file:
        if not line.startswith(">"):
            print(line.strip())
