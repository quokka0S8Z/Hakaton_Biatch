import pygame 

pygame.init()
pygame.font.init()
running = True
screen = pygame.display.set_mode((800, 600))  # Set the screen size
pygame.display.set_caption("the way home game")
background = pygame.image.load("pygame_art\\background.png")
background = pygame.transform.scale(background, (800, 600))  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.display.toggle_fullscreen()
    font = pygame.font.SysFont('Arial', 30)
    screen.blit(background,(0,0))
    pygame.display.flip() 