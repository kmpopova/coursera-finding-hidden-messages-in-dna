"""
We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if 
pi ≠ qi. For example, CGAAT and CGGAC have two mismatches. The number of 
mismatches between strings p and q is called the Hamming distance between 
these strings and is denoted HammingDistance(p, q).

Hamming Distance Problem: Compute the Hamming distance between two strings.

Input: Two strings of equal length.
Output: The Hamming distance between these strings.
Code Challenge: Solve the Hamming Distance Problem.
"""



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

if __name__ == "__main__":

    p = "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"
    q = "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"
    print(hamming_distance(p, q))
    
    # Output: 23

