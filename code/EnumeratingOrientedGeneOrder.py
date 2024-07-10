import itertools

def signedPermutation(number):
    list1 = []
    for i in range(number):
        list1.extend([i + 1, -i - 1])

    list2 = list(itertools.permutations(list1, number))
    list3 = []

    for eachTuple in list2:
        newSet = set() #auto remove duplicate
        for value in eachTuple:
            newSet.add(abs(value))

        if len(newSet) == len(eachTuple):
            list3.append(eachTuple)

    print(len(list3))
    for eachTuple in list3:
        a = str(eachTuple)
        a = a.replace('(', '').replace(',', '').replace(')', '')
        print(a)


if __name__ == "__main__":
    with open("../data/rosalind_sign.txt", 'r') as f:
        number = int(f.readline())
        signedPermutation(number)
