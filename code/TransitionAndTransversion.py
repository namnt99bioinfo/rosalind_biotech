from utils import readFastaFormat

TRANSITION_LIST = [('A', 'G'), ('T', 'C'), ('C', 'T'), ('G', 'A')]
TRANSVERSION_LIST = [('A', 'T'), ('A', 'C'), ('T', 'A'), ('T', 'G'), ('C', 'A'), ('C', 'G'), ('G', 'T'), ('G', 'C')]


def getTransitionTransversionRatio(string1, string2):
    transition = 0
    transversion = 0
    for i in range(len(string1)):
        if (string1[i], string2[i]) in TRANSITION_LIST:
            transition += 1
        if (string1[i], string2[i]) in TRANSVERSION_LIST:
            transversion += 1
    return transition / transversion


if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_tran.txt")
    s1, s2 = list(fastaDict.values())
    result = getTransitionTransversionRatio(s1, s2)
    print(result)
