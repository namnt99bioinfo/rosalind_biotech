from utils import readFastaFormat


def getGcContentPercent(dna):
    gcCount = 0
    for nu in dna:
        if nu == 'G' or nu == 'C':
            gcCount += 1
    return round(gcCount / len(dna) * 100, 6)


def findMaxGcContent(fastaDict):
    return [fastaLabel, maxGc]


if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_gc.txt")
    dnaList = list(fastaDict.values())
    dnaLabel = list(fastaDict.keys())

    fastaLabel = ''
    maxGc = getGcContentPercent(dnaList[0])
    for index in range(1, len(dnaList)):
        currentValue = getGcContentPercent(dnaList[index])
        if currentValue > maxGc:
            maxGc = currentValue
            fastaLabel = dnaLabel[dnaList.index(dnaList[index])]

    print(fastaLabel)
    print(maxGc)
