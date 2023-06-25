# PySnake
# AMCocan
# 2.01.2023

# --- Imports ---

from Utills import snake_lib as lib

# --- Vars & Args ---

size = [700, 700]
title = f'PySnake'
icon = lib.pg.image.load('Assets/icon.png')

ui_colors = {
    'background':(10, 10, 10), 
    'player':(0, 255, 140), 
    'enemy':(0, 0, 0), 
    'obj':(0, 0, 0), 
    'key':(250, 250, 250)
}

# --- main_process Loop ---

lib.main_process(size, title, icon, ui_colors)

# ---