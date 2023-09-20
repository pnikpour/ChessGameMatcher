class Game:
    moves = ''
    count = 0
    
    def __init__(self, moves, count):
        self.moves = moves
        self.count = count

    def tostring(self):
        return 'Moves\t' + self.moves + '\nCount\t' + str(self.count)
