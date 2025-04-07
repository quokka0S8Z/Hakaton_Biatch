import pygame 

pygame.init()
pygame.font.init()
running = True
screen = pygame.display.set_mode((800, 600))  # Set the screen size
pygame.display.set_caption("The Way Home Game")
background = pygame.image.load("pygame_art\\background.png")
background = pygame.transform.scale(background, (800, 600))  

button_color = (255, 0, 0)  # Red color for the button
button_rect = pygame.Rect(225, 290, 370, 80)  # x, y, width, height

state = "menu"  # Start in the menu state

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.display.toggle_fullscreen()

        elif event.type == pygame.MOUSEBUTTONDOWN and state == "menu":
            if button_rect.collidepoint(pygame.mouse.get_pos()):  
                print("Start button clicked!")
                state = "game" 

    if state == "menu":
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, button_color, button_rect)
    elif state == "game":
        pass#change to fit game window(load chr stats lvl and such)
    pygame.display.flip()