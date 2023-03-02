from utils import *


if __name__ == '__main__':
    print_map(game_map,f'map with traps & treasure')

loop_count = 1
while loop_count < 1000:
    # check if player is win
    status = check_for_treasure()
    if  __name__ == '__main__' and status == 'win':
        print('\n','-'*25,status,'-'*25)
        break
    
    dir = move_player()

    if dir is None:
        move_player_back_until_find_new_path()
    else:
        character_moves.append([tuple(character_position),dir])
    
    if  __name__ == '__main__':
        print_map(game_map,f'map with traps & treasure & {loop_count} move')
    loop_count +=1
else:
    status = 'fail'
    print('\n','-'*25,status,'-'*25)
