def readFastaFormat(filePath):
    with open(filePath, 'r') as f:
        fasta = f.read().strip().split('\n')
        fastaLabel = ''
        fastaDict = {}
        for line in fasta:
            if '>' in line:
                fastaLabel = line
                fastaDict[fastaLabel] = ''
            else:
                fastaDict[fastaLabel] += line
        return fastaDict