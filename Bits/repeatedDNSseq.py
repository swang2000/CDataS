'''
187. Repeated DNA Sequences
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
'''
def findRepeatedDnaSequences(s: str):
    # let's map each ATCG to some integer, so that I don't end of saving 10 char in my map
    # A = 00
    # T = 01
    # C = 10
    # G = 11

    res = []
    mp = {"A": 0, "T": 1, "C": 2, "G": 3}
    seen = {}
    ln = len(s)
    for i in range(ln -9):
        sequence = 0
        for j in range(i, i+ 10):
            sequence <<= 2
            sequence |= mp[s[j]]

        gt = seen.get(sequence, 0)
        if gt == 1:
            res.append(s[i:i + 10])
            seen[sequence] = 2
        elif gt == 0:
            seen[sequence] = 1

    return res

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
findRepeatedDnaSequences(s)