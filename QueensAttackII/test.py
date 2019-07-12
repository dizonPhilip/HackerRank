import unittest
from queens_attack_ii import queensAttack, cleanup_obstacles

class QueensAttackIITest(unittest.TestCase):
    def test_1x1(self):
        test_case = {
            "n": 1,
            "k": 0,
            "r_q": 1,
            "c_q": 1,
            "obstacles": [],
        }
        num_attacks = queensAttack(**test_case)
        self.assertEqual(0, num_attacks)

    def test_1(self):
        test_case = {
            "n": 4,
            "k": 0,
            "r_q": 4,
            "c_q": 4,
            "obstacles": [],
        }
        num_attacks = queensAttack(**test_case)
        self.assertEqual(9, num_attacks)

    def test_2(self):
        test_case = {
            "n": 5,
            "k": 0,
            "r_q": 4,
            "c_q": 3,
            "obstacles": [],
        }
        num_attacks = queensAttack(**test_case)
        self.assertEqual(14, num_attacks)

    def test_5x5_with_horizontal_obstacles(self):
        test_case = {
            "n": 5,
            "k": 0,
            "r_q": 4,
            "c_q": 3,
            "obstacles": [(4,2), (4,4)],
        }
        num_attacks = queensAttack(**test_case)
        self.assertEqual(10, num_attacks)

    def test_5x5_with_vertical_obstacles(self):
        test_case = {
            "n": 5,
            "k": 0,
            "r_q": 4,
            "c_q": 3,
            "obstacles": [(5,3), (2,3)],
        }
        num_attacks = queensAttack(**test_case)
        self.assertEqual(11, num_attacks)

    def test_5x5_with_forward_diagonal_obstacles(self):
        test_case = {
            "n": 5,
            "k": 0,
            "r_q": 4,
            "c_q": 3,
            "obstacles": [(5,2), (3,4)],
        }
        num_attacks = queensAttack(**test_case)
        self.assertEqual(11, num_attacks)

    def test_5x5_with_backward_diagonal_obstacles(self):
        test_case = {
            "n": 5,
            "k": 0,
            "r_q": 4,
            "c_q": 3,
            "obstacles": [(5,4), (3,2)],
        }
        num_attacks = queensAttack(**test_case)
        self.assertEqual(11, num_attacks)

    def test_5x5_with_backward_diagonal_obstacles_and_superfluous(self):
        test_case = {
            "n": 5,
            "k": 0,
            "r_q": 4,
            "c_q": 3,
            "obstacles": [(5,4), (3,2), (2,1)],
        }
        num_attacks = queensAttack(**test_case)
        self.assertEqual(11, num_attacks)

    def test_cleanup_obstacles(self):
        test_case = {
            "r_q" : 6,
            "c_q" : 6,
            "obstacles" : [ (1,1), (2,2), (1,6), (2,6), (1,11), (2,10), (6,11), (6, 10), (11, 11), (10, 10), (11,6), (10,6), (11,1), (10,2), (6,1), (6,2)] 
        }
        filtered_obstacles = cleanup_obstacles(**test_case)
        self.assertEqual((2,2), filtered_obstacles["min_nw"])
        self.assertEqual((2,6), filtered_obstacles["min_n"])
        self.assertEqual((2,10), filtered_obstacles["min_ne"])
        self.assertEqual((6,10), filtered_obstacles["min_e"])
        self.assertEqual((10,10), filtered_obstacles["min_se"])
        self.assertEqual((10,6), filtered_obstacles["min_s"])
        self.assertEqual((10,2), filtered_obstacles["min_sw"])
        self.assertEqual((6,2), filtered_obstacles["min_w"])


if __name__ == "__main__":
    unittest.main()