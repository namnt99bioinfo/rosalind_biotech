from utils import readFastaFormat


def getProfile(dnaStrings):
    default = [0] * len(dnaStrings[0])
    results = {
        'A': default[:],
        'C': default[:],
        'G': default[:],
        'T': default[:],
    }
    for dnaString in dnaStrings:
        for order, nucleotide in enumerate(dnaString):
            results[nucleotide][order] += 1
    return results


def getConsensus(profile):
    result = []
    nuKeys = list(profile.keys())

    for index in range(len(profile[nuKeys[0]])):
        maxCount = 0
        maxLabel = ''
        for nuKey in nuKeys:
            currentCount = profile[nuKey][index]
            if currentCount > maxCount:
                maxCount = currentCount
                maxLabel = nuKey

        result.append(maxLabel)
    return ''.join(result)


if __name__ == "__main__":
    fastaDict = readFastaFormat("../data/rosalind_cons.txt")
    dnaStrings = list(fastaDict.values())
    profile = getProfile(dnaStrings)
    consensus = getConsensus(profile)
    print(consensus)
    for key in list(profile.keys()):
        finalValue = " ".join(str(value) for value in profile[key])
        print(key, ':', finalValue)
