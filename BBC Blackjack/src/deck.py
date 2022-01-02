import random
from src.card import Card
from src.hand import Hand

# Deck class - Holds all things which need the cards from the deck directly
class Deck:
    # The deck is initialised in order of the suits (diamonds, clubs, hearts, spades) from ace to king
    def __init__(self):
        self.cards = [] # List of card objects
                
        # Diamonds, clubs, hearts, spades
        suits = ["♦", "♣", "♥", "♠"]
        
        # 4 suits need to be created
        for i in range(4):
            suit = suits[i]
            # 13 cards within each suit
            for j in range(1, 14):
                if(j == 1): # Assign number 1 to Aces
                    number = "A"
                elif(j == 11): # 11 is jacks
                    number = "J"
                elif(j == 12): # 12 is queens
                    number = "Q"
                elif(j == 13): # 13 is kings
                    number = "K"
                else: # every other number is itself
                    number = str(j)
                # Create the card object
                card = Card(suit, number)
                self.cards.append(card)
        
        
    # Shuffle the cards object created by the constructor.
    def shuffle(self):
        random.shuffle(self.cards)


    # Create a hand object, deal the player parameter 2 cards from the deck
    def deal_initial_hand(self, player):
        hand = Hand() # New hand object created
        cards = [] # List of card objects created
        for x in range(2): # Hand size of 2
            card = self.draw_card()
            cards.append(card)
            
        hand.set_initial_cards(cards) # Set the cards in the hand
        player.set_hand(hand) # Give the player the hand object
    
    
    # Take the last card from the deck - the "top card"
    def draw_card(self):
        card = self.cards[len(self.cards)-1]
        self.cards.remove(card) # Remove card from deck as it's been dealt out
        return card
    
    
    # -- Getters --
    
    def get_cards(self):
        return self.cards
 
                