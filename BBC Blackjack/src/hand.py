# Class which holds the card objects for a complete hand and amends the hand during play
class Hand:
    def __init__(self):
        self.cards = [] # List of card objects which make up the hand
        self.scores = [] # List of integers which represent the possible scores for a hand. This array being empty indicates a bust hand
        self.bust = False # Boolean for a bust hand

    
    # When the cards are set, the score is calculated at the same time
    def set_initial_cards(self, cards):
        self.cards = cards
        self.calculate_score()
        
    # Adding a card to the hand and score recalculation
    def add_card(self, card):
        self.cards.append(card)
        # Clear the previous scores as they are no longer valid for the current hand
        self.scores = []
        self.calculate_score()
        
    # Work out the score of the hand given the cards within it
    #   The score is an array of scores due to Aces having more than one value in given situations
    def calculate_score(self):
        base_score = 0
        # The number of aces present in the hand
        ace_count = 0
        # Iterate over every card, adding up the numbers present to get a value of the hand
        for card in self.cards:
            # Record number of aces present
            if(card.get_number() == "A"):
                ace_count += 1
            # Sum the value of cards within the hand
            base_score += card.get_value()
            
            
        # Hand has been assessed so now we calculate the Ace affect on the hand
        if(ace_count != 0):
            # There are exclusively 2 options regardless of number of aces as every other outcome will exceed 21
            option1 = base_score + (ace_count*1)
            option2 = base_score + (ace_count*1) + 10
            # Only add the options to the list if they are valid scores
            if(option1 <= 21):
                self.scores.append(option1)
            if(option2 <= 21):
                self.scores.append(option2)    
        else:
            # No aces so there would only be one score
            if(base_score <= 21): # Only add if valid
                self.scores.append(base_score)
                
        # Set bust if there are no valid scores for the hand
        if(len(self.scores) == 0):
            self.bust = True
        
        
    # Display the current hand in a nicely formatted way
    def display_hand(self):
        print("Hand: ", end = "")
        for x in range(len(self.cards)):
            card = self.cards[x]
            if(x == len(self.cards)-1):
                print(card.to_string())
            else:
                print(card.to_string() + ", ", end="")
        
        
    # Best score will always be the highest from the options
    def calculate_final_score(self):
        return max(self.scores)
    
        
    # -- Getters --
    
    def get_cards(self):
        return self.cards
    
    def get_scores(self):
        return self.scores
    
    def get_bust(self):
        return self.bust
    
    
    