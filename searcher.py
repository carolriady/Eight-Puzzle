#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """

    def __init__(self, depth_limit):
        """constructor for Searcher objects
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit
        
    def add_state(self, new_state):
        """takes a single State object called new_state and adds it to the 
            Searcher‘s list of untested states
        """
        self.states += [new_state]
    
    def should_add(self, state):
        """takes a State object called state and returns True if the called 
            Searcher should add state to its list of untested states, and False
            otherwise
        """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else: 
            return True
    
    def add_states(self, new_states):
        """takes a list State objects called new_states, and that processes the
            elements of new_states one at a time as follows
        """
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)
                
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
        
    def find_solution(self, init_state):
        """performs a full state-space search that begins at the specified 
            initial state init_state and ends when the goal state is found or 
            when the Searcher runs out of untested states
        """
        self.add_state(init_state)
    
        while self.states != []:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())
                
        return None
        
    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
  
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


class BFSearcher(Searcher):
    """a class for searcher objects that perform breadth-first search (BFS) 
        instead of random search
    """
    def next_state(self):
        """follows FIFO (first-in first-out) ordering – choosing the state that
            has been in the list the longest, removing it from the list before 
            returning it
        """
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    """a class for searcher objects that perform depth-first search (DFS) 
        instead of random search
    """
    def next_state(self):
        """follows LIFO (last-in first-out) ordering – choosing the state that
            was most recently added to the list, removing it from the list before 
            returning it
        """
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0


def h1(state):
    """a heuristic function that returns an estimate of how many additional 
        moves are needed to get from state to the goal state
    """
    return state.board.num_misplaced()

def h2(state):
    """a heuristic function that returns an estimate of"""
    count = 0 
    g_string = '012345678'

    for r in range(len(state.board.tiles)):
        for c in range(len(state.board.tiles[0])):
            if state.board.tiles[r][c] == '0':
                count
            elif state.board.tiles[r][c] != GOAL_TILES:
                if state.board.tiles[r][c] not in GOAL_TILES[r]:
                    count += 1
                if state.board.tiles[r][c] not in g_string[c::3]:
                    count += 1
                    
    return count
    

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    
  
    def __init__(self, heuristic):
        """constructor for GreedySearcher objects
        """
        super().__init__(-1)
        
        self.heuristic = heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    def add_state(self, state):
        """adds a sublist that is a [priority, state] pair, where priority is 
            the priority of state that is determined by calling the priority 
            method
        """
        self.states += [[self.priority(state), state]]

    def next_state(self):
        """chooses one of the states with the highest priority, returns the 
            state component of the sublist
        """
        s = max(self.states)
        self.states.remove(s)
        return s[-1]


class AStarSearcher(GreedySearcher):
    """a class for searcher objects that perform A* search
    """
    def priority(self, state):
        """computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher and number of 
            moves from the initial state
        """
        return -1 * (self.heuristic(state) + state.num_moves)