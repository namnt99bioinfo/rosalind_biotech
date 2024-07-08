def getDnaStrand(dnaSample):
    newDnaStrand = ''
    for nu in dnaSample[::-1]:
        if nu == 'A':
            newDnaStrand += 'T'
        if nu == 'T':
            newDnaStrand += 'A'
        if nu == 'G':
            newDnaStrand += 'C'
        if nu == 'C':
            newDnaStrand += 'G'
    return newDnaStrand


if __name__ == "__main__":
    with open("../data/rosalind_revc.txt", 'r') as f:
        dnaSample = f.readline().strip()
        result = getDnaStrand(dnaSample)
        print(result)