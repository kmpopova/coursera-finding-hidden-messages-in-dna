"""
Since we don't know the location of ori in a circular genome, let's linearize it 
(i.e., select an arbitrary position and pretend that the genome begins here), 
resulting in a linear string Genome. 

We define Skew_i(Genome) as the difference 
between the total number of occurrences of G and the total number of occurrences 
of C in the first i nucleotides of Genome. 

The skew diagram is defined by plotting 
Skew_i (Genome) (as i ranges from 0 to |Genome|), where Skew0 (Genome) is set equal 
to zero. The figure below shows a skew diagram for the DNA string 
CATGGGCATCGGCCATACGCC.

Note that we can compute Skew_i+1(Genome) from Skew_i(Genome) according to the 
nucleotide in position i of Genome. If this nucleotide is G, then 
Skew_i+1(Genome) = Skew_i(Genome) + 1; if this nucleotide is C, then 
Skew_i+1(Genome)= Skew_i(Genome) – 1; otherwise, Skew_i+1(Genome) = Skew_i(Genome).

Exercise:
Give all values of Skew_i (GAGCCACCGCGATA) for i ranging from 0 to 14 as a 
collection of space-separated integers. Use the sample dataset below to help!
"""

def calculate_skew(genome: str) -> str:
    skew = [0]
    skew_i = 0

    for nucleotide in genome:
        
        if nucleotide == "G":
            skew_i += 1
        elif nucleotide == "C":
            skew_i -= 1
            
        skew.append(skew_i)

    output = ""
    for element in skew:
        output += str(element) + " "
    return output.strip()


if __name__ == "__main__":
    sample_input = "CATGGGCATCGGCCATACGCC"
    sample_output = calculate_skew(sample_input)

    print(sample_output)

    # Output: 0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2
