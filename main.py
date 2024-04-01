#Axel Eloniemi NTIS21K

import pygame, sys
from asetukset import *
from luokat import Peli

#Setuppi
pygame.init() 
pygame.display.set_caption("Pingviiniseikkailu")
naytto = pygame.display.set_mode((naytto_leveys, naytto_korkeus))
kello = pygame.time.Clock()
peli = Peli()

#Game-looppi
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    peli.run()
    pygame.display.update()
    kello.tick(60)

    #Alemmalla, pois kommentoidulla metodilla voi halutessaan tarkistaa fps:än.
    #print(kello.get_fps())