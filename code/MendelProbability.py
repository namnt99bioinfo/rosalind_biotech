def probaMendelMating(dominant, hetero, recess):
    total = dominant + hetero + recess
    mauso = total * (total - 1)
    couples = [
        dominant * (dominant - 1),
        dominant * hetero,
        dominant * recess,
        hetero * dominant,
        hetero * (hetero - 1) * 0.75,
        hetero * recess * 0.5,
        recess * dominant,
        recess * hetero * 0.5,
    ]
    return round(sum(couples) / mauso, 5)


if __name__ == "__main__":
    with open("../data/rosalind_iprb.txt", 'r') as f:
        dominant, hetero, recess = map(float, f.readline().strip().split(' '))
        print(probaMendelMating(dominant, hetero, recess))
