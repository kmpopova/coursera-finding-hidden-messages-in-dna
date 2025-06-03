"""
Code Challenge: Implement MotifEnumeration (reproduced below).

Input: Integers k and d, followed by a space-separated collection of 
strings Dna.

Output: All (k, d)-motifs in Dna.

MotifEnumeration(Dna, k, d)
    Patterns ← an empty set
    for each k-mer Pattern in Dna
        for each k-mer Pattern’ differing from Pattern by at most d mismatches
            if Pattern' appears in each string from Dna with at most d mismatches
                add Pattern' to Patterns
    remove duplicates from Patterns
    return Patterns
"""

"""
REASONING:
For a given DNA string, we have many kmers, each of which also 
has a d-neighbourhood of kmers. The union of these sets of d-neighbourhoods 
is the set of kmers which are in the d-neighbourhood for at least one kmer 
in that DNA string.

Considering this set for each DNA string in the collection, we are 
interested in the kmers which appear in the set for every DNA string 
(i.e. the intersection of the sets for each DNA string). 
These will be the kmers which are in the d-neighbourhood for at least 
one kmer from every DNA string, i.e. the (k,d)-motifs we are searching for.
"""
from helper_functions import neighbors

def motif_enumeration(dna: list, k: int, d: int) -> set:
    # Following the logic suggested by Ben Parker on the forum
    
    # collect neighborhood for each string in one place
    full_neighborhood = [] # will be a list of sets
    for sequence in dna:
        sequence_neighborhood = set()
        for i in range(len(sequence)-k+1):
            pattern = sequence[i:i+k]
            pattern_neighbors = neighbors(pattern, d)
            for pattern_neighbor in pattern_neighbors:
                sequence_neighborhood.add(pattern_neighbor)
        full_neighborhood.append(sequence_neighborhood)
        
    # Initialise an intersection as first set among all sets
    intersection_of_neighborhoods = full_neighborhood[0]
    for x in range(1, len(full_neighborhood)):
        intersection_of_neighborhoods = intersection_of_neighborhoods & full_neighborhood[x]
    
    return intersection_of_neighborhoods





if __name__ == "__main__":
    output_set = motif_enumeration(["AGGAAAATGCAACTACAATAACGGC", \
                                    "TTCAATTAGTTTTCGCACTATCCCT", \
                                        "GCACTCAGTAGAGTAATAAACCGTG", \
                                            "AGGTGCTTGACAGTAACAGGAGGTG", \
                                                "GGCCCTCAATCAGTACTTTCAAGCC", \
                                                    "AAAAAATCCGGTAAGGACACCAGTA"], 5, 1)
    output_str = ""
    for element in output_set:
        output_str += element + " "
    print(output_str.strip())
    
    # Output: AAGTA CATTA CAGTA AATAA CAATA CACTA