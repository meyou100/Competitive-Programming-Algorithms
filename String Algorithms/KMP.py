from typing import List

#Implements the KMP Algorithm for finding the number of occurrences of a pattern in another string
def KMP(text: str, pattern: str) -> List[int]:
    #Constructs the longest prefix suffix array for use in the KMP algorithm
    def lps(s: str) -> List[int]:
        n = len(s)
        lps = [0] * n
        for i in range(1, n):
            j = lps[i - 1]
            while j and s[i] != s[j]: #finds the longest prefix suffix such that the next character is s[i]
                j = lps[j - 1]
            lps[i] = j + (1 if s[i] == s[j] else 0) #if s[i] == s[j] the lps gets extended by an extra character
        return lps

    l = lps(pattern)
    indices = [] #stores the indices of matches
    j = 0 #index in pattern
    for i in range(len(text)):
        while j and text[i] != pattern[j]: #finds the longest prefix of pattern such that the next character is text[i]
            j = l[j - 1]
        if text[i] == pattern[j]: #if the next character of text and pattern is the same, increment the index variables
            j += 1
            if j == len(pattern): #full match to pattern
                indices.append(i - len(pattern) + 1) #finds the index of the first matching letter in a match
                j = l[j - 1] #go to the next longest match
    return indices