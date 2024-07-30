def completeATree(data):
    n = data[0][0]
    edges = data[1:]
    print(n - len(edges) - 1)


with open('../data/rosalind_tree.txt', 'r') as f:
    data = []
    for line in f:
        splitData = [int(x) for x in line.split()]
        data.append(splitData)
    completeATree(data)
