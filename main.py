import pygame, sys
from button import Button
pygame.init()

screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Menu")
background = pygame.image.load("assets/menu_background.jpg")

icon = pygame.image.load("assets/rune.png")
pygame.display.set_icon(icon)


def get_font(font_size):
    return pygame.font.Font("assets/font.ttf", font_size)


def play():
    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        play_text = get_font(35).render("Here's the Play screen!", True, "white")
        play_rect = play_text.get_rect(center=(640, 260))
        screen.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(640,460),
                           text_input="back", font=get_font(35), base_color="white", hovering_color="Green")

        play_back.changeColor(play_mouse_pos)
        play_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(play_mouse_pos):
                    main_menu()

        pygame.display.update()


def options():
    while True:
        options_mouse_pos = pygame.mouse.get_pos()

        screen.fill("white")

        options_text = get_font(35).render("Here's the options screen!", True, "black")
        options_rect = options_text.get_rect(center=(640, 260))
        screen.blit(options_text, options_rect)

        options_back = Button(image=None, pos=(640, 460),
                              text_input="back", font=get_font(35), base_color="black", hovering_color="green")

        options_back.changeColor(options_mouse_pos)
        options_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.checkForInput(options_mouse_pos):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        screen.blit(background, (0,0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(90).render("Main Menu", True, "yellow")
        menu_rect = menu_text.get_rect(center=(640, 100))

        play_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="Play", font=get_font(75), base_color="green", hovering_color="white")
        options_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="Options", font=get_font(75), base_color="green", hovering_color="white")
        quit_button = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="Quit", font=get_font(75), base_color="green", hovering_color="white")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    play()
                if options_button.checkForInput(menu_mouse_pos):
                    options()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()




