# PySnake
# AMCocan
# 2.01.2023

# --- Imports ---

from Utills import snake_utills as utills

# --- Vars & Args ---

size = [700, 700]
title = f'PySnake'
icon = utills.pg.image.load('Assets/icon.png')

ui_colors = {
    'obj':(0, 0, 0), 
    'background':(10, 10, 10), 
    'enemy':(0, 0, 0), 
    'player':(0, 255, 140), 
    'key':(250, 250, 250)
}

# ---

utills.main_process(size, title, icon, ui_colors)

# ---