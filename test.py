import unittest
from main import *

class TestTrap(unittest.TestCase):
    def test_first_trap_place(self):
        self.assertNotEqual((trap_1_row,trap_1_element),(0,0))

    
    def test_second_trap_place(self):
        self.assertNotEqual((trap_2_row,trap_2_element),(0,0))
        self.assertNotEqual((trap_2_row,trap_2_element),(trap_1_row,trap_1_element))
        self.assertNotEqual((trap_2_row , trap_2_element ,trap_1_row , trap_1_element) , (1,0,0,1))
        self.assertNotEqual((trap_2_row , trap_2_element ,trap_1_row , trap_1_element) , (0,1,1,0))


    def test_treasure_place(self):
        if (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (2,0,3,1):
            self.assertEqual((treasure_row , treasure_element) , (3,0))
        if (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (0,2,1,3):
            self.assertEqual((treasure_row , treasure_element) , (3,0))
        if (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (0,2,1,3):
            self.assertEqual((treasure_row , treasure_element) , (0,3))
        if (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (1,3,0,2):
            self.assertEqual((treasure_row , treasure_element) , (0,3))
        if (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (2,3,3,2):
            self.assertEqual((treasure_row , treasure_element) , (3,3))
        if (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (3,2,2,3) :
            self.assertEqual((treasure_row , treasure_element) , (3,3))




if __name__ == '__main__':
    unittest.main()
