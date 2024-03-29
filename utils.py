import random


n = int(input('n * n?:'))
r = input('random?:')

game_map = []
character_moves = []
character_position = [0,0]
max_n = n
trap_1_row = 0
trap_1_element = 0
is_random = True


def generate_board():    
    for _ in range(n):
        game_map.append([])
        for _ in range(n):
            game_map[-1].append('0')

    game_map[0][0] = '1'

generate_board()

def print_map(game_map,info=None):
    """print game map with information we found"""
    print('\n','-'*25,info,'-'*25)
    for row in game_map:
        for element in row:
            print(element,end='\t')
        print('\n')

def create_danger_place():
    """create randome trap place"""
    danger_place_row = random.randint(0,max_n-1)
    danger_place_element = random.randint(0,max_n-1)
    return check_danger_place(danger_place_row,danger_place_element)

def create_treasure_place():
    """create randome treasure place"""
    treasure_place_row = random.randint(0,max_n-1)
    treasure_place_element = random.randint(0,max_n-1)
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
    elif (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (max_n-2,0,max_n-1,1) and (row , element) == (max_n-1,0) or \
        (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (max_n-1,1,max_n-2,0) and (row , element) == (max_n-1,0) or \
        (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (0,max_n-2,1,max_n-1) and (row , element) == (0,max_n-1) or \
        (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (1,max_n-1,0,max_n-2) and (row , element) == (0,max_n-1) or \
        (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (max_n-2,max_n-1,max_n-1,max_n-2) and (row , element) == (max_n-1,max_n-1) or \
        (trap_2_row , trap_2_element ,trap_1_row , trap_1_element) == (max_n-1,max_n-2,max_n-2,max_n-1) and (row , element) == (max_n-1,max_n-1) :
        return create_treasure_place()
    else:
        return row,element

def move_player():
    global character_position

    # check player is not in bottom side of map and player down element is not Trap and not S
    if character_position[0] != max_n-1 and game_map[character_position[0] + 1][character_position[1]] != 'X' and \
        game_map[character_position[0] + 1][character_position[1]] != 'S' :

        # make a mark of previous step
        game_map[character_position[0]][character_position[1]] = 'S'
        
        # move player
        game_map[character_position[0] + 1][character_position[1]] = '1'

        # change player index
        character_position[0] += 1
        return 'down'
    
    # check player is not in right side of map and player right element is not Trap
    elif character_position[1] != max_n-1 and game_map[character_position[0]][character_position[1] + 1] != 'X' and \
        game_map[character_position[0]][character_position[1] + 1] != 'S' :



        # make a mark of previous step
        game_map[character_position[0]][character_position[1]] = 'S'
        
        # move player
        game_map[character_position[0]][character_position[1] + 1] = '1'

        # change player index
        character_position[1] += 1
        return 'right'

    # check player is not in up side of map and player up element is not Trap
    elif character_position[0] != 0 and game_map[character_position[0] - 1][character_position[1]] != 'X' and \
        game_map[character_position[0] - 1][character_position[1]] != 'S' :


        
        # make a mark of previous step
        game_map[character_position[0]][character_position[1]] = 'S'
        
        # move player
        game_map[character_position[0] - 1][character_position[1]] = '1'

        # change player index
        character_position[0] -= 1

        return 'up'
    
    # check player is not in left side of map and player left element is not Trap
    elif character_position[1] != 0 and game_map[character_position[0]][character_position[1] - 1] != 'X' and \
        game_map[character_position[0]][character_position[1] - 1] != 'S' :

        # make a mark of previous step
        game_map[character_position[0]][character_position[1]] = 'S'
        
        # move player
        game_map[character_position[0]][character_position[1] - 1] = '1'

        # change player index
        character_position[1] -= 1

        return 'left'

def move_player_back_until_find_new_path():
    global character_moves
    global character_position
    
    # make a mark of previous step
    game_map[character_position[0]][character_position[1]] = 'S'
    
    # move player
    game_map[character_moves[-1][0][0]][character_moves[-1][0][1]] = '1'
    character_position = [character_moves[-1][0][0],character_moves[-1][0][1]]
    character_moves.pop()
    # print_map(game_map,f'map with traps & treasure & {x} move')
    check_area()

def check_area():
    down = ''
    if character_position[0] != max_n-1:
        down =  game_map[character_position[0] + 1][character_position[1]]

    up = ''
    if character_position[0] != 0:
        up = game_map[character_position[0] - 1][character_position[1]]
    

    right = ''
    if character_position[1] != max_n-1:
        right = game_map[character_position[0]][character_position[1] + 1]

    left = ''
    if character_position[1] != 0:
        left =  game_map[character_position[0]][character_position[1] - 1]

    if down == '0' or up == '0' or right == '0' or left == '0':
        return ''
    else :
        move_player_back_until_find_new_path()  
    
def check_for_treasure():
    down = ''
    if character_position[0] != max_n-1:
        down =  game_map[character_position[0] + 1][character_position[1]]

    up = ''
    if character_position[0] != 0:
        up = game_map[character_position[0] - 1][character_position[1]]

    right = ''
    if character_position[1] != max_n-1:
        right = game_map[character_position[0]][character_position[1] + 1]

    left = ''
    if character_position[1] != 0:
        left =  game_map[character_position[0]][character_position[1] - 1]

    if down == '$' or up == '$'or right == '$' or left == '$':
        return 'win'
    else :
        return 'continue'       
print(n)
print(game_map)
if is_random : 
    # set first trap
    trap_1_row,trap_1_element = create_danger_place()
    game_map[trap_1_row][trap_1_element] = "X"


    # set second trap
    trap_2_row,trap_2_element = create_danger_place()
    game_map[trap_2_row][trap_2_element] = "X"


    # set treasure
    treasure_row,treasure_element = create_treasure_place()
    game_map[treasure_row][treasure_element] = "$"
