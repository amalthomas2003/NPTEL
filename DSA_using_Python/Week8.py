def longest_fully_dividing_subsequence(seq):
    n = len(seq)
    dp = [1] * n 

    for i in range(1, n):
        for j in range(i):
            if seq[i] % seq[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    max_length = max(dp)
    return max_length

# Example 1
sequence1=[]
for _ in range(int(input())):
    
    sequence1+=[int(input())]
result1 = longest_fully_dividing_subsequence(sequence1)
print(result1)