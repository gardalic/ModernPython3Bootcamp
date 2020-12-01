import unittest
from deck_course import Deck, Card


class TestCard(unittest.TestCase):
    """Test the Card assignment"""
    def test_card_assignment(self):
        """Test if the card is being set correctly"""
        c = Card("Hearts", "Queen")
        self.assertEqual(str(c), "Queen of Hearts")

class TestDeck(unittest.TestCase):
    """Class to hold Deck tests"""
    def setUp(self):
        self.d = Deck()
        self.init_number = 52
    
    def test_count(self):
        """Check if the count method works, should return standard poker number of cards (52)."""
        self.assertEqual(self.d.count(), self.init_number)


    def test_card_deal_single(self):
        cur_deck = self.d.cards[:]
        card = self.d.deal_card()
        self.assertIn(card, cur_deck)
        self.assertNotIn(card, self.d.cards)
    
    def test_reset(self):
        """Check if the reset() method returns a full deck"""
        self.d.deal_card()
        self.assertNotEqual(self.d.count(), self.init_number)
        self.d.reset()
        self.assertEqual(self.d.count(), self.init_number)

    


if __name__ == "__main__":
    unittest.main()
