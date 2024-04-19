import unittest
from TienLen import Card, Deck, Game


class TestTienLen(unittest.TestCase):

    def setUp(self):
        # Initialize the game
        self.game = Game()

    def test_sort_one_hand(self):
        # Test case 1
        test_hand_1 = [
            Card("Two", "Hearts"),
            Card("Two", "Diamonds")
        ]
        sorted_hand_1 = self.game.sort_one_hand(test_hand_1)
        expected_sorted_hand_1 = [
            Card("Two", "Diamonds"),
            Card("Two", "Hearts")
        ]
        self.assertEqual(sorted_hand_1, expected_sorted_hand_1)

        # Test case 2
        test_hand_2 = [
            Card("Two", "Diamonds"),
            Card("Two", "Hearts"),
            Card("Two", "Spades"),
            Card("Two", "Clubs")
        ]
        expected_sorted_hand_2 = [
            Card("Two", "Spades"),
            Card("Two", "Clubs"),
            Card("Two", "Diamonds"),
            Card("Two", "Hearts")
        ]
        sorted_hand_2 = self.game.sort_one_hand(test_hand_2)
        self.assertEqual(sorted_hand_2, expected_sorted_hand_2)

    def test_player_index_has_four_twos(self):
        # test case 1
        self.game.players.player1 = [Card("Two", "Diamonds"),
                                     Card("Two", "Hearts"),
                                     Card("Two", "Spades"),
                                     Card("Two", "Clubs")]
        self.game.players.player2 = []
        self.game.players.player3 = []
        self.game.players.player4 = []

        expected_player = self.game.player_index_has_four_twos()
        self.assertEqual(expected_player, 0)

        # test case 2
        self.game.players.player1 = []
        self.game.players.player2 = []
        self.game.players.player3 = []
        self.game.players.player4 = []

        expected_player = self.game.player_index_has_four_twos()
        self.assertEqual(expected_player, None)

        # test case 3
        self.game.players.player1 = []
        self.game.players.player2 = [Card("Two", "Diamonds"),
                                     Card("Two", "Hearts"),
                                     Card("Two", "Spades"),
                                     Card("Two", "Clubs")]
        self.game.players.player3 = []
        self.game.players.player4 = []

        expected_player = self.game.player_index_has_four_twos()
        self.assertEqual(expected_player, 1)

        # test case 4
        self.game.players.player1 = []
        self.game.players.player2 = []
        self.game.players.player3 = [Card("Two", "Diamonds"),
                                     Card("Two", "Hearts"),
                                     Card("Two", "Spades"),
                                     Card("Two", "Clubs")]
        self.game.players.player4 = []

        expected_player = self.game.player_index_has_four_twos()
        self.assertEqual(expected_player, 2)

        # test case 5
        self.game.players.player1 = []
        self.game.players.player2 = []
        self.game.players.player3 = []
        self.game.players.player4 = [Card("Two", "Diamonds"),
                                     Card("Two", "Hearts"),
                                     Card("Two", "Spades"),
                                     Card("Two", "Clubs")]

        expected_player = self.game.player_index_has_four_twos()
        self.assertEqual(expected_player, 3)


if __name__ == '__main__':
    unittest.main()
