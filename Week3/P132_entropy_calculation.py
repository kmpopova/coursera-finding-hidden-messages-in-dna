"""
Exercise Break: Compute the entropy of 
the NF-κB motif matrix (reproduced below). 
Your answer should be accurate to within 0.002 of the correct response.

"""
import math 

def calculate_entropy(motifs : list) -> int:
    # motifs: list of strings, assuming each string of equal length
    # e.g.
    # motifs = ["TCGGGGGTTTTT", "CCGGTGACTTAC", "ACGGGGATTTTC", "TTGGGGACTTTT", "AAGGGGACTTCC", "TTGGGGACTTCC", "TCGGGGATTCAT", "TCGGGGATTCCT", "TAGGGGAACTAC", "TCGGGTATAACC"]
    probabilities = {"A": [], "T": [],"G": [],"C": []}

    n = len(motifs[0])

    for i in range(n):
        occurence_a = 0
        occurence_t = 0
        occurence_g = 0
        occurence_c = 0

        for motif in motifs:

            if motif[i] == "A":
                occurence_a += 1
            elif motif[i] == "T":
                occurence_t += 1
            elif motif[i] == "G":
                occurence_g += 1
            else:
                occurence_c += 1
        
        probabilities["A"].append(occurence_a/len(motifs))
        probabilities["T"].append(occurence_t/len(motifs))
        probabilities["G"].append(occurence_g/len(motifs))
        probabilities["C"].append(occurence_c/len(motifs))

    entropies = []
    for j in range(n):
        col_entropy = 0
        for val in probabilities.values():
            if val[j] != 0:
                col_entropy += val[j]*math.log2(val[j])
        entropies.append(-1*col_entropy)

    total_entropy = sum(entropies)

    return total_entropy


if __name__ == "__main__":
    motifs = ["TCGGGGGTTTTT", "CCGGTGACTTAC", "ACGGGGATTTTC", "TTGGGGACTTTT", "AAGGGGACTTCC", "TTGGGGACTTCC", "TCGGGGATTCAT", "TCGGGGATTCCT", "TAGGGGAACTAC", "TCGGGTATAACC"]
    print(f"{calculate_entropy(motifs):.4f}")

    # Output: 9.9163