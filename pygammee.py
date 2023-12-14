import pygame

reussi, echec = pygame.init()
print(f'{reussi} est la valeur de réussi et {echec} la valeur de échec')

pygame.display.set_caption('mon premier exo avec pygame', 'GOJO')
screen = pygame.display.set_mode((1080, 720))
image = pygame.image.load('assets/alien.png').convert_alpha()
pygame.display.set_icon(image)
position_image = (0, 0)

black = (0, 0, 0)
white = (255, 255, 255)

running = True
while running:
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 640, 480))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            position_image = event.pos
        if event.type == pygame.QUIT:
            running = False
    screen.blit(image, position_image)
    # Mettre à jour l'affichage
    pygame.display.flip()
