import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_game_created(self):
        f = Frame(1,5)
        game = BowlingGame()
        game.add_frame(f)
        self.assertEqual(f, game.get_frame_at(0))

    def test_game_with_multiple_frames(self):
        f1 = Frame(1, 5)
        f2 = Frame(2, 5)
        f3 = Frame(3, 5)
        f4 = Frame(4, 5)
        f5 = Frame(5, 5)
        f6 = Frame(6, 5)
        f7 = Frame(7, 5)
        f8 = Frame(8, 5)
        f9 = Frame(9, 5)
        f10 = Frame(10, 5)

        game = BowlingGame()
        game.add_frame(f1)
        game.add_frame(f2)
        game.add_frame(f3)
        game.add_frame(f4)
        game.add_frame(f5)
        game.add_frame(f6)
        game.add_frame(f7)
        game.add_frame(f8)
        game.add_frame(f9)
        game.add_frame(f10)

        self.assertEqual(f1, game.get_frame_at(0))
        self.assertEqual(f2, game.get_frame_at(1))
        self.assertEqual(f3, game.get_frame_at(2))
        self.assertEqual(f4, game.get_frame_at(3))
        self.assertEqual(f5, game.get_frame_at(4))
        self.assertEqual(f6, game.get_frame_at(5))
        self.assertEqual(f7, game.get_frame_at(6))
        self.assertEqual(f8, game.get_frame_at(7))
        self.assertEqual(f9, game.get_frame_at(8))
        self.assertEqual(f10, game.get_frame_at(9))

    def test_incorrect_get (self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at, 0)

    def test_game_with_too_may_frames(self):
        f1 = Frame(1, 5)
        f2 = Frame(2, 5)
        f3 = Frame(3, 5)
        f4 = Frame(4, 5)
        f5 = Frame(5, 5)
        f6 = Frame(6, 4)
        f7 = Frame(7, 3)
        f8 = Frame(8, 2)
        f9 = Frame(9, 1)
        f10 = Frame(10, 0)
        f11 = Frame(10, 5)

        game = BowlingGame()
        game.add_frame(f1)
        game.add_frame(f2)
        game.add_frame(f3)
        game.add_frame(f4)
        game.add_frame(f5)
        game.add_frame(f6)
        game.add_frame(f7)
        game.add_frame(f8)
        game.add_frame(f9)
        game.add_frame(f10)
        self.assertRaises(BowlingError, game.add_frame, f11)

    def test_calculate_score(self):
        game = BowlingGame()
        game.add_frame(Frame(1,5))
        game.add_frame(Frame(2,5))

        self.assertEqual(13, game.calculate_score())

    def test_calculate_score_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(5,5))
        game.add_frame(Frame(2,5))

        self.assertEqual(19, game.calculate_score())

    def test_calculate_score_spare_with_full_game(self):
        game = BowlingGame()

        game.add_frame(Frame(1,9))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        self.assertEqual(88, game.calculate_score())

    def test_calculate_score_strike_with_full_game(self):
        game = BowlingGame()

        game.add_frame(Frame(10,0))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))

        self.assertEqual(94, game.calculate_score())

    def test_calculate_empty_game(self):
        game = BowlingGame()

        self.assertEqual(0, game.calculate_score())
