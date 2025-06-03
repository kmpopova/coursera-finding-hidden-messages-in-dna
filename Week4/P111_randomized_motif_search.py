"""
RandomizedMotifSearch(Dna, k, t)
    randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    BestMotifs ← Motifs
    while forever
        Profile ← Profile(Motifs)
        Motifs ← Motifs(Profile, Dna)
        if Score(Motifs) < Score(BestMotifs)
            BestMotifs ← Motifs
        else
            return BestMotifs


Code Challenge: Implement RandomizedMotifSearch.

Input: Integers k and t, followed by a space-separated collection of strings Dna.
Output: A collection BestMotifs resulting from running RandomizedMotifSearch(Dna, k, t) 1,000 times. Remember to use pseudocounts!
Debug Datasets

Sample Input:
8 5
CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA

Sample Output:
TCTCGGGG CCAAGGTG TACAGGCG TTCAGGTG TCCACGTG

You have an unlimited number of attempts.
Time limit: 5 mins
"""

import numpy as np
from helper_functions import *

def randomly_select_kmers(dna: list[str], k: int) -> list:
    # Takes a random sequence of length k from each string in list dna
    # returns the list of these sequences
    random_kmers = []
    for seq in dna:
        start = np.random.randint(0, len(seq) - k + 1)
        random_kmer = seq[start: start + k]
        random_kmers.append(random_kmer)
    
    return random_kmers

def calculate_profile(motifs : list) -> dict:
    
    k = len(motifs[0])
    counts = {"A": [0]*k, "C": [0]*k, "G": [0]*k, "T": [0]*k}
    # for each sequence
    # look at letters one by one
    # add one to the corresponding position in the dictionary, 
    # to the corresponding letter
    for motif in motifs:
        for i in range(len(motif)):
            counts[motif[i]][i] += 1

    # adding pseudocounts
    for letter in "ACGT":
        for j in range(len(counts[letter])):
            counts[letter][j] += 1

    # turning counts into probabilities
    # for each position, count how many time each letter occurs
    # update counts[letter][position] by dividing that number 
    # by the (total number of motifs + 4)
    for letter in "ACGT":
        for j in range(len(counts[letter])):
            counts[letter][j] /= (len(motifs)+4)
    
    return counts


def find_profile_most_probable_kmer(text: str, k: int, profile: dict) -> str:
    
    n = len(text)
    max_score = 0
    best_pattern = ""

    for start_position in range(n-k+1):
        pattern = text[start_position:start_position+k]
        pattern_score = 1
        for i in range(k):
            letter = pattern[i]
            profile_row = letter
            profile_column = i

            pattern_score *= profile[profile_row][profile_column]
        if pattern_score > max_score:
                max_score = pattern_score
                best_pattern = pattern

    return best_pattern



def create_profile_string(profile: dict, k) -> str:
    profile_string = ""
    
    alphabet = "ACGT"
    for i in range(k):
        max_value = 0
        max_position = ""
        for letter in alphabet:
            if profile[letter][i] > max_value:
                max_value = profile[letter][i]
                max_position = letter
        profile_string += max_position
    
    return profile_string


def calculate_score_of_motifs(motifs: list, profile: dict) -> int:
    total_score = 0
    k = len(motifs[0])
    consensus_string = create_profile_string(profile, k)
    
    for motif in motifs:
        total_score += hamming_distance(motif, consensus_string)

    return total_score


def randomized_motif_search(dna: list, k: int, t: int) -> list:
    
    motifs = randomly_select_kmers(dna, k)
    best_motifs = motifs
    
    while True:

        profile = calculate_profile(motifs)
        current_motifs = []
        for seq in dna:
            most_prob_kmer = find_profile_most_probable_kmer(seq, k, profile)
            current_motifs.append(most_prob_kmer)
        
        if calculate_score_of_motifs(current_motifs, profile) < \
            calculate_score_of_motifs(best_motifs, profile):
            best_motifs = current_motifs
        else:
            return best_motifs




if __name__ =="__main__":
        
    dna_str = "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
    dna = dna_str.split()
    
    k = 8
    t = 5
    best_motifs = []
    
    best_score = float("inf")
    for i in range(1000):
      
        current_motifs = randomized_motif_search(dna, k, t)
        current_profile = calculate_profile(current_motifs)
        current_score = calculate_score_of_motifs(current_motifs, current_profile)
        if current_score < best_score:
            best_motifs = current_motifs
            best_score = current_score

    print(best_motifs)
