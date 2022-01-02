import random
from src.player import Player

# A dealer which plays after the players all conclude their turns
# The dealer cards are shown and the players are working against the dealer
class Dealer(Player):
    def __init__(self):
        self.hand = None
        self.final_score = 0
        self.standing = False
    
    # The dealer will have a basic mechanic of probability when it comes to what total they have already
    def choose_move(self, deck):
        # Calculate the current value of their hand
        hand_value = max(self.hand.get_scores())
        # Never hit if you have 21 - you have the winning score
        if(hand_value == 21):
            self.stand()
        # Always hit if below 10 - you can draw any card without going bust
        elif(hand_value <= 10):
            card = deck.draw_card()
            self.hit(card)
        else:
            # Calculate an percentage which will dictate if a card is taken
            percentage = ((21 - hand_value) / 21)*100
            # Select a random number which will align with the percentages
            num = random.randint(1, 100)
            # If the random number is lower than the percentage, then we hit, otherwise we stand
            #   The lower the percentage, the better the hand currently is, so there is a much smaller chance that it is worth drawing a card
            if(num < percentage):
                card = deck.draw_card()
                self.hit(card)
            else:
                self.stand()
    
        