import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))  # Set the screen size
        pygame.display.set_caption("The Way Home Game")
        self.background = pygame.image.load("pygame_art\\background.png")
        self.background = pygame.transform.scale(self.background, (800, 600))

        self.button_color = (255, 0, 0)  # Red color for the button
        self.button_rect = pygame.Rect(225, 290, 370, 80)  # x, y, width, height

        self.state = "menu"  # Start in the menu state

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    self.running = False
                elif event.key == pygame.K_p:
                    pygame.display.toggle_fullscreen()

            elif event.type == pygame.MOUSEBUTTONDOWN and self.state == "menu":
                if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Start button clicked!")
                    self.state = "game"

    def update(self):
        if self.state == "menu":
            self.screen.blit(self.background, (0, 0))
            #pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        elif self.state == "game":
            pass
        #to do:
            # make main game background platforms exit(or something like that) and obsticoles(use the smile detector in each one of them)
            # combie the health bar and character into one file and make it work with the game
            #make player animation(items maybe?)
            # make unique lvls(maybe 3-5) with different obsticoles

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            pygame.display.flip()

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()
