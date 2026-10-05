# Simple script for DNA sequence quality control

def analyze_dna(sequence_id, sequence):
    # Convert everything to uppercase for consistency
    sequence = sequence.upper()

    # 1. Calculate the length of the sequence
    length = len(sequence)

    # 2. Count the number of C and G bases
    c_count = sequence.count('C')
    g_count = sequence.count('G')

    # 3. Calculate GC content of sequences, answer depends on sequence length (percentage of G and C)
    gc_content = ((c_count + g_count) / length) * 100
    if length >= 200:
        status_message = "Status: OK"
    elif length <200 and length >50:
        status_message = "Status: sequence is too short or aborted, GC content is calculated anyways"

    else:
        gc_content = 0.0
        status_message = "no GC content available"

    # Print results®
    print(f"--- DNA Quality Report ---")
    print(f"ID: {sequence_id}")
    print(status_message)
    print(f"Sequence length: {length} base pairs")
    print(f"GC content: {gc_content:.2f}%")
    print(f"Sequence: {sequence[:19]}") #show only the first 20 bases of the sequence -> check if sequence is correct


# Test the function with a sample sequence
sequence_id = "ID_001"
test_dna = "AGTC"*20
analyze_dna(sequence_id, test_dna)