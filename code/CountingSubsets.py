def getSubsetCount(number):
    sset = 1
    for i in range(number):
        sset = (sset * 2) % 1000000
    return sset


if __name__ == "__main__":
    with open("../data/rosalind_sset.txt", 'r') as f:
        number = f.readline().strip()
        result = getSubsetCount(int(number))
        print(result)
