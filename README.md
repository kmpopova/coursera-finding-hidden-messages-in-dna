# Coursera: Finding Hidden Messages in DNA (Bioinformatics I)

This repository contains my solutions and code for the Coursera course **"Finding Hidden Messages in DNA (Bioinformatics I)"** by UC San-Diego (course authors: Pavel Pevzner & Philipp Compeau). 

The code is organized by week and covers a variety of classic bioinformatics algorithms and problems, implemented in Python.

## Certificate of completion

You can view my certificate of completion for this course here: [Coursera: Finding Hidden Messages in DNA (Bioinformatics I) Certificate](https://coursera.org/share/e5d16bf4227fcf60d72e39d06b79ae51)

## Folder Structure

- **Week1/**: Basic string and pattern matching algorithms for DNA sequences.
  - `P121_dna_pattern_search.py`: Search for patterns in DNA.
  - `P122_dna_freq_words.py`: Find frequent words (k-mers) in DNA.
  - `P131_dna_rev_complement.py`: Compute the reverse complement of a DNA string.
  - `P132_dna_pattern_in_genome.py`: Find all occurrences of a pattern in a genome.
  - `P141_dna_find_clumps.py`: Find clumps of patterns in a genome.

- **Week2/**: Approximate pattern matching, mismatches, and related algorithms.
  - `P130_dna_skew_diagram.py`: Compute skew diagrams for DNA sequences.
  - `P131_dna_min_skew.py`: Find minimum skew positions.
  - `P141_dna_hamming_dist.py`: Calculate Hamming distance between strings.
  - `P142_dna_approx_pattern_match.py`: Approximate pattern matching.
  - `P143_dna_approx_pattern_count.py`: Count approximate pattern matches.
  - `P145_dna_freq_words_w_mismatch.py`: Find frequent words with mismatches.
  - `helper_functions.py`: Utility functions for Week 2 scripts.

- **Week3/**: Motif finding and entropy calculations.
  - `P121_dna_motif_enumeration.py`: Motif enumeration in DNA sequences.
  - `P132_entropy_calculation.py`: Calculate entropy of motifs.
  - `P151_profile_most_prob_kmer.py`: Find most probable k-mers using a profile matrix.
  - `P171_median_string.py`: Find the median string in a set of DNA sequences.
  - `helper_functions.py`: Utility functions for Week 3 scripts.

- **Week4/**: Randomized algorithms for motif search.
  - `P111_randomized_motif_search.py`: Randomized motif search algorithm implementation.
  - `helper_functions.py`: Utility functions for Week 4 scripts.

## About

Each script is a standalone solution to a classic problem in bioinformatics, as presented in the course. The code is written in Python and is intended for educational and reference purposes.

## Usage

- Run any script with Python 3.x:
  ```
  python script_name.py
  ```
- Some scripts require helper functions from the corresponding `helper_functions.py` file in the same week folder.

## License

This repository is for educational use and personal study. If you use or adapt the code, please credit the original Coursera course and the author.
