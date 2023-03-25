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

    # Set background color fill here.
    pg.Surface.fill(bgw, ui_colors['background'])

    # Set the framerate here.
    frame_rate(60)

    # Main process loop condition
    running = True

    # Create window and run main process here.
    while running:

        for event in pg.event.get():

            if event.type == pg.QUIT:

                running = False

        player(bgw, ui_colors['player'])

        pg.display.update()
    
    # Uninitialize everything and quit.
    pg.quit()
    quit()

# --- frame_rate ---

def frame_rate(x):
    
    # Set a static frame rate here.
    pg.time.Clock().tick(x)

# --- player ---

def player(bgw, ui):

    # Draw player here.
    pg.draw.rect(bgw, ui, [345, 345, 10, 10])

# ---