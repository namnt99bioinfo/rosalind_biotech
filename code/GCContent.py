from utils import readFastaFormat


def getGcContentPercent(dna):
    gcCount = 0
    for nu in dna:
        if nu == 'G' or nu == 'C':
            gcCount += 1
    return round(gcCount / len(dna) * 100, 6)

if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_gc.txt")
    dnaList = list(fastaDict.values())
    dnaLabel = list(fastaDict.keys())

    fastaLabel = dnaLabel[dnaList.index(dnaList[0])]
    maxValue = getGcContentPercent(dnaList[0])
    for index in range(1, len(dnaList)):
        currentValue = getGcContentPercent(dnaList[index])
        if currentValue > maxValue:
            maxValue = currentValue
            fastaLabel = dnaLabel[dnaList.index(dnaList[index])]

    print(fastaLabel)
    print(maxValue)
