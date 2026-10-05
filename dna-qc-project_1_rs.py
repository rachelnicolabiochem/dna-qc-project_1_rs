# Simple script for DNA sequence quality control

def analyze_dna(sequence):
    # Convert everything to uppercase for consistency
    sequence = sequence.upper()
    
    # 1. Calculate the length of the sequence
    length = len(sequence)
    
    # 2. Count the number of C and G bases
    c_count = sequence.count('C')
    g_count = sequence.count('G')
    
    # 3. Calculate GC content (percentage of G and C)
    if length > 0:
        gc_content = ((c_count + g_count) / length) * 100
    else:
        gc_content = 0.0
        
    # Print results
    print(f"--- DNA Quality Report ---")
    print(f"Sequence: {sequence}")
    print(f"Sequence length: {length} base pairs")
    print(f"GC content: {gc_content:.2f}%")

# Test the function with a sample sequence
test_dna = "ATCGATCGATCGTACGATCG"
analyze_dna(test_dna)
