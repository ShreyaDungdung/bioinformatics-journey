def analyze_nucleotides(fasta_file_path):
    """
    Reads a FASTA file, calculates the frequency of each nucleotide, 
    and determines the overall GC content percentage.
    """
    sequence = ""
    header = ""

    # Step 1: Open and parse the FASTA file safely
    try:
        with open(fasta_file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith(">"):
                    header = line  # Save the FASTA header record
                else:
                    sequence += line.upper()  # Consolidate sequence lines in uppercase
    except FileNotFoundError:
        return f"Error: The file at {fasta_file_path} was not found."

    # Step 2: Clean the sequence string to ensure accuracy
    # Removes any whitespace or accidental newlines inside the file text
    sequence = "".join(sequence.split())
    total_length = len(sequence)

    if total_length == 0:
        return "Error: The sequence file is empty."

    # Step 3: Count individual nucleotide frequencies
    counts = {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C')
    }

    # Step 4: Calculate biological metrics
    gc_count = counts['G'] + counts['C']
    gc_percentage = (gc_count / total_length) * 100

    # Step 5: Format and present the metrics clearly
    print("=" * 60)
    print(f"🧬 BIOINFORMATICS REPORT: NUCLEOTIDE ANALYSIS")
    print("=" * 60)
    print(f"Target Record : {header}")
    print(f"Total Sequence Length : {total_length} base pairs\n")
    
    print(f"📊 Nucleotide Counts:")
    for base, count in counts.items():
        percentage = (count / total_length) * 100
        print(f"  - {base}: {count} ({percentage:.2f}%)")
        
    print(f"\n🧪 Thermal Stability Metric:")
    print(f"  - Total GC Content: {gc_percentage:.2f}%")
    print("=" * 60)

# Run the program against your local human insulin data file path
if __name__ == "__main__":
    # Adjust this path depending on where you execute your python environment
    file_path = "../Data/human_insulin_dna.fasta"
    analyze_nucleotides(file_path)
