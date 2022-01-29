import pygame
import sys

from .background import slow_bg_obj
from utils.draw import draw_text
from models.icon_button import IconButton
from models.controls import audio_cfg, display_cfg
from config import config
from constants import Image, Font, Colors, Text


def controls():
    run = True

    control_title_font = pygame.font.Font(Font.edit_undo_font, 50)
    control_font = pygame.font.Font(Font.neue_font, 30)
    keys_font = pygame.font.Font(Font.neue_font, 30)

    go_back_btn = IconButton(Image.GO_BACK_IMAGE, (config.starting_x + 65, 50))

    while run:
        slow_bg_obj.update()
        slow_bg_obj.render()

        draw_text(Text.CONTROLS, control_title_font, Colors.BLUE,
                  (config.center_x - 30, 130), True)
        config.CANVAS.blit(Image.CONTROL_IMAGE, (config.center_x + 95, 120))

        draw_text('Shoot', control_font, Colors.GREEN,
                  (config.starting_x + 125, 215))
        draw_text('[spacebar]', keys_font, Colors.RED,
                  (config.starting_x + 470, 215))

        draw_text('Move Left', control_font, Colors.GREEN,
                  (config.starting_x + 125, 270))
        draw_text('[left] or [a]', keys_font, Colors.RED,
                  (config.starting_x + 470, 270))

        draw_text('Move Right', control_font, Colors.GREEN,
                  (config.starting_x + 125, 325))
        draw_text('[right] or [d]', keys_font, Colors.RED,
                  (config.starting_x + 470, 325))

        draw_text('Move Down', control_font, Colors.GREEN,
                  (config.starting_x + 125, 380))
        draw_text('[down] or [s]', keys_font, Colors.RED,
                  (config.starting_x + 470, 380))

        draw_text('Move Up', control_font, Colors.GREEN,
                  (config.starting_x + 125, 435))
        draw_text('[up] or [w]', keys_font, Colors.RED,
                  (config.starting_x + 470, 435))

        draw_text('Return back to home', control_font, Colors.GREEN,
                  (config.starting_x + 125, 490))
        draw_text('[backspace]', keys_font, Colors.RED,
                  (config.starting_x + 470, 490))

        draw_text('Mute Audio', control_font, Colors.GREEN,
                  (config.starting_x + 125, 545))
        draw_text('[m]', keys_font, Colors.RED,
                  (config.starting_x + 470, 545))

        draw_text('Volume Up/Down', control_font, Colors.GREEN,
                  (config.starting_x + 125, 600))
        draw_text('[+]/[-]', keys_font, Colors.RED,
                  (config.starting_x + 470, 600))

        draw_text('Toggle Full Screen', control_font, Colors.GREEN,
                  (config.starting_x + 125, 655))
        draw_text('[f]', keys_font, Colors.RED,
                  (config.starting_x + 470, 655))

        go_back_btn.draw()

        audio_cfg.display_volume()

        pygame.display.update()
        config.clock.tick(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    audio_cfg.toggle_mute()
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    audio_cfg.inc_volume(5)
                if event.key == pygame.K_MINUS:
                    audio_cfg.dec_volume(5)
                if event.key == pygame.K_f:
                    display_cfg.toggle_full_screen()
                if event.key == pygame.K_BACKSPACE:
                    run = False

            # Mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if go_back_btn.isOver():
                        run = False

            # Mouse hover events
            if event.type == pygame.MOUSEMOTION:
                if go_back_btn.isOver():
                    go_back_btn.outline = True
                else:
                    go_back_btn.outline = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_BACKSPACE]:
        #     run = False
