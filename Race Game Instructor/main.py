# initialize the screen
import pygame, sys, time
from pygame.locals import *

from utils.utils import *
from utils.padsprite import PadSprite
from utils.carsprite import CarSprite
from utils.trophy import Trophy

from level2 import level2

pygame.mixer.init()
crash_sound = pygame.mixer.Sound("explosion.wav")

def level1():
    screen, clock, font, win_font, win_condition, win_text, loss_text, t0 = init_level()
    
    pads = [PadSprite((x, y)) for (x, y) in [
        (0, 10),
        (700, 10),
        (1100, 10),

        (100, 150),
        (400, 150),

        (50, 300),
        (900, 300),

        (600, 450),

        (100, 600),
        (900, 600),

        (500, 750),
        (800, 750),
    ]]
    pad_group = pygame.sprite.RenderPlain(*pads)

    trophies = [Trophy((315,0))]
    trophy_group = pygame.sprite.RenderPlain(*trophies)

    # CREATE A CAR AND RUN
    rect = screen.get_rect()
    car = CarSprite('images/car.png', (10, 730))
    car_group = pygame.sprite.RenderPlain(car)

    # check that sound effect is not yet played
    crash_played = False

    #THE GAME LOOP
    while 1:
        #USER INPUT
        t1 = time.time()
        dt = t1-t0

        deltat = clock.tick(30)


        # MISSING SECTION
        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue

            down = event.type == KEYDOWN 
            if win_condition == None: 
                if event.key == K_RIGHT:
                    car.move_right(down)
                elif event.key == K_LEFT:
                    car.move_left(down)
                elif event.key == K_UP:
                    car.move_up(down)
                elif event.key == K_DOWN:
                    car.move_down(down)

                elif event.key == K_ESCAPE:
                    sys.exit(0) # quit the game

            elif win_condition == True and event.key == K_SPACE:
                # start level 2
                level2()
            elif win_condition == False and event.key == K_SPACE:
                # restart level 1
                level1()
                t0 = t1

            elif event.key == K_ESCAPE: sys.exit(0)    
    


        #COUNTDOWN TIMER
        seconds = round((20 - dt),2)
        if win_condition == None:
            timer_text = font.render(str(seconds), True, (255,255,0))
            if seconds <= 0:
                win_condition = False
                timer_text = font.render("Time!", True, (255,0,0))
                loss_text = win_font.render('Press Space to Retry', True, (255,0,0))
            
        #RENDERING
        screen.fill((0,0,0))
        car_group.update(deltat)


        # MISSING SECTION: CRASHING
        collisions = pygame.sprite.groupcollide(car_group, pad_group, False, False, collided = None)
        if collisions != {}:
            win_condition = False
            timer_text = font.render("Crash!", True, (255,0,0))
            car.image = pygame.image.load('images/collision.png')

            # prevent sfx repeat
            if not crash_played:
                crash_sound.play()
                crash_played = True

            loss_text = win_font.render('Press Space to Retry', True, (255,0,0))
            seconds = 0
            car.MAX_FORWARD_SPEED = 0
            car.MAX_REVERSE_SPEED = 0
            car.k_right = 0
            car.k_left = 0


        # MISSING SECTION: TROPHY COLLECTION
        trophy_collision = pygame.sprite.groupcollide(car_group, trophy_group, False, True)
        if trophy_collision != {}:
            seconds = seconds
            timer_text = font.render("Finished!", True, (0,255,0))
            win_condition = True
            car.MAX_FORWARD_SPEED = 0
            car.MAX_REVERSE_SPEED = 0
            win_text = win_font.render('Press Space to Advance', True, (0,255,0))
            if win_condition == True:
                car.k_right = -5
                

        pad_group.update(collisions)
        pad_group.draw(screen)
        car_group.draw(screen)
        trophy_group.draw(screen)

        #Counter Render
        screen.blit(timer_text, (20,60))
        screen.blit(win_text, (250, 700))
        screen.blit(loss_text, (250, 700))
        pygame.display.flip()


