# kv3nw
import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)
bird = gamebox.from_color(200,300, "yellow", 20, 20)
bird_speed = 3
pillar_width = 60
pillar = [
]
score = 0
start = False
ticks = 0


def tick(keys):
    '''
    draws the images into the game and controls the movement
    :param keys: what keys on the computer is enter
    :return: nothing
    '''
    global start
    global score
    global ticks
    if start is True:
        if pygame.K_SPACE in keys:
            bird.speedy = -15
            bird.speedx = 3
            keys.remove(pygame.K_SPACE)
        camera.x = bird.x
        bird.speedy += 2
        bird.move_speed()

    if pygame.K_SPACE in keys:
        start = True
    ticks += 1
    camera.clear('light blue')
    camera.draw(bird)
    pillar_height = int(random.randint(100, 300))
    if ticks % 40 == 0:
        top_pillar = gamebox.from_color(camera.right + 50, camera.top, 'green', 60, 650 - pillar_height)
        bottom_pillar = gamebox.from_color(camera.right + 50, camera.bottom, 'green', 60, 650 - pillar_height)
        pillar.append(top_pillar)
        pillar.append(bottom_pillar)

    for pipe in pillar:
        camera.draw(pipe)
        bird.move_to_stop_overlapping(pipe)
        if bird.x == pipe.x:
            score += 1

        if bird.touches(pipe) or bird.touches(pipe) or bird.touches(pipe) or bird.touches(pipe):
            gamebox.pause()
            end_game = gamebox.from_text(bird.x, 200, 'THE END', 30, 'black')
            scoreboard = gamebox.from_text(bird.x, 300, 'SCORE: ' + str(score // 2), 30, 'black')
            camera.draw(scoreboard)
            camera.draw(end_game)

        if bird.bottom > camera.bottom:
            gamebox.pause()
            end_game = gamebox.from_text(bird.x, 200, 'THE END', 30, 'black')
            scoreboard = gamebox.from_text(bird.x, 300, 'SCORE: ' + str(score // 2), 30, 'black')
            camera.draw(scoreboard)
            camera.draw(end_game)
    camera.display()
gamebox.timer_loop(30,tick)
