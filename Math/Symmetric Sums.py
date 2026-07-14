def symmetric_sum(arr, k):
    s = [0] * (k + 1) #represents the kth sym sum
    s[0] = 1 #base case

    for i in range(len(arr)):
        for j in range(k, 0, -1): #traverse backwards since s[j] depends on the previous value of s[j - 1]
            s[j] += arr[i] * s[j - 1]

    return s