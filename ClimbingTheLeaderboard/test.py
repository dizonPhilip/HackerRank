import unittest
from climbing_the_leaderboard import climbingLeaderboard, generate_rankings, get_alices_ranking

class ClimbingTheLeaderboard(unittest.TestCase):
    def test_top_rank(self):
        scores = [50]
        alice = [100]
        self.assertEqual([1], climbingLeaderboard(scores, alice))

    def test_bottom_rank(self):
        scores = [50]
        alice = [40]
        self.assertEqual([2], climbingLeaderboard(scores, alice))

    def test_equal_rank(self):
        scores = [50]
        alice = [50]
        self.assertEqual([1], climbingLeaderboard(scores, alice))

    def test_multiple_alice_scores(self):
        scores = [90, 90, 50]
        alice = [40, 60, 90, 100]
        self.assertEqual([3, 2, 1, 1], climbingLeaderboard(scores, alice))

    def test_generate_rankings(self):
        scores = [100, 50]
        expected_rankings = {100: 1, 50: 2}
        rankings = generate_rankings(scores)
        self.assertEqual(expected_rankings, rankings)

    def test_generate_rankings_with_duplicates(self):
        scores = [100, 100, 50]
        expected_rankings = {100: 1, 50: 2}
        rankings = generate_rankings(scores)
        self.assertEqual(expected_rankings, rankings)

    def test_get_ranking_1(self):
        scores_in_ascending_order = [50, 100, 100]

        rankings = {100: 1, 50: 2}
        alices_score = 90
        rank = get_alices_ranking(scores_in_ascending_order, alices_score, rankings)
        self.assertEqual(2, rank)

if __name__ == "__main__":
    unittest.main()