import math

def getCombination(n, m):
    result = 0
    for k in range(m, n + 1):
        result += math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    return round(result % 1000000)


if __name__ == "__main__":
    with open("../data/rosalind_aspc.txt", 'r') as f:
        n, m = f.readline().strip().split()
        result = getCombination(int(n), int(m))
        print(result)
