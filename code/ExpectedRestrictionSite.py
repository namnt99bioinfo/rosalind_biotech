if __name__ == "__main__":
    with open("../data/rosalind_eval.txt", 'r') as f:
        n = int(f.readline().strip())
        s = f.readline().strip()
        A = map(float, f.readline().strip().split(" "))

        at = s.count('A') + s.count('T')
        gc = s.count('G') + s.count('C')
        for i in A:
            result = pow((1 - i) / 2, at) * pow(i / 2, gc) * (n - len(s) + 1)
            print(round(result, 3), end=" ")