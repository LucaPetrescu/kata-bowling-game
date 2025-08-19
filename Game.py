class Game:

    def __init__(self):
        self.current_roll = 0 
        self.rolls = []

    def roll(self, pins_down):
        self.rolls.append(pins_down)
        self.current_roll += 1
    
    def score(self):
        score = 0
        cursor = 0
        for _ in range(10):
            if self.is_spare(cursor) == True:
                score += 10 + self.rolls[cursor + 2]
                cursor += 2
            elif self.is_strike(cursor) == True:
                score += 10 + self.rolls[cursor + 1] + self.rolls[cursor + 2]
                cursor += 1
            else:
                score += self.rolls[cursor] + self.rolls[cursor + 1]
                cursor += 2
        return score
    
    def is_spare(self, cursor):
        return (self.rolls[cursor] + self.rolls[cursor + 1] == 10)    

    def is_strike(self, cursor):
        return self.rolls[cursor] == 10