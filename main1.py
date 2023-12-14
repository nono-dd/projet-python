import pygame

pygame.init()


# une seconde classe qui va représenter notre jeu
class Game:

    def __int__(self):
        self.player = Player


# créer une classe qui va représenter notre joueur
class Player(pygame.sprite.Sprite):

    def __int__(self):
        super().__int__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5  # correspond à la vitesse de déplacement du joueur
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500


# générer la fenêtre de notre jeu
pygame.display.set_caption("Comet fall")
screen = pygame.display.set_mode((1080, 720))

# importer pour générer l'arrière-plan de la fenêtre
background = pygame.image.load('assets/bg.jpg')

# charger notre joueur
game = Game
running = True

# boucle tant que la variable est vrai
while running:
    # appliquer l'arrière-plan du jeu
    screen.blit(background, (0, -200))
    
    # appliquer l'image de notre joueur
    screen.blit(game.player.image, game.player.rect)
    
    # mettre à jour la fenêtre
    pygame.display.flip()
    
    # si le joueur ferme la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu ...")
