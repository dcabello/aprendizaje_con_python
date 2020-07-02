def next_level(estudiante, n_total):
    if n_total >= 200:
        print estudiante, "Pasa con", n_total
    else:
        print estudiante, "Repite con", n_total
def total_score(estudiante, score1, score2, score3, score4, score5, score6):
    suma_total = score1 + score2 + score3 + score4 + score5 + score6
    next_level(estudiante, suma_total)
print "Resultados Score "
print "---------- ----- "
total_score("Juan", 34, 30, 30, 34, 35, 37)
total_score("Pablo", 24, 28, 50, 24, 45, 27)
total_score("Maria", 44, 20, 34, 43, 35, 32)
total_score("Alcides", 23, 36, 30, 22, 45, 39)
total_score("Pedro", 38, 40, 36, 37, 26, 32)
total_score("Tomas", 23, 52, 51, 30, 33, 22)
total_score("Ana", 40, 32, 27, 16, 32, 34)    
total_score("Laura", 38, 39, 28, 37, 36, 42)
