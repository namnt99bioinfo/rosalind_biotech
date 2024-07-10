import itertools

if __name__ == "__main__":
    with open("../data/rosalind_lexf.txt", 'r') as f:
        string = f.readline().strip().split()
        number = int(f.readline())
        result = list(itertools.product(string, repeat=number))
        print("\n".join(["".join(x) for x in result]))
