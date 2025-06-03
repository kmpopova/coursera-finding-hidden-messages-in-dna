"""
Given a nucleotide p, we denote its complementary nucleotide as p*. The reverse complement of a string Pattern = p1 … pn is the string Patternrc = pn* … p1* formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string. We will need the solution to the following problem throughout this chapter:

Reverse Complement Problem: Find the reverse complement of a DNA string.

Input: A DNA string Pattern.
Output: Patternrc , the reverse complement of Pattern.

Code Challenge: Solve the Reverse Complement Problem.
"""


def reverse_complement(dna: str):
    matches = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for nucleotide in dna:
        complement += matches[nucleotide]
    return complement[::-1]

if __name__ == "__main__":
    dna_string = "GCTAGCT"
    rev_comp = reverse_complement(dna_string)
    print(rev_comp)
