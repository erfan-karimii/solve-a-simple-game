import unittest
from main import *

class TestTrap(unittest.TestCase):
    def test_first_trap_place(self):
        self.assertNotEqual((trap_1_row,trap_1_element),(0,0))

    
    def test_second_trap_place(self):
        self.assertNotEqual((trap_2_row,trap_2_element),(0,0))
        self.assertNotEqual((trap_2_row,trap_2_element),(trap_1_row,trap_1_element))
        self.assertNotEqual((game_map[0][1],game_map[1][0]),('X','X'))


    def test_treasure_place(self):
        self.assertNotEqual((game_map[3][2],game_map[3][3],game_map[2][3]),('X','$','X'))
        self.assertNotEqual((game_map[0][2],game_map[0][3],game_map[1][3]),('X','$','X'))
        self.assertNotEqual((game_map[2][0],game_map[3][0],game_map[3][1]),('X','$','X'))







if __name__ == '__main__':
    unittest.main()
