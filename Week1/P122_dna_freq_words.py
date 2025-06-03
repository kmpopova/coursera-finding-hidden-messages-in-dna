"""
FrequentWords(Text, k)
    FrequentPatterns ← an empty set
    for i ← 0 to |Text| − k
        Pattern ← the k-mer Text(i, k)
        Count(i) ← PatternCount(Text, Pattern)
    maxCount ← maximum value in array Count
    for i ← 0 to |Text| − k
        if Count(i) = maxCount
            add Text(i, k) to FrequentPatterns
    remove duplicates from FrequentPatterns
    return FrequentPatterns

FrequencyTable(Text, k)
    freqMap ← empty map
    n ← |Text|
    for i ← 0 to n − k
        Pattern ← Text(i, k)
        if freqMap[Pattern] doesn't exist
            freqMap[Pattern]← 1
        else
           freqMap[pattern] ←freqMap[pattern]+1 
    return freqMap    

BetterFrequentWords(Text, k)
    FrequentPatterns ← an array of strings of length 0
    freqMap ← FrequencyTable(Text, k)
    max ← MaxMap(freqMap)
    for all strings Pattern in freqMap
        if freqMap[pattern] = max
            append Pattern to frequentPatterns
    return frequentPatterns
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

def better_frequent_words(text: str, k: int) -> list:
    # Returns a list containing all the most frequent patterns of length k
    # in text
    frequent_patterns = []
    freq_map = frequency_table(text, k)
    max_count = max(freq_map.values())
    
    for key in freq_map:
        if freq_map[key] == max_count:
            frequent_patterns.append(key)

    return frequent_patterns


if __name__ == "__main__":
    
    text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
    k = 3
    output_array = better_frequent_words(text, k)
    print(output_array)

    my_string = ""
    for value in output_array:
        my_string += value + " "
    my_string.strip()

    print(my_string)
