# Card class, contains information about each card
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        
        # Calculate the value
        if(number == "A"):
            # Counted as 0 but then are looked into when the hand is evaluated as there are 2 options for Aces
            self.value = 0
        elif(number in ["J", "Q", "K"]):
            # Pictures are worth 10
            self.value = 10
        else:
            # Convert the number directly to an integer as it's value is correct already
            self.value = int(number)
            
            
    # To string method to nicely show each card's suit and number
    def to_string(self):
        return self.suit + self.number
    
    
    # -- Getters --
    
    def get_suit(self):
        return self.suit
    
    def get_number(self):
        return self.number
    
    def get_value(self):
        return self.value