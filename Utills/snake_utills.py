# PySnake Utills
# AMCocan
# 2.08.2023

# --- Imports ---
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Hides: 'Hello from the pygame community'

import pygame as pg
# import random as rn
# import time as tm
# import sys as sy

# --- main_process ---

def main_process(size, title, icon, ui_colors):

    # Initialize Pygame.
    pg.init()

    # Read agrs and build window.
    bgw = pg.display.set_mode(size)
    pg.display.set_caption(title)
    pg.display.set_icon(icon)

    # Set player size here.
    player_size = [10, 10]

    # Set the player initial position here.
    player_xpos_init = size[0]/2
    player_ypos_init = size[1]/2

    # Set player move index here.
    player_move_index = [[-5, 5], [-5, 5]]
    h_move_index = player_move_index[0]
    v_move_index = player_move_index[1]

    # Create list variable for player position.
    player_pos = [player_xpos_init, player_ypos_init]

    # Main process loop condition
    running = True

    # Create window and run main process here.
    while running:

        # Set the framerate here.
        frame_rate(60)

        # Set background color fill here.
        pg.Surface.fill(bgw, ui_colors['background'])

        # Key's event listener.
        keypress = pg.key.get_pressed()

        # Event listener for 'QUIT'
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif keypress[pg.K_ESCAPE]:
                running = False
            
            # Listen event for reset.
            if keypress[pg.K_r]:
                player_pos[0] = size[0]/2
                player_pos[1] = size[1]/2

        # Map edge detection called here.
        map_edge(player_pos, size, player_size, h_move_index, v_move_index)

        # Player movement called here.
        player_movement(keypress, running, h_move_index, v_move_index, player_pos)

        # Player render called here.
        player(bgw, ui_colors['player'], player_pos, player_size)
        
        # Update the screen.
        pg.display.flip()
    
    # Uninitialize everything and quit.
    pg.quit()
    quit()

# --- frame_rate ---
def frame_rate(x):

    # Set a static frame rate here.
    pg.time.Clock().tick(x)

# --- player_movement ---
def player_movement(keypress, running, h_move_index, v_move_index, player_pos):

    # Listen and change player position per diagonal. (BETA Feature)
    # if keypress[pg.K_w] and keypress[pg.K_d]:
    #     player_pos[1] += v_move_index[0]
    #     player_pos[0] += h_move_index[1]
    # elif keypress[pg.K_d] and keypress[pg.K_s]:
    #     player_pos[0] += h_move_index[1]
    #     player_pos[1] += v_move_index[1]
    # elif keypress[pg.K_s] and keypress[pg.K_a]:
    #     player_pos[1] += v_move_index[1]
    #     player_pos[0] += h_move_index[0]
    # elif keypress[pg.K_a] and keypress[pg.K_w]:
    #     player_pos[0] += h_move_index[0]
    #     player_pos[1] += v_move_index[0]
    
    # Listen and change player position per axis.
    if keypress[pg.K_w]:
        player_pos[1] += v_move_index[0]
    elif keypress[pg.K_a]:
        player_pos[0] += h_move_index[0]
    elif keypress[pg.K_s]:
        player_pos[1] += v_move_index[1]
    elif keypress[pg.K_d]:
        player_pos[0] += h_move_index[1]
    
    # Return list variable for player position.
    return(player_pos, running)

# --- map_edge ---
def map_edge(player_pos, size, player_size, h_move_index, v_move_index):
    
    # Horizontal edge detection here.
    if player_pos[0] < 0:
        h_move_index[0] = 0
        player_pos[0] = 0
    elif player_pos[0] + player_size[0] > size[0]:
        h_move_index[1] = 0
        player_pos[0] = size[0] - player_size[0]
    elif player_pos[0] > 0 and player_pos[0] < size[0] - player_size[0]:
        h_move_index[0] = -5
        h_move_index[1] = 5

    # Vertical edge detection here.
    if player_pos[1] < 0:
        v_move_index[0] = 0
        player_pos[1] = 0
    elif player_pos[1] + player_size[1] > size[1]:
        v_move_index[1] = 0
        player_pos[1] = size[1] - player_size[1]
    elif player_pos[1] > 0 and player_pos[1] < size[1] - player_size[1]:
        v_move_index[0] = -5
        v_move_index[1] = 5
        
    # Use switch for edge detection here. (If needed only.)

# --- player ---
def player(bgw, color, player_pos, player_size):

    # Draw player here.
    pg.draw.rect(bgw, color, [player_pos[0], player_pos[1], player_size[0], player_size[1]])

# ---