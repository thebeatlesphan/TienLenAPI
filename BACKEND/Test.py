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

    def test_get_hand_type(self):
        # test case 1
        test_hand_1 = [
            Card("Two", "Hearts")
        ]
        expected_singles_hand_1 = self.game.get_hand_type(test_hand_1)
        self.assertEqual(expected_singles_hand_1, (True, 'singles'))

        # test case 2
        test_hand_2 = [
            Card("Two", "Diamonds"),
            Card("Two", "Hearts")
        ]
        expected_pairs_hand_2 = self.game.get_hand_type(test_hand_2)
        self.assertEqual(expected_pairs_hand_2, (True, "pairs"))

        # test case 3
        test_hand_3 = [
            Card("Two", "Diamonds"),
            Card("Three", "Hearts")
        ]
        expected_pairs_hand_3 = self.game.get_hand_type(test_hand_3)
        self.assertEqual(expected_pairs_hand_3, (False, "Invalid hand type"))

        # test case 4
        test_hand_4 = [
            Card("Two", "Diamonds"),
            Card("Three", "Hearts"),
            Card("Four", "Spades")
        ]
        expected_pairs_hand_4 = self.game.get_hand_type(test_hand_4)
        self.assertEqual(expected_pairs_hand_4, (False, "Cannot play twos"))

        # test case 5
        test_hand_5 = [
            Card("Five", "Clubs"),
            Card("Five", "Diamonds"),
            Card("Five", "Hearts")
        ]
        expected_pairs_hand_5 = self.game.get_hand_type(test_hand_5)
        self.assertEqual(expected_pairs_hand_5, (True, "triples"))

        # test case 6
        test_hand_6 = [
            Card("Five", "Clubs"),
            Card("Five", "Diamonds"),
            Card("Five", "Hearts")
        ]
        expected_pairs_hand_6 = self.game.get_hand_type(test_hand_6)
        self.assertEqual(expected_pairs_hand_6, (True, "triples"))

        # test case 7
        test_hand_7 = [
            Card("Five", "Spades"),
            Card("Five", "Clubs"),
            Card("Five", "Diamonds"),
            Card("Five", "Hearts")
        ]
        expected_pairs_hand_7 = self.game.get_hand_type(test_hand_7)
        self.assertEqual(expected_pairs_hand_7, (True, "quads"))

        # test case 8
        test_hand_8 = [
            Card("Five", "Spades"),
            Card("Five", "Clubs"),
            Card("Six", "Spades"),
            Card("Six", "Clubs"),
            Card("Seven", "Diamonds"),
            Card("Seven", "Hearts"),
            Card("Eight", "Spades"),
            Card("Eight", "Hearts")
        ]
        expected_pairs_hand_8 = self.game.get_hand_type(test_hand_8)
        self.assertEqual(expected_pairs_hand_8, (True, "double straight"))

        # test case 9
        test_hand_9 = [
            Card("King", "Spades"),
            Card("King", "Clubs"),
            Card("Ace", "Diamonds"),
            Card("Ace", "Hearts"),
            Card("Two", "Clubs"),
            Card("Two", "Hearts")
        ]
        expected_pairs_hand_9 = self.game.get_hand_type(test_hand_9)
        self.assertEqual(expected_pairs_hand_9, (True, "double straight"))

        # test case 10
        test_hand_10 = [
            Card("Three", "Spades"),
            Card("Four", "Clubs"),
            Card("Five", "Diamonds"),
            Card("Seven", "Hearts"),
            Card("Eight", "Clubs"),
            Card("Nine", "Hearts")
        ]
        expected_pairs_hand_10 = self.game.get_hand_type(test_hand_10)
        self.assertEqual(expected_pairs_hand_10, (False, "Invalid hand type"))

        # test case 11
        test_hand_11 = [
            Card("Four", "Spades"),
            Card("Five", "Clubs"),
            Card("Six", "Diamonds"),
            Card("Seven", "Hearts"),
            Card("Eight", "Clubs"),
            Card("Nine", "Hearts")
        ]
        expected_pairs_hand_11 = self.game.get_hand_type(test_hand_11)
        self.assertEqual(expected_pairs_hand_11, (True, "straight"))

        # test case 12
        test_hand_12 = [
            Card("Six", "Spades"),
            Card("Six", "Diamonds"),
            Card("Seven", "Clubs"),
            Card("Seven", "Hearts"),
        ]
        expected_pairs_hand_12 = self.game.get_hand_type(test_hand_12)
        self.assertEqual(expected_pairs_hand_12, (False, "Invalid hand type"))

        # test case 13
        test_hand_13 = [
            Card("Queen", "Hearts"),
            Card("King", "Spades"),
            Card("Ace", "Spades"),
            Card("Two", "Diamonds")
        ]
        expected_pairs_hand_13 = self.game.get_hand_type(test_hand_13)
        self.assertEqual(expected_pairs_hand_13, (False, "Cannot play twos"))

    def test_is_higher_suit(self):
        # test case 1
        test_card_1 = Card("Four", "Diamonds")
        test_card_2 = Card("Four", "Hearts")
        expected_comparison_1_2 = self.game.is_higher_suit(
            test_card_1, test_card_2)
        self.assertEqual(expected_comparison_1_2, False)

        # test case 2
        test_card_3 = Card("Four", "Hearts")
        test_card_4 = Card("Four", "Diamonds")
        expected_comparison_3_4 = self.game.is_higher_suit(
            test_card_3, test_card_4)
        self.assertEqual(expected_comparison_3_4, True)

        # test case 3
        test_card_5 = Card("Five", "Hearts")
        test_card_6 = Card("Four", "Diamonds")
        expected_comparison_5_6 = self.game.is_higher_suit(
            test_card_5, test_card_6)
        self.assertEqual(expected_comparison_5_6,
                         (False, "Cards not same rank"))

    def test_is_valid_play(self):
        # test case 1
        test_intended_play_1 = [Card("Six", "Spades"),]
        test_last_hand_1 = [Card("Six", "Diamonds"),]
        expected_result_1 = self.game.is_valid_play(
            test_intended_play_1, test_last_hand_1)
        self.assertEqual(expected_result_1, False)

        # test case 2
        test_intended_play_2 = [
            Card("Six", "Spades"),
            Card("Six", "Hearts"),
        ]
        test_last_hand_2 = [
            Card("Six", "Clubs"),
            Card("Six", "Diamonds"),
        ]
        expected_result_2 = self.game.is_valid_play(
            test_intended_play_2, test_last_hand_2)
        self.assertEqual(expected_result_2, True)

        # test case 3
        test_intended_play_3 = [
            Card("Six", "Spades"),
            Card("Six", "Diamonds"),
            Card("Six", "Hearts"),
        ]
        test_last_hand_3 = [
            Card("Two", "Clubs"),
            Card("Two", "Diamonds"),
            Card("Two", "Hearts"),
        ]
        expected_result_3 = self.game.is_valid_play(
            test_intended_play_3, test_last_hand_3)
        self.assertEqual(expected_result_3, False)

        # test case 4
        test_intended_play_4 = [
            Card("Six", "Spades"),
            Card("Seven", "Diamonds"),
            Card("Eight", "Diamonds"),
        ]
        test_last_hand_4 = [
            Card("Six", "Clubs"),
            Card("Seven", "Spades"),
            Card("Eight", "Hearts"),
        ]
        expected_result_4 = self.game.is_valid_play(
            test_intended_play_4, test_last_hand_4)
        self.assertEqual(expected_result_4, False)

    def test_get_number_of_twos(self):
        # test case 1
        test_hand_1 = [
            Card("Three", "Spades"),
        ]
        expected_count_1 = self.game.get_number_of_twos(test_hand_1)
        self.assertEqual(expected_count_1, 0)

        # test case 2
        test_hand_2 = [
            Card("Two", "Spades"),
        ]
        expected_count_2 = self.game.get_number_of_twos(test_hand_2)
        self.assertEqual(expected_count_2, 1)

        # test case 3
        test_hand_3 = [
            Card("Ace", "Diamonds"),
            Card("Two", "Spades"),
            Card("Two", "Clubs"),
        ]
        expected_count_3 = self.game.get_number_of_twos(test_hand_3)
        self.assertEqual(expected_count_3, 2)

        # test case 4
        test_hand_4 = [
            Card("Two", "Spades"),
            Card("Two", "Clubs"),
            Card("Two", "Diamonds"),
        ]
        expected_count_4 = self.game.get_number_of_twos(test_hand_4)
        self.assertEqual(expected_count_4, 3)

        # test case 5
        test_hand_5 = [
            Card("Two", "Spades"),
            Card("Two", "Clubs"),
            Card("Two", "Diamonds"),
            Card("Two", "Hearts"),
        ]
        expected_count_5 = self.game.get_number_of_twos(test_hand_5)
        self.assertEqual(expected_count_5, 4)

        # test case 6
        test_hand_6 = [
            Card("Ten", "Spades"),
            Card("Two", "Spades"),
            Card("Two", "Clubs"),
            Card("Two", "Diamonds"),
            Card("Two", "Hearts"),
        ]
        expected_count_6 = self.game.get_number_of_twos(test_hand_6)
        self.assertEqual(expected_count_6, 4)


if __name__ == '__main__':
    unittest.main()
