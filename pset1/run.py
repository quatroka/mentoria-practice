with open('hino.txt') as file:
    n_patria = 0
    n_brasil = 0
    for line in file:
        line = line.lower()
        if 'pátria' in line:
            n_patria += 1
        if 'brasil' in line:
            n_brasil += 1
    file.close()
    print("Número de vezes que aparece a palavra 'Pátria': %s" % n_patria)
    print("Número de vezes que aparece a palavra 'Brasil': %s" % n_brasil)
