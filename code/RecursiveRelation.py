
def expectedPairs(months, offsprings):
    adults, pairs = 1, 1
    for month in range(months - 1):
        pairs, adults = adults, adults + offsprings * pairs
    return pairs

if __name__ == "__main__":
    with open("../data/rosalind_fib.txt", 'r') as f:
        n, k = f.readline().strip().split(" ")
        print(expectedPairs(int(n), int(k)))