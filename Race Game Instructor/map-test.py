import pygame
from utils import *
from padsprite import PadSprite

pygame.init()

# sprite coordinates are based on MIDDLE of the sprite
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
    (800, 750)
]]

pad_group = pygame.sprite.RenderPlain(*pads)
screen, clock, font, win_font, win_condition, win_text, loss_text, t0 = init_level()

running = True
while running:
    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Game logic ---
    # (update pads if needed)
    # pad_group.update([])

    # --- Drawing ---
    screen.fill((0, 0, 0))
    pad_group.draw(screen)
    pygame.display.flip()

    # --- Control the framerate ---
    clock.tick(60)

pygame.quit()
