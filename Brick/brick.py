import sys
import pygame as pg
from  util import *
from objects import *

pg.init()

screen = pg.display.set_mode(SCREEN_SIZE)

pg.display.set_caption('Brick')

all_sprites_list = pg.sprite.Group()

paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list.add(paddle)
all_sprites_list.add(ball)

all_bricks = pg.sprite.Group()

for i in range(7):
    brick = Brick(RED, 80, 30)
    brick.rect.x = 60+i*100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(ORANGE, 80, 30)
    brick.rect.x = 60+i*100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)

for i in range(7):
    brick = Brick(YELLOW, 80, 30)
    brick.rect.x = 60+i*100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
    
clk = pg.time.Clock()
carryOn = True
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        
        keys = pg.key.get_pressed()    
        if keys[pg.K_LEFT]:
            paddle.moveLeft(5)
        if keys[pg.K_RIGHT]:
            paddle.moveRight(5)

        all_sprites_list.update()

        if ball.rect.x >= SCREEN_SIZE[0] -1:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x < 0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > SCREEN_SIZE[1]-1:
            ball.velocity[1] = -ball.velocity[1]
            lives -= 1
            if lives == 0:
                font = pg.font.Font(None, 75)
                text = font.render('GAME OVER', 1, WHITE)
                screen.blit(text, (250, 300))
                pg.display.flip()
                pg.time.wait(3000)
                carryOn = False
        if ball.rect.y < 40 :
            ball.velocity[1] = -ball.velocity[1]
        if pg.sprite.collide_mask(ball, paddle):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()

        if ball.velocity[1] == 0:
            ball.velocity[1] = 10

        brick_collision_list = pg.sprite.spritecollide(ball, all_bricks, False)
        for brick in brick_collision_list:
            ball.bounce()
            score += 1
            brick.kill()
            if len(all_bricks) == 0:
                font = pg.fint.Font(None, 75)
                text = font.render('Level Complete', 1, WHITE)
                screen.blit(text, (200, 300))
                pg.display.flip()
                pg.time.wait(3000)
                carryOn = False
        # screen background
        screen.fill(DARKBLUE)
        
        # scoreboard
        pg.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
        font = pg.font.Font(None, 34)
        text = font.render(f'Score: {score}', 1, WHITE)
        screen.blit(text, (20, 10))
        text = font.render(f'Lives: {lives}', 1, WHITE)
        screen.blit(text, (650, 10))
        
        all_sprites_list.draw(screen)
        pg.display.flip()

        clk.tick(60)