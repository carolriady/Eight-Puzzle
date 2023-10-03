#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   


from searcher import *


def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, param):
    """open the file with the specified filename for reading, and it should
        use a loop to process the file one line at a time. In addition, the
        function should perform the cumulative computations needed to 
        report the following summary statistics after processing the entire 
        file
    """
    file = open(filename, 'r')
        
    solved = 0
    moves = 0
    tested_states = 0
        
    for line in file:
        line = line[:-1]
        init_board = Board(line)
        s = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        if searcher == None:
            return
        
        soln = None
        try:
            soln = searcher.find_solution(s)
        except KeyboardInterrupt:
            print(line + ":", 'search terminated, ', end='')
            
        if soln == None:
            print('no solution')
        else:
            print(line + ':', soln.num_moves, 'moves,', searcher.num_tested, 'states tested')
            solved += 1
            moves += soln.num_moves
            tested_states += searcher.num_tested
            
    print()        
    print('solved', solved, 'puzzles')
    if solved != 0:
        print('averages:', moves / solved, 'moves,', tested_states / solved, 'states tested')
        
            