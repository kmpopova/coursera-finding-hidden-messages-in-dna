"""
The Clump Finding Problem is a more complex problem than we have encountered 
thus far, and writing a function solving it from scratch would be difficult. 
However, this is where modularity in writing programs is so helpful. 
We already have a FrequencyTable function that will produce a frequency 
table for a given window of a string of length L. If we apply it to a given 
window, then we simply need to check if there are any string keys in the 
table whose values are at least equal to t. We will append any such keys 
that we have not already seen in some other window of text to a growing 
list of strings. In the end, this list of strings will contain the 
(L, t)-clumps of text. This is handled by the following FindClumps function.

FindClumps(Text, k, L, t)
    Patterns ← an array of strings of length 0
    n ← |Text|
    for every integer i between 0 and n − L
        Window ← Text(i, L)
        freqMap ← FrequencyTable(Window, k)
        for every key s in freqMap
            if freqMap[s] ≥ t
                append s to Patterns
    remove duplicates from Patterns
    return Patterns
"""

def frequency_table(text: str, k: int) -> dict:
    # Creates a dictionary with counts for all patterns of length k in text
    freq_map = dict()
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i : i + k]
        if pattern not in freq_map.keys():
            freq_map[pattern] = 1
        else:
            freq_map[pattern] += 1
    return freq_map

def find_clumps(text: str, k: int, L: int, t: int) -> list:
    patterns =  []
    n = len(text)
    for i in range(n-L+1):
        window = text[i:i+L]
        freq_map = frequency_table(window, k)
        
        for key in freq_map.keys():
            if freq_map[key] >= t and key not in patterns:
                patterns.append(key)

        
    return patterns 


if __name__ == "__main__":
    
    genome_string = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    
    output_list = find_clumps(genome_string, 5, 50, 4)
        
    output_string = ""
    for element in output_list:
        output_string += str(element) + " "
    
    print(output_string.strip())
    
    # Output: CGACA GAAGA
    
