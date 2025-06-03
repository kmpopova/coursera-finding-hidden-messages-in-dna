"""
Code Challenge: Implement PatternCount (reproduced below).
     Input: Strings Text and Pattern.
     Output: Count(Text, Pattern).

PatternCount(Text, Pattern)
  count ← 0
  for i ← 0 to |Text| − |Pattern|
    if Text(i, |Pattern|) = Pattern
      count ← count + 1
  return count
"""

def pattern_count(text: str, pattern: str):
    count = 0
    
    window = len(pattern)
    
    for i in range(len(text)):
        
        if i + window <= len(text):
            substring = text[i : i + window]
            
            if substring == pattern:
                count += 1
                
    return count

if __name__ == "__main__":
    # expect 3
    print(pattern_count("ACGTACGTACGT", "CG"))
    # expect 2
    print(pattern_count("ATGCGCGTA", "GCG"))
    # expect 1
    print(pattern_count("AAAGAGTGTCTGA", "AAA"))
    # expect 1
    print(pattern_count("AGCGTGCCGAAATTT", "TTT"))

    # test problem
    print(pattern_count("CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC", "CGCG"))
