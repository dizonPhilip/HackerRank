import unittest
from queens_attack_ii import queensAttack, get_direction_of_obstacle

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

    def test_get_direction_of_n_obstacle(self):
        test_case = {
            "r_q": 3,
            "c_q": 3,
            "obstacle": (1,3),
        }
        direction = get_direction_of_obstacle(**test_case)
        self.assertEqual("n", direction)
    
    def test_get_direction_of_ne_obstacle(self):
        test_case = {
            "r_q": 3,
            "c_q": 3,
            "obstacle": (2,4),
        }
        direction = get_direction_of_obstacle(**test_case)
        self.assertEqual("ne", direction)

    def test_get_direction_of_e_obstacle(self):
        test_case = {
            "r_q": 3,
            "c_q": 3,
            "obstacle": (3,4),
        }
        direction = get_direction_of_obstacle(**test_case)
        self.assertEqual("e", direction)

    def test_get_direction_of_se_obstacle(self):
        test_case = {
            "r_q": 3,
            "c_q": 3,
            "obstacle": (4,4),
        }
        direction = get_direction_of_obstacle(**test_case)
        self.assertEqual("se", direction)

    def test_get_direction_of_s_obstacle(self):
        test_case = {
            "r_q": 3,
            "c_q": 3,
            "obstacle": (4,3),
        }
        direction = get_direction_of_obstacle(**test_case)
        self.assertEqual("s", direction)

    def test_get_direction_of_sw_obstacle(self):
        test_case = {
            "r_q": 3,
            "c_q": 3,
            "obstacle": (4,2),
        }
        direction = get_direction_of_obstacle(**test_case)
        self.assertEqual("sw", direction)

    def test_get_direction_of_w_obstacle(self):
        test_case = {
            "r_q": 3,
            "c_q": 3,
            "obstacle": (3,2),
        }
        direction = get_direction_of_obstacle(**test_case)
        self.assertEqual("w", direction)

    def test_get_direction_of_nw_obstacle(self):
        test_case = {
            "r_q": 3,
            "c_q": 3,
            "obstacle": (1,1),
        }
        direction = get_direction_of_obstacle(**test_case)
        self.assertEqual("nw", direction)

if __name__ == "__main__":
    unittest.main()