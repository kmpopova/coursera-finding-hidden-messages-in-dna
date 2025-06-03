def return_list_as_string(input_list: list) -> str:
    output_str = ""
    for element in input_list:
        output_str += str(element) + " "
    return output_str.strip()

def read_string_from_file(input_file: str) -> str:
    output_string = ""

    with open(input_file) as f:
        for line in input_file:
            output_string += f.readline().strip()

    return output_string

def reverse_complement(dna: str):
    matches = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for nucleotide in dna:
        complement += matches[nucleotide]
    return complement[::-1]

def hamming_distance(p: str, q: str) -> int:
    # Calculates how many mismatches two strings have
    len_p = len(p)
    if len_p != len(q):
        print("Strings must be of equal length!")
        return None

    hamm_dist = 0
    for i in range(len_p):
        if p[i] != q[i]:
            hamm_dist += 1

    return hamm_dist

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