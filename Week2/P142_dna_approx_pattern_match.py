"""
We say that a k-mer Pattern appears as a substring of Text with at most 
d  mismatches if there is some k-mer substring Pattern' of Text having d 
or fewer mismatches with Pattern, i.e., 

HammingDistance(Pattern, Pattern') ≤ d. 

Our observation that a DnaA box may appear with slight variations leads 
to the following generalization of the Pattern Matching Problem.

Approximate Pattern Matching Problem: Find all approximate occurrences 
of a pattern in a string.

Input: Strings Pattern and Text along with an integer d.
Output: All starting positions where Pattern appears as a substring of 
Text with at most d mismatches.

Code Challenge: Solve the Approximate Pattern Matching Problem.
"""

from P141_dna_hamming_dist import hamming_distance
from helper_functions import  return_list_as_string

def pattern_search(pattern: str, text: str, d: int) -> list:

    positions = []
    
    window = len(pattern)
    
    for i in range(len(text) - len(pattern) + 1):
        substring = text[i : i + window]
        hamm_dist = hamming_distance(substring, pattern)

        if hamm_dist <= d:
            positions.append(i)
                
    return positions

if __name__ == "__main__":
    sample_pattern = "GAGG"
    sample_text = "TTTAGAGCCTTCAGAGG"
    sample_d = 2

    # Printing all starting positions
    print(return_list_as_string(pattern_search(sample_pattern, sample_text, sample_d)))
    
    # Output: 2 4 11 13    