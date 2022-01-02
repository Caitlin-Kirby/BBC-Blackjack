from src.deck import Deck
from src.player import Player
from src.dealer import Dealer
import time

# Method to play the game!
def play():
    # Boolean to allow the player to play more than once
    playing = True
    while(playing):
        print("\nHello! Welcome to Blackjack.")
        # New deck method will construct and shuffle a deck ready for play
        deck = new_deck()
    
        # User input for how many people are playing
        num_players = determine_players()
        
        # This creates a list of player objects which are then used to play the game
        players = []
        for i in range(num_players):
            player = Player(str(i+1)) # Create the player with their number, as determiend by their position in the list
            players.append(player)
        
        # Create the dealer
        dealer = Dealer()
        deck.deal_initial_hand(dealer)
        dealer_hand = dealer.get_hand()
        
        # Deal a hand to every player in the list
        for player in players:
            deck.deal_initial_hand(player)
            
        
        # Loop over all players to play the game in turn
        for player in players:
            print("\nCurrent Player: Player " + str(player.get_number()))
            # Get the hand for the current player of the game
            current_hand = player.get_hand()
            # Keep hitting cards until you stand or you go bust
            hit = True
            while(hit):
                # Show the dealer hand 
                print("\nDealer ", end="")
                dealer_hand.display_hand()
                print("\n")
                # Show the current players hand 
                current_hand.display_hand()
                
                
                # Method returns true if the hand is bust
                if(current_hand.get_bust()):
                    print("You went bust! Better luck next time")
                    hit = False
                    continue
                
                # Display the scores from the current hand
                for score in current_hand.get_scores():
                    print("Score option: " + str(score))
                            
                # Player not bust so can draw cards, we check if they want to
                response = input("Would you like to hit or stand? ").lower().strip()
                
                # Stand - Stop drawing cards
                if(response == "stand"):
                    player.stand()
                    print("Your final score for this hand is : " + str(player.get_final_score()))
                    hit = False
                # Hit - Draw a card and loop around to see if you are bust or can draw again
                elif(response == "hit"):
                    card = deck.draw_card() # Get the card from the deck
                    player.hit(card)
                else:
                    # Response wasn't valid so they user is shown their hand and asked to try again
                    print("I didn't understand that, please try again.")
                    
                    
        # Resolve the dealer hand - loop over choose_move until they stand or go bust
        dealer_hand.display_hand()
        while(not dealer.get_hand().get_bust() and not dealer.get_standing()):
            dealer.choose_move(deck)
            time.sleep(1) # Time delay to add suspence and to make it seem like the dealer is thinking to the user
            dealer_hand.display_hand()
        
        # Display dealer results
        if(dealer.get_hand().get_bust()):
            print("Dealer went bust.")
        elif(dealer.get_standing()):
            print("Dealer standing")
        
        
        # Finish up and display the winners
        select_winner(players, dealer)
        # User input to play again
        good_response = False
        while(not good_response):
            loop = input("Thank you for playing! Would you like to play again? (y/n) ").lower().strip()
            if(loop == "n"):
                playing = False
                good_response = True
            elif(loop == "y"):
                print("Great! Good luck!")
                deck.player_scores = []
                good_response = True
            else:
                print("I didn't understand that, please try again.")
        


# This method makes a new deck, shuffles it, and returns the shuffled ready deck for the next game
def new_deck():
    deck = Deck()
    deck.shuffle()
    return deck
    
    
# Loop over a dialog with the user to get a valid number for the quantity of players
def determine_players():    
    players_confirm = False
    while(not players_confirm):
        num_players = input("How many players would like to play today? Please pick a number between 1 and 4.\n").strip()
        
        # Limit the game to 4 players
        if(num_players not in ["1", "2", "3", "4"]):
            print("That doesn't seem quite right. Please enter again making sure you enter a number between 1 and 4.")
            continue
       
        # Convert to int post check as otherwise incorrect characters will crash the program 
        num_players = int(num_players)

        # Check response for accurate number of players
        response_confirm = False
        while(not response_confirm):
            response = input("So we're playing with " + str(num_players) + " player(s) today, is that correct? (y/n)\n")
            response = response.lower().strip()
            if(response == "y"):
                print("Perfect. Onto the game!")
                response_confirm = True
                players_confirm = True
            elif(response == "n"):
                response_confirm = True
            else:
                print("Sorry, I didn't catch that. Please could you try again.")
                
    return num_players

# Take the players are select the winner, winners if there was a tie, or the dealer as winner
def select_winner(players, dealer):
       
    print("\nScores: ")
    winners = []
    winning_score = 0
    for player in players:
        player_score = player.get_final_score()
        # Display bust if they got a score of 0
        if(player_score == 0):
            text = "Bust"
        else:
            text = str(player_score)
        print("Player " + player.get_number() + ": " + text)
        
        if(player_score == winning_score and not player.get_hand().get_bust()):
            winners.append(player) # A draw
        elif(player_score > winning_score):
            winning_score = player_score
            winners = [] # Remove all previous winners
            winners.append(player) # Add this winner
    print("Dealer  : " + str(dealer.get_final_score()))
    # Determine if the dealer wins over the players
    dealer_win = False    
    if(dealer.get_hand().get_bust() == False):
        # Dealer still in, we check if they win or not
        if(len(winners) == 0 and dealer.get_standing() == True):
            dealer_win = True
        else:
            for win in winners:
                if(dealer.get_final_score() >= win.get_final_score()):
                    print("Dealer wins with a score of " + str(dealer.get_final_score()))
                    dealer_win = True
    # Dealer doesn't win, we display the winning player (or nobody if everybody went bust)  
    if(dealer_win == False):
        print("Final winners are: ")
        if(len(winners) == 0):
            print("Everybody went bust! Better luck next time")
        else:
            for win in winners:
                print("Player " + win.get_number())
            print("With a score of " + str(winning_score))
    

if __name__ == '__main__':
    play()
