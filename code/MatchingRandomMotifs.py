


if __name__ == "__main__":
    with open("../data/rosalind_rstr.txt", 'r') as f:
        N, x = f.readline().strip().split(" ")
        N = int(N)
        x = float(x)
        string = f.readline().strip()

        at = string.count('A') + string.count('T')
        gc = string.count('G') + string.count('C')
        P_s = pow(x/2, gc) * pow((1-x)/2, at)
        print(round(1 - pow(1 - P_s, N), 3))
