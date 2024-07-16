from utils import readFastaFormat


def reverseComplement(dnaString):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[nucleotide] for nucleotide in dnaString[::-1])


def findPalindrome(dnaString):
    for start in range(len(dnaString)):
        for length in range(4, 13, 1):
            currentDna = dnaString[start: start + length]
            reversedDna = reverseComplement(currentDna)
            if (currentDna == reversedDna) and (start + length <= len(dnaString)):
                print(start + 1, length)


if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_revp.txt")
    dnaString = list(fastaDict.values())[0]
    findPalindrome(dnaString)
