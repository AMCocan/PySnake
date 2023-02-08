# PySnake Utills
# AMCocan
# 2.08.2023

# --- Imports ---

import pygame as pg
import random as rn
import time as tm
import sys as sy

# --- main_process ---

def main_process(size, title, icon):

    # Initialize Pygame.
    pg.init()

    # Read agrs and build window.
    pg.display.set_mode(size)
    pg.display.set_caption(title)
    pg.display.set_icon(icon)

    # Main process loop condition
    running = True

    # Create window and run main process here.
    while running:

        for event in pg.event.get():

            if event.type == pg.QUIT:

                running = False
    
        pg.display.flip()

# --- frame_rate ---

def frame_rate(x):
    
    # Set a static frame rate here.
    pass

# --- player ---

def player():

    # Create player here.
    pass

# ---