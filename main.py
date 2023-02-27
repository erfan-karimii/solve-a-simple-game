import random

game_map = [['1','0','0','0'],['0','0','0','0'],['0','0','0','0'],['0','0','0','0']] 

trap_1_row = 0
trap_1_element = 0

def print_map(game_map,info=None):
    """print game map with information we found"""
    print('-'*25,info,'-'*25)
    for row in game_map:
        print('\n')
        for element in row:
            print(element,end='\t')
    

def create_danger_place():
    """create randome trap place"""
    danger_place_row = random.randint(0,3)
    danger_place_element = random.randint(0,3)
    return check_danger_place(danger_place_row,danger_place_element)

def check_danger_place(row,element):
    """check random trap set in right place"""
    # check is trap in starting point  
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


trap_1_row,trap_1_element = create_danger_place()

# set first trap
game_map[trap_1_row][trap_1_element] = "X"

trap_2_row,trap_2_element = create_danger_place()

# set first trap
game_map[trap_2_row][trap_2_element] = "X"

if __name__ == '__main__':
    print_map(game_map,'map with traps')

