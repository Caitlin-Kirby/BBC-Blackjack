# Class for a player object. It contains the hand and the data which is used at the end to work out a winner
class Player:
    def __init__(self, number):
        self.hand = None # Hand object of card objects. The player is given one hand which is altered as the game is played
        self.number = number # Player id number to distinguish them
        self.final_score = 0 # Score when the player chooses to stand
        self.standing = False # Boolean if they player is standing or not
    
    
    # Hitting during play. Adds a card to the hand. The new score is calculted within the hand object class
    def hit(self, card):
        self.hand.add_card(card)
        
    # Stand during play. Set the final score for the current hand
    def stand(self): # Set final score
        self.final_score = self.hand.calculate_final_score()
        self.standing = True
    
    
    # -- Getters --
    def get_final_score(self):
        return self.final_score
    
    def get_number(self):
        return self.number
    
    def get_hand(self):
        return self.hand
    
    def get_standing(self):
        return self.standing
    
    
    # -- Setters --
    def set_number(self, num):
        self.number = num
    
    def set_hand(self, hand):
        self.hand = hand
    

    
    
    
    