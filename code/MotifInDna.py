def findMotifInDNA(orgDna, testDna):
    positions = []
    for i in range(len(orgDna) - len(testDna)):
        if orgDna[i:i+len(testDna)] == testDna:
            positions.append(i + 1)
    return ' '.join(map(str, positions))

if __name__ == "__main__":
    with open("../data/rosalind_subs.txt", 'r') as f:
        orgDna = f.readline().strip()
        testDna = f.readline().strip()
        result = findMotifInDNA(orgDna, testDna)
        print(result)