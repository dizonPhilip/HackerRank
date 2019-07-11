import unittest
import unittest.mock
import io
from staircase import staircase

class ClimbingTheLeaderboard(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        staircase(n)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    def test_1(self):
        self.assert_stdout(1, "#\n")

    def test_2(self):
        self.assert_stdout(2, " #\n##\n")
    
    def test_3(self):
        self.assert_stdout(3, "  #\n ##\n###\n")

if __name__ == "__main__":
    unittest.main()