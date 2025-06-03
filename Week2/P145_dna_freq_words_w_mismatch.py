"""
A most frequent k-mer with up to d mismatches in Text is simply a string 
Pattern maximizing Countd(Text, Pattern) among all k-mers. Note that 
Pattern does not need to actually appear as a substring of Text; for example, 
as we already saw, AAAAA is the most frequent 5-mer with 1 mismatch in 
AACAAGCTGATAAACATTTAAAGAG, even though it does not appear exactly in this string. 
Keep this in mind while solving the following problem.

Frequent Words with Mismatches Problem: Find the most frequent k-mers with 
mismatches in a string.

Input: A string Text as well as integers k and d.
Output: All most frequent k-mers with up to d mismatches in Text.
"""

"""
Start by solving the Neighbors Problem: finding all d-mismatched strings of 
a given pattern.
"""
from P141_dna_hamming_dist import hamming_distance
from helper_functions import reverse_complement, return_list_as_string


def suffix(pattern: str):
    """
    Our idea for generating Neighbors(Pattern, d) is as follows. 
    If we remove the first symbol of Pattern (denoted FirstSymbol(Pattern)), 
    then we will obtain a (k − 1)-mer that we denote by Suffix(Pattern).
    """
    
    return pattern[1:]

def neighbors(pattern: str, d: int) -> set:
    neighborhood = set()
    neighborhood.add(pattern)
    nucleotides = ["A", "C", "G", "T"]
    if d == 0:
        return neighborhood
    
    if len(pattern) == 1:
        for nuc in nucleotides:
            neighborhood.add(nuc)
        return neighborhood
    
    suffix_neughbors = neighbors(suffix(pattern), d)
    for text_str in suffix_neughbors:
        if hamming_distance(suffix(pattern), text_str) < d:
            for x in nucleotides:
                neighborhood.add(x + text_str)
        else:
            neighborhood.add(pattern[0]+text_str)


    return neighborhood

def neighbors_exactly_d(pattern: str, d: int) -> set:
    neighborhood = set()
    neighborhood.add(pattern)
    nucleotides = ["A", "C", "G", "T"]
    if d == 0:
        return neighborhood
    
    if len(pattern) == 1:
        for nuc in nucleotides:
            neighborhood.add(nuc)
        return neighborhood
    
    suffix_neughbors = neighbors(suffix(pattern), d)
    for text_str in suffix_neughbors:
        if hamming_distance(suffix(pattern), text_str) == d:
            for x in nucleotides:
                neighborhood.add(x + text_str)
        else:
            neighborhood.add(pattern[0]+text_str)


    return neighborhood

def freq_words_w_mismatches(text: str, k: int, d: int):
    patterns = []
    freq_map = {}
    n = len(text)

    for i in range(0, n-k+1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            if neighbor not in freq_map.keys():
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] += 1

    m = max(freq_map.values())
    
    for key in freq_map.keys():
        if freq_map[key] == m:
            patterns.append(key)
    return set(patterns)



def freq_words_w_mismatches_and_rev_complements(text: str, k: int, d: int) -> list:
    """
    text: the Text in which to search, e.g. fragment of genome
    k: length of Pattern
    d: number of mismatches
    """
    patterns = []
    freq_map = {}
    n = len(text)

    for i in range(0, n - k + 1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern, d)
        rev_pattern = reverse_complement(pattern)
        rev_neighborhood = neighbors(rev_pattern, d)
        for neighbor in neighborhood.union(rev_neighborhood):
            if neighbor not in freq_map:
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] += 1

    m = max(freq_map.values())
    for key in freq_map.keys():
        if freq_map[key] == m:
            patterns.append(key)
    return set(patterns)


if __name__ == "__main__":
    
    str_1 = "AAAAAGGGGGAGTTTGGGTAAAGGTTTTAAGTTTTAATTTTTTAGGTAGAATTTAAAGTTTAGGGGTTTTAGGTAGAGAATTTTTTAAGTGGAAAATTTAAAAGGGTGGGTGTAGGTTTTGGAAAGGGGTAAAATTTGTAGTTTGGAGGTAGAGTTTTTTAAAAAGGGGTTTTGGAGAGTTTAGAGTTTTTTTTTGTTTTGGAGGGTTTAGTTTAAAGAAGTAAGTTTTAAAAGTAGGGGTGTGTGG"
    num_1 = 7
    num_2 = 2

    output = freq_words_w_mismatches_and_rev_complements(str_1, num_1, num_2)
    print(return_list_as_string(output))
    
    # Output: TTAAAAT ATTTTAA


