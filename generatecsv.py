import pickle
cycles = pickle.load(open("5cycle.pickle", "rb"))
print(len(cycles.keys()))

nutella = {}
minty = {}

for case in cycles.keys():
    permutation, orientation, rlub_solutions, rlu_solutions = cycles[case]
    if permutation[0] == 1 and permutation[1] == 0 and orientation[0] == 1 and orientation[1] == 1:
        nutella[case] = cycles[case]
    if permutation[0] == 1 and permutation[1] == 0 and orientation[0] == 0 and orientation[1] == 0:
        minty[case] = cycles[case]


print(nutella)