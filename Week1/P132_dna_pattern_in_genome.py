"""
Code Challenge: Solve the Pattern Matching Problem.

Input: Two strings, Pattern and Genome.
Output: A collection of space-separated integers specifying all starting 
positions where Pattern appears as a substring of Genome.

Sample Input:
ATAT
GATATATGCATATACTT

Sample Output:
1 3 9
"""

def pattern_search(pattern: str, genome: str):

    positions = []
    
    window = len(pattern)
    
    for i in range(len(genome) - len(pattern) + 1):
        substring = genome [i : i + window]
        if substring == pattern:
            positions.append(i)
                
    return positions

if __name__ == "__main__":
    pattern = "CGC"
    genome = "ATGACTTCGCTGTTACGCGC"
    output = pattern_search(pattern, genome)
    output_string = ""
    for element in output:
        output_string += str(element) + " "
    print(output_string.strip())