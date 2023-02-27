import random

game_map = [['1','0','0','0'],['0','0','0','0'],['0','0','0','0'],['0','0','0','0']] 

trap_1_row = 0
trap_1_element = 0
character_position = (0,0)

def print_map(game_map,info=None):
    """print game map with information we found"""
    print('\n','-'*25,info,'-'*25)
    for row in game_map:
        for element in row:
            print(element,end='\t')
        print('\n')

def create_danger_place():
    """create randome trap place"""
    danger_place_row = random.randint(0,3)
    danger_place_element = random.randint(0,3)
    return check_danger_place(danger_place_row,danger_place_element)

def create_treasure_place():
    """create randome treasure place"""
    treasure_place_row = random.randint(0,3)
    treasure_place_element = random.randint(0,3)
    return check_treasure_place(treasure_place_row,treasure_place_element)

def check_danger_place(row,element):
    """check random trap set in right place"""
    # check if is trap in starting point  
    if row == element == 0:
        return create_danger_place()
    # check two trap in one place situation
    elif row == trap_1_row and element == trap_1_element :
        return create_danger_place()
    # check must lose situation
    elif (row , element) == (0,1) and (trap_1_row , trap_1_element) == (1,0) or (row , element) == (1,0) and (trap_1_row , trap_1_element) == (0,1) :
        return create_danger_place()
    else:
        return row,element

def check_treasure_place(row,element):
    """check random treasure set in right place"""
    # check if is treasure in starting point  
    if row == element == 0:
        return create_treasure_place()
    # check treasure not set in trap
    elif (row , element) == (trap_1_row,trap_1_element) or (row , element) == (trap_2_row,trap_2_element):
        return create_treasure_place()
    
    # check treasure not set in corner and surroundby traps
    elif (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (2,0,3,1) and (row , element) == (3,0) or \
        (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (3,1,2,0) and (row , element) == (3,0) or \
        (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (0,2,1,3) and (row , element) == (0,3) or \
        (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (1,3,0,2) and (row , element) == (0,3) or \
        (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (2,3,3,2) and (row , element) == (3,3) or \
        (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (3,2,2,3) and (row , element) == (3,3) :
        return create_treasure_place()
    else:
        return row,element

def check_area():
    pass

trap_1_row,trap_1_element = create_danger_place()

# set first trap
game_map[trap_1_row][trap_1_element] = "X"

trap_2_row,trap_2_element = create_danger_place()

# set second trap
game_map[trap_2_row][trap_2_element] = "X"

if __name__ == '__main__':
    print_map(game_map,'map with traps')

treasure_row,treasure_element = create_treasure_place()

# set treasure
game_map[treasure_row][treasure_element] = "$"

if __name__ == '__main__':
    print_map(game_map,'map with traps & treasure')

