# PySnake
# AMCocan
# 2.01.2023

# --- Imports ---

import pygame as pg
from Utills import snake_utills as utills

# --- Vars & Args ---

size = [700, 700]
title = f'PySnake'
icon = pg.image.load('Assets/icon.png')

# ---

utills.main_process(size, title, icon)

# ---