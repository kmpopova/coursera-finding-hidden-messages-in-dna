"""
Let's follow the 5' → 3' direction of DNA and walk along the chromosome from 
ter to ori (along a reverse half-strand), then continue on from ori to ter 
(along a forward half-strand). In our previous discussion, we saw that the skew 
is decreasing along the reverse half-strand and increasing along the forward 
half-strand. Thus, the skew should achieve a minimum at the position where 
the reverse half-strand ends and the forward half-strand begins, which is 
exactly the location of ori!

We have just developed an insight for a new algorithm for locating ori: 
it should be found where the skew attains a minimum.

Minimum Skew Problem: Find a position in a genome where the skew diagram 
attains a minimum.

Input: A DNA string Genome.
Output: All integer(s) i minimizing Skewi (Genome) among all values of i 
(from 0 to |Genome|).
"""

def calculate_skew(genome: str) -> list:
    
    skew = [0]
    skew_i = 0

    for nucleotide in genome:
        
        if nucleotide == "G":
            skew_i += 1
        elif nucleotide == "C":
            skew_i -= 1
            
        skew.append(skew_i)

    return skew

def calculate_skew_min(genome: str) -> list:

    skew_diagram = calculate_skew(genome)
    skew_min_list = []
    skew_min = min(skew_diagram)

    for i in range(len(skew_diagram)):
        if skew_diagram[i] == skew_min:
            skew_min_list.append(i)

    return skew_min_list

def return_list_as_string(input_list: list) -> str:
    # Helper function for processing output before submission
    output_str = ""
    for element in input_list:
        output_str += str(element) + " "
    return output_str.strip()


if __name__ == "__main__":

    input_str = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
    print(calculate_skew_min(input_str))
    
    # Output: [11, 24]


    

    