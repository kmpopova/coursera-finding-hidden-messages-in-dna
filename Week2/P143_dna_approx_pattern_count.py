"""
Our goal now is to modify our previous algorithm for the Frequent Words Problem 
in order to find DnaA boxes by identifying frequent k-mers, possibly with 
mismatches. Given strings Text and Pattern as well as an integer d, 
we define Countd(Text, Pattern) as the total number of occurrences of 
Pattern in Text with at most d mismatches. 

For example, Count1(AACAAGCTGATAAACATTTAAAGAG, AAAAA) = 4 
because AAAAA appears four times in this string with at most one mismatch: 
AACAA, ATAAA, AAACA, and AAAGA. Note that two of these occurrences overlap.

Exercise: Compute Count2(AACAAGCTGATAAACATTTAAAGAG, AAAAA).
"""

from P142_dna_approx_pattern_match import pattern_search

def compute_count(text: str, pattern: str, d: int) -> int:
    positions = pattern_search(pattern=pattern, text=text, d=d)
    return len(positions)

if __name__ == "__main__":
    sample_text = "GGAAGGGTCGCACTGAGGCTTCGCATAACTGCTCTACGCCTTCAGATAGAAACAAGTGCAACGTGGCTCCTCATAACTCATCCCAAACTTAGCTCACTCCTCTCGTTCCCGAGATTGGGCAATCCTGAAGATAGTCCCGGACCAACGTGCAGACGCGCAGTTTTTACGGGTTAACGGTAACACAAGAAAGATACGAACCTTACGCGGCTAATAAAAGGCCATAAAATTTATTTACCGGTGGCAAAATTAGAGAATCTCGAACGGTCCTTATGAAGCCCTGGGGCCCCTGCATAGCATTTGCAATGTCTATCTAAATTCG"
    sample_pattern = "CCTGGGG"
    sample_d = 2
    print(compute_count(sample_text, sample_pattern, sample_d))
    
    # Output: 5