import copy
from search import *
import time
import threading

# TAI color
# sem cor = 0
# com cor > 0
def get_no_color():
    return 0
def no_color(c):
    return c==0
def color(c):
    return c > 0

# TAI pos
# Tuplo (l, c)
def make_pos(l, c):
    return (l, c)
def pos_l(pos):
    return pos[0]
def pos_c(pos):
    return pos[1]

# TAI group
# Lista de Tuplos (l, c)
def make_group():
    return []
def add_to_group(group, pos):
    return group + [pos]

# TAI board
# Lista de Listas de Tuplos (l, c)
def make_board():
    return []
def make_line():
    return []
def add_to_line(line, color):
    return line + [color]
def add_line(board, line):
    return board + [line]
def get_color(board, pos):
    return board[pos_l(pos)][pos_c(pos)]

def pos_exists(board, pos):
    height = len(board)
    width = len(board[0])
    if(0 <= pos_l(pos) < height and 0 <= pos_c(pos) < width):
        return True
    return False

def find_group(board, positions, group, pos):
    positions.remove(pos)
    group += [pos]
    color = board[pos_l(pos)][pos_c(pos)]
    #Up position#
    posUP = make_pos(pos_l(pos) - 1, pos_c(pos))
    if(pos_exists(board, posUP) and posUP in positions and color == board[pos_l(posUP)][pos_c(posUP)]):
        find_group(board, positions, group, posUP)
    #Down position#
    posDOWN = make_pos(pos_l(pos) + 1, pos_c(pos))
    if(pos_exists(board, posDOWN) and posDOWN in positions and color == board[pos_l(posDOWN)][pos_c(posDOWN)]):
        find_group(board, positions, group, posDOWN)
    #Left position#
    posLEFT = make_pos(pos_l(pos), pos_c(pos) - 1)
    if(pos_exists(board, posLEFT) and posLEFT in positions and color == board[pos_l(posLEFT)][pos_c(posLEFT)]):
        find_group(board, positions, group, posLEFT)
    #Right position#
    posRIGHT = make_pos(pos_l(pos), pos_c(pos) + 1)
    if(pos_exists(board, posRIGHT) and posRIGHT in positions and color == board[pos_l(posRIGHT)][pos_c(posRIGHT)]):
        find_group(board, positions, group, posRIGHT)
    if(group != [] and no_color(board[pos_l(group[0])][pos_c(group[0])])):
        group = []
    return group

def board_find_groups(board):
    groups = []
    positions = []
    i = 0
    for l in board:
        j = 0
        for c in l:
            positions += [make_pos(i, j)]
            j += 1
        i += 1
    while positions != []:
        groups += [find_group(board, positions, [], positions[0])]
    return groups
    
def board_remove_group(board_input, group):
    board = copy.deepcopy(board_input)
    for pos in group:
        board[pos_l(pos)][pos_c(pos)] = get_no_color()
    c = 0
    while c < len(board[0]):
        l = len(board) - 1
        while l >= 0:
            a = 1
            while no_color(board[l][c]) and l - a >= 0:
                board[l][c] = board[l - a][c]
                board[l - a][c] = get_no_color()
                a += 1
            l -= 1
        c += 1
        
    c = 0
    while c < len(board[0]):
        if no_color(board[len(board) - 1][c]):
            l = len(board) - 1
            a = 1
            while c + a < len(board[0]) and no_color(board[len(board) - 1][c + a]):
                a += 1
            while c + a < len(board[0]) and l >= 0:
                board[l][c] = board[l][c + a]
                board[l][c + a] = get_no_color()
                l -= 1
        c += 1
                
    return board

def count_colors(board):
    colors = []
    count = 0
    for line in board:
        for el in line:
            if el not in colors:
                colors += [el]
                count += 1
    return count
        
#TAI sg_state
class sg_state:
    def __init__(self, board):
        self.board = board
        self.colors = count_colors(board)
        self.groups = len(board_find_groups(board))
    def __hash__(self):
        final = []
        for line in self.board:
            for el in line:
                final += [el]
        final = tuple(final)
        return hash(final)
    def __eq__(self, other):
        return self.board == other.board
    def __lt__(self, other):
        total_self = random.random()
        total_other = random.random()            
        if total_other > total_self:
            return True
        else:
            return False
    
#TAI same_game
class same_game(Problem):
    def __init__(self, board):
        self.state = sg_state(board)
        ideal = []
        one_line = []
        for line in board:
            one_line = []
            for i in line:
                one_line += [0]
            ideal += [one_line]
        super().__init__(self.state, sg_state(ideal))
    
    def actions(self, state):
        groups = board_find_groups(state.board)
        solution = []
        for group in groups:
            if len(group) >= 2:
                solution += [group]
        return solution

    def result(self, state, action):
        return sg_state(board_remove_group(state.board, action))
    
    def h(self, node):
        return node.state.colors*node.state.groups
    
def depth_first_tree_search(problem):
    result = tree_search(problem, Stack())
    if result == None:
        result = []
    return result

def greedy_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    result = best_first_graph_search(problem, lambda n: h(n))
    if result == None:
        result = []
    return result

def astar_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    result = best_first_graph_search(problem, lambda n: n.path_cost + h(n))
    if result == None:
        result = []
    return result



def solve(boards, header, search):
    """
    a = InstrumentedProblem(same_game(board))
    start_time = time.time()
    b = greedy_search(a)
    print("GREEDY: --- %s seconds ---" % (time.time() - start_time))
    print(a)
    print("\n")
    
    a = InstrumentedProblem(same_game(board))
    start_time = time.time()
    b = astar_search(a)
    print(" ASTAR :--- %s seconds ---" % (time.time() - start_time))
    print(a)
    print("\n")
    
    a = InstrumentedProblem(same_game(board))
    start_time = time.time()
    b = depth_first_tree_search(a)
    print(" DFS :--- %s seconds ---" % (time.time() - start_time))
    print(a) 
    """
    compare_searchers(boards, "Hello")


    
    