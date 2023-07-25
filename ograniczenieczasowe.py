import pygame

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW_CAPTION = 'Przerwa od komputera'
BG_COLOR = (255, 255, 255)  # Biały
TEXT_COLOR = (0, 0, 0)  # Czarny
FONT_SIZE = 32

# Ustawienia przerwy
BREAK_TIME_SECONDS = 5

# Inicjalizacja okna
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(WINDOW_CAPTION)

# Inicjalizacja czcionki
font = pygame.font.SysFont(None, FONT_SIZE)

# Inicjalizacja licznika czasu
break_time_counter = 0

# Pętla główna programu
while True:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEMOTION or event.type == pygame.KEYDOWN:
            break_time_counter = 0

    # Zmiana koloru tła w zależności od czasu przerwy
    screen.fill((BG_COLOR[0] - break_time_counter * 10, BG_COLOR[1] - break_time_counter * 10, BG_COLOR[2] - break_time_counter * 10))

    # Wyświetlenie tekstu na ekranie
    text_surface = font.render('Czas na przerwę od komputera na godzinę', True, TEXT_COLOR)
    screen.blit(text_surface, (SCREEN_WIDTH/2 - text_surface.get_width()/2, SCREEN_HEIGHT/2 - text_surface.get_height()/2))

    # Aktualizacja okna
    pygame.display.update()

    # Zwiększenie licznika czasu
    break_time_counter += 1

    # Sprawdzenie, czy czas przerwy się skończył
    if break_time_counter >= BREAK_TIME_SECONDS * 60:
        break