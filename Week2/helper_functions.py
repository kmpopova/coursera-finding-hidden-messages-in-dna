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