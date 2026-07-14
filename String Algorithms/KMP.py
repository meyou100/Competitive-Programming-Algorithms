#Implements the KMP Algorithm for finding the number of occurrences of a substring in another string
def KMP(s: str, sub: str):
    #Constructs the longest prefix suffix array for use in the KMP algorithm
    def lps(s: str):
        n = len(s)
        lps = [0] * n
        for i in range(1, n):
            j = lps[i - 1]
            while j and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
            lps[i] = j
        return lps

    l = lps(sub)
    #not finished