import unittest
from src.deck import Deck
from src.player import Player
from src.hand import Hand
from src.card import Card


class DeckTestCase(unittest.TestCase):
    
    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.deck_check = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass


    def test_number_of_cards(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)
        
        
    # Ensure the deck shuffle makes the deck different from the original created deck
    def test_shuffle(self):
        self.deck.shuffle() # Shuffle the original deck
        
        unshuffled_deck = self.deck_check.get_cards()
        shuffled_deck = self.deck.get_cards()
        
        self.assertNotEqual(unshuffled_deck, shuffled_deck)
        
        
    # Ensure the initial hand size is 2
    def test_hand_size(self):
        player = Player("1") # We create a player with the number 1
        self.deck.deal_initial_hand(player)
        self.assertEqual(len(player.get_hand().get_cards()), 2)
        
        
    # Method to rest if the player recieves the top card from the deck after hitting
    def test_hit(self):
        # Setup a hand which we will give the player
        cards = [Card("♦", "5"), Card("♦", "7")]
        starting_hand = Hand()
        starting_hand.set_initial_cards(cards)
        
        # Set the deck manually so we can control what card comes up
        self.deck.cards = [Card("♦", "6")] 
        
        # Setup the player
        player = Player("1")
        player.set_hand(starting_hand)
        
        # Draw the top card and deal it to the player
        card = self.deck.draw_card()
        player.hit(card) 
        
        # Manually add the card to the copy hand
        man_hand = starting_hand
        man_hand.add_card(Card("♦", "6"))
        
        # Both hands should be equal
        self.assertEqual(player.get_hand(), man_hand)
       
       
    # Method to ensure the player has their final score calculated correctly 
    def test_stand(self):
        # Set the hand so we know what we're comparing against
        cards = [Card("♦", "5"), Card("♦", "7")]
        starting_hand = Hand()
        starting_hand.set_initial_cards(cards)
        # Set the player hand
        player = Player("1")
        player.set_hand(starting_hand)
        # The method under test
        player.stand()

        self.assertEqual(player.get_final_score(), 12)
        
    
    def test_higher_than_21(self):
        # Hand sums to 22 so get_bust should return true as they are bust
        cards = [Card("♦", "5"), Card("♦", "5"), Card("♥", "5"), Card("♠", "7")]
        starting_hand = Hand()
        starting_hand.set_initial_cards(cards)
        
        player = Player("1")
        player.set_hand(starting_hand)
        
        self.assertEqual(player.get_hand().get_bust(), True)
        
        
    def test_less_than_21(self):
        # Hand sums to 10 so get_bust should return False as they are not bust
        cards = [Card("♦", "5"), Card("♦", "5")]
        starting_hand = Hand()
        starting_hand.set_initial_cards(cards)
        
        player = Player("1")
        player.set_hand(starting_hand)
        
        self.assertEqual(player.get_hand().get_bust(), False)
        
        
    def test_check_ace_and_king(self):
        cards = [Card("♦", "K"), Card("♦", "A")]
        starting_hand = Hand()
        starting_hand.set_initial_cards(cards)
        
        player = Player("1")
        player.set_hand(starting_hand)
        player.stand() # We stand to solidify our best score
        
        self.assertEqual(player.get_final_score(), 21)
        
        
    def test_check_ace_queen_and_king(self):
        cards = [Card("♦", "K"), Card("♦", "Q"), Card("♦", "A")]
        starting_hand = Hand()
        starting_hand.set_initial_cards(cards)
        
        player = Player("1")
        player.set_hand(starting_hand)
        player.stand() # We stand to solidify our best score
        
        self.assertEqual(player.get_final_score(), 21)
        
    
    def test_check_ace_ace_and_nine(self):
        cards = [Card("♦", "A"), Card("♦", "A"), Card("♦", "9")]
        starting_hand = Hand()
        starting_hand.set_initial_cards(cards)
        
        player = Player("1")
        player.set_hand(starting_hand)
        player.stand() # We stand to solidify our best score
        
        self.assertEqual(player.get_final_score(), 21)
        
        

if __name__ == '__main__':
    unittest.main()
