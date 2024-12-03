import sys
import pygame as pg
from  util import *

pg.init()

screen = pg.display.set_mode(SCREEN_SIZE)

pg.display.set_caption('Brick')
clk = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # screen background
        screen.fill(DARKBLUE)
        pg.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
        
        # scoreboard
        font = pg.font.Font(None, 34)
        text = font.render(f'Score: {score}', 1, WHITE)
        screen.blit(text, (20, 10))
        text = font.render(f'Lives: {lives}', 1, WHITE)
        screen.blit(text, (650, 10))
        
        
        
        
        
        pg.display.flip()
        clk.tick(60)