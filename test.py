import unittest
from main import *

class TestTrap(unittest.TestCase):
    def test_first_trap(self):
        self.assertNotEqual((trap_1_row,trap_1_element),(0,0))

    
    def test_second_trap(self):
        self.assertNotEqual((trap_2_row,trap_2_element),(0,0))
        self.assertNotEqual((trap_2_row,trap_2_element),(trap_1_row,trap_1_element))
        self.assertEqual((trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (1,0,0,1))
        self.assertEqual((trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (0,1,1,0))




if __name__ == '__main__':
    unittest.main()
