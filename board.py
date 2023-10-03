#
# board.py (Final project)
#
# A Board class for the Eight Puzzle

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = digitstr[3*r + c]
                
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
  
    
    def __repr__(self):
        """returns the string representation of a Board object
        """
        s = ''
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == '0':
                    s += '_' + ' '
                else:
                    s += self.tiles[row][col] + ' '
                    
            s += '\n'

        return s
    
    def move_blank(self, direction):
        """returns True or False to indicate whether the requested move was 
            possible
        """
        blank_r = self.blank_r
        blank_c = self.blank_c
        
        if direction == 'up':
            if blank_r <= 0:
                return False
            else:
                blank_r -= 1
            
        elif direction == 'down':
            if blank_r >= 2:
                return False
            else:
                blank_r += 1
            
        elif direction == 'left':
            if blank_c <= 0:
                return False
            else:
                blank_c -= 1
            
        elif direction == 'right':
            if blank_c >= 2:
                return False
            else:
                blank_c += 1
        
        if direction in ['up', 'down', 'left', 'right']:      
            self.tiles[self.blank_r][self.blank_c] = self.tiles[blank_r][blank_c]
            self.tiles[blank_r][blank_c] = '0'
            self.blank_r = blank_r
            self.blank_c = blank_c
            return True
        
        return False
            
    def digit_string(self):
        """creates and returns a string of digits that corresponds to the 
            current contents of the called Board object’s tiles attribute
        """
        digits = ''
            
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == '_':
                    digits += '0'
                else:
                    digits += self.tiles[row][col]
                    
        return digits
    
    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of the 
            called object
        """
        copy = Board(self.digit_string())
        
        return copy
    
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object 
            that are not where they should be in the goal state
        """
        count = 0
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == '0':
                    count
                elif self.tiles[row][col] != GOAL_TILES[row][col]:
                    count += 1
        
        return count
                
    def __eq__(self, other):
        """return True if the called object (self) and the argument (other)
            have the same values for the tiles attribute, and False otherwise
        """
        if self.tiles == other.tiles:
            return True
        else:
            return False
        