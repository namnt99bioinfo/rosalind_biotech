if __name__ == "__main__":
    with open("../data/rosalind_init4.txt", 'r') as f:
        num1, num2 = f.readline().strip().split()
        sum = 0
        for i in range(int(num1), int(num2) + 1):
            if i % 2 != 0:
                sum += i
        print(sum)
