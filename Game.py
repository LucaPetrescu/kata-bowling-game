class Game:

    def __init__(self):
        self.game_score = 0;
    
    def roll(self, pins):
        self.game_score += pins
    
    def score(self):
        return self.game_score
    