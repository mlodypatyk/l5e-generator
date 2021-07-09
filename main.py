import itertools
from time import time
import pickle

solved = 'ggggggbbbbbbrrrrrryyyyyy'
moves = {
    "U": [6, 7, 8, 3, 4, 5, 12, 13, 14, 9, 10, 11, 0, 1, 2, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "U'": [12, 13, 14, 3, 4, 5, 0, 1, 2, 9, 10, 11, 6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    "R":  [0, 1, 19, 3, 23, 20, 4, 7, 8, 5, 2, 11, 12, 13, 14, 15, 16, 17, 18, 10, 9, 21, 22, 6],
    "R'": [0, 1, 10, 3, 6, 9, 23, 7, 8, 20, 19, 11, 12, 13, 14, 15, 16, 17, 18, 2, 5, 21, 22, 4],
    "L": [16, 1, 2, 17, 14, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21, 15, 19, 18, 3, 0, 20, 4, 22, 23],
    "L'": [19, 1, 2, 18, 21, 5, 6, 7, 8, 9, 10, 11, 12, 13, 4, 15, 0, 3, 17, 16, 20, 14, 22, 23],
    "B": [0, 1, 2, 3, 4, 5, 6, 7, 23, 9, 21, 22, 10, 13, 14, 11, 8, 17, 18, 19, 20, 12, 15, 16],
    "B'": [0, 1, 2, 3, 4, 5, 6, 7, 16, 9, 12, 15, 21, 13, 14, 22, 23, 17, 18, 19, 20, 10, 11, 8]
}

RLUB = ["U", "U'", "R", "R'", "L", "L'", "B", "B'"]
RLU = ["U", "U'", "R", "R'", "L", "L'"]

edge_positions = [
    [14, 0],
    [2, 6],
    [4, 19],
    [10, 23],
    [16, 21]
]

edge_colors = [
    ['r', 'g'],
    ['g', 'b'],
    ['g', 'y'],
    ['b', 'y'],
    ['r', 'y']
]

def arePermsEqualParity(perm0, perm1):
    perm1 = perm1[:]

    transCount = 0
    for loc in range(len(perm0) - 1):
        p0 = perm0[loc]
        p1 = perm1[loc]
        if p0 != p1:
            sloc = perm1[loc:].index(p0)+loc
            perm1[loc], perm1[sloc] = p0, p1
            transCount += 1

    return (transCount % 2) == 0

def inverse_move(move):
    if len(move) == 2:
        return move[0]
    return move + "'"

def inverse_moves(moves):
    return [inverse_move(move) for move in moves[::-1]]

def apply_move(state, move):
    return ''.join([state[moves[move][x]] for x in range(24)])

def apply_moves(state, moves):
    new_state = state
    for move in moves:
        new_state = apply_move(new_state, move)
    return new_state

def solve(state, solved, moveset):
    front_states = [[state, []]]
    back_states = [[solved, []]]
    previous_front_states = [state]
    previous_back_states = [solved]
    while True:
        # front
        new_front_states = []
        for state, moves in front_states:
            for move in moveset:
                new_state = apply_move(state, move)
                if new_state not in previous_front_states:
                    previous_front_states.append(new_state)
                    new_front_states.append([new_state, moves + [move]])
        front_states = new_front_states
        # sprawdzanie
        solutions = []
        for fstate, fmoves in front_states:
            for bstate, bmoves in back_states:
                if fstate == bstate:
                    solutions.append(fmoves + inverse_moves(bmoves))
        if solutions:
            return solutions
        # back
        new_back_states = []
        for state, moves in back_states:
            for move in moveset:
                new_state = apply_move(state, move)
                if new_state not in previous_back_states:
                    previous_back_states.append(new_state)
                    new_back_states.append([new_state, moves + [move]])
        back_states = new_back_states
        # sprawdzanie
        solutions = []
        for fstate, fmoves in front_states:
            for bstate, bmoves in back_states:
                if fstate == bstate:
                    solutions.append(fmoves + inverse_moves(bmoves))
        if solutions:
            return solutions

all_cases = {}
# permutacja
for permutation in itertools.permutations(range(5)):
    # parity
    if arePermsEqualParity(permutation, list(range(5))):
        # orientacja
        for orientation in itertools.product([0,1], [0,1], [0,1], [0,1], [0,1]):
            # parity
            if sum(orientation) % 2 == 0:
                solved_list = ['g'] * 6 + ['b'] * 6 + ['r'] * 6 + ['y'] * 6
                for edge in range(5):
                    edge_pos = edge_positions[edge]
                    current_edge_colors = edge_colors[permutation[edge]]
                    if orientation[edge]:
                        current_edge_colors = current_edge_colors[::-1]
                    solved_list[edge_pos[0]] = current_edge_colors[0]
                    solved_list[edge_pos[1]] = current_edge_colors[1]
                scrambled_state = ''.join(solved_list)
                print(scrambled_state)
                print(permutation, orientation)
                # RLUB
                time_start = time()
                rlub_solutions = solve(scrambled_state, solved, RLUB)
                print("RLUB: ", rlub_solutions)
                print(time() - time_start)
                # RLU
                time_start = time()
                rlu_solutions = solve(scrambled_state, solved, RLU)
                print("RLU: ", rlu_solutions)
                print(time() - time_start)
                all_cases[scrambled_state] = [permutation, orientation, rlub_solutions, rlu_solutions]

f = open('5cycle.pickle', 'wb')
pickle.dump(all_cases, f)
f.close()