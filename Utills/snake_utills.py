# PySnake Utills
# AMCocan
# 2.08.2023

# --- Imports ---

import pygame as pg
import random as rn
import time as tm
import sys as sy

# --- main_process ---

def main_process(size, title, icon, ui_colors):

    # Initialize Pygame.
    pg.init()

    # Read agrs and build window.
    bgw = pg.display.set_mode(size)
    pg.display.set_caption(title)
    pg.display.set_icon(icon)

    # Set the player initial position here.
    player_xpos_init = size[0]/2
    player_ypos_init = size[1]/2

    # Set player move index here.
    pos_move_index = 2
    neg_move_index = -2

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

        # Player movement called here.
        player_movement(keypress, running, pos_move_index, neg_move_index, player_pos)

        # Player render called here.
        player(bgw, ui_colors['player'], player_pos)
        
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
def player_movement(keypress, running, pos_move_index, neg_move_index, player_pos):

    # Listen and change player position.
    if keypress[pg.K_ESCAPE]: # Work on this -- Now working rn. -- [!]
        running = False
    elif keypress[pg.K_w]:
        player_pos[1] += neg_move_index
    elif keypress[pg.K_a]:
        player_pos[0] += neg_move_index
    elif keypress[pg.K_s]:
        player_pos[1] += pos_move_index
    elif keypress[pg.K_d]:
        player_pos[0] += pos_move_index
    
    # Return list variable for player position.
    return(player_pos, running)

# --- player ---
def player(bgw, ui, player_pos):

    # Draw player here.
    pg.draw.rect(bgw, ui, [player_pos[0], player_pos[1], 10, 10])

# ---