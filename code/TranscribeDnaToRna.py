def getDnaToRna(dnaSample):
    return dnaSample.replace('T', 'U')

if __name__ == "__main__":
    with open("../data/rosalind_rna.txt", 'r') as f:
        dnaSample = f.readline().strip()
        result = getDnaToRna(dnaSample)
        print(result)