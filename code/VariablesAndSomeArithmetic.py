if __name__ == "__main__":
    with open("../data/rosalind_init2.txt", 'r') as f:
        values = f.readline().strip().split(' ')
        number1, number2 = int(values[0]), int(values[1])

        print(number1 * number1 + number2 * number2)
