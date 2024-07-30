from Bio import SeqIO

def longestCommonSubsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i, x in enumerate(s):
        for j, y in enumerate(t):
            if x == y:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    # Finding a Shared Spliced Motif
    longest_common_subsequence = ""
    while m*n!=0:
        if dp[m][n] == dp[m-1][n]:
            m -= 1
        elif dp[m][n] == dp[m][n-1]:
            n -= 1
        else:
            longest_common_subsequence += s[m-1]
            m -= 1
            n -= 1
    # print(dp)
    print(longest_common_subsequence)
    return longest_common_subsequence

if __name__ == "__main__":
    seq_name, seq_string = [], []
    with open("rosalind_lcsq.txt", "r") as fa:
        for seq_record in SeqIO.parse(fa, "fasta"):
            seq_name.append(seq_record.name)
            seq_string.append(str(seq_record.seq))
    s, t = seq_string
    longestCommonSubsequence(s, t)