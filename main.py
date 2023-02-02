# PySnake
# AMCocan
# 2.01.2023

# --- Imports ---

import pygame as pg

# --- Pygame Initiate ---

pg.init()

# ---

size = [700, 700]
title = f'PySnake'
icon = pg.image.load('Assets/icon.png')

# ---

pg.display.set_mode(size)
pg.display.set_caption(title)
pg.display.set_icon(icon)

# ---

running = True

# ---

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    pg.display.flip()