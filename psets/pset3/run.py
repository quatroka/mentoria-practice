#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('hino.txt') as file:
    n_patria = 0
    n_brasil = 0
    n_ada = 0
    for line in file:
        line = line.lower()
        n_patria += line.count('pátria')
        n_brasil += line.count('brasil')
        n_ada += line.count('ada')
    file.close()
    print("Número de vezes que aparece a palavra 'Pátria': %s" % n_patria)
    print("Número de vezes que aparece a palavra 'Brasil': %s" % n_brasil)
    print("Número de vezes que aparece a sequência de caracteres 'ada': %s" % n_ada)
