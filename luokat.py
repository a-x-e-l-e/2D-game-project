#Axel Eloniemi NTIS21K

import pygame, sys
from asetukset import *
import math

#Tämä luokka on luotu yksinkertaisia tilejä, kuten maa-tilejä (joiden päällä pelaaja voi kävellä jne) varten.
class Tile(pygame.sprite.Sprite):
    def __init__(self, paikka, ryhma, image):
        super().__init__(ryhma)
        self.image = image
        self.rect = self.image.get_rect(topleft = paikka)
        self.old_rect = self.rect.copy()
    def update(self, x_muutos):
        self.rect.x += x_muutos

#Tämän luokan avulla taas luodaan taso, joita tässä pelissä on vain yksi. Mutta samalla lailla tätä voisi käyttää myös toisen tason luomiseen, pienin muutoksin, esim. tasokartta pitäisi
#tietysti syöttää init-metodiin, jos niitä olisi monta. Koska tässä käytetään vain yhtä tasokarttaa, (tasokartta1), siihen viitataan suoraan.
class Taso:
    #Init-metodissa muun muassa ryhmät, joihin luotuja olioita sijoitetaan. Tämä on hyödyllistä siksi, että esimerkiksi oliot, joiden mahdolliset törmäykset pelaajan kanssa
    #meitä kiinnostavat, löydetään helposti yhdestä paikasta. (Tosin kaikkia pelaajan kanssa mahdollisesti törmääviä olioita ei ole sijoitettu samaan ryhmään.)
    #Init-metodi ottaa myös parametrina Alkuruutu-luokan luo_alkuruutu-metodin, jotta Taso-luokan olio voi sitä kutsua.
    def __init__(self, luo_alkuruutu):
        self.display_surface = pygame.display.get_surface()
        self.luo_alkuruutu = luo_alkuruutu
        #Spritet, jotka piirretään
        self.visible_sprites = Kamera()
        #Spritet, joita päivitetään
        self.active_sprites = pygame.sprite.Group()
        #Spritet, joiden kanssa pelaaja voi "törmätä"
        self.collision_sprites = pygame.sprite.Group()
        #Spritet, jotka voivat törmätä pelaajaan ja aiheuttaa vahinkoa
        self.enemy_collisions = pygame.sprite.Group()
        #Jos pelaaja törmää näihin spriteihin, niiden alla oleva enemy kuolee/katoaa
        self.enemy_kill_collisions = pygame.sprite.Group()
        #Liikkuvat spritet
        self.liikkuva_collisions = pygame.sprite.Group()
        #Vesispritet
        self.vesi_collisions = pygame.sprite.Group()
        #Törmäykset puiden kanssa, tarkoituksena oli muuttaa niiden läpinäkyvyyttä jos pelaaja on niiden kohdalla, mutta tästä luovuttiin.
        self.puu_collisions = pygame.sprite.Group()
        #Törmäykset putoavien pommien kanssa
        self.pommi_collisions = pygame.sprite.Group()
        #Pommeja pudottelevat viholliset, ei välitetä törmäyksistä tämän ryhmän kanssa, koska pelaajan ei ole tarkoitus suoraa vuorovaikuttaa niiden kanssa
        self.marjaryhmä = pygame.sprite.Group()
        #Törmäys VihannesPommpu-luokan olion kanssa, joka törmätessään heittää pelaajan ilmaan
        self.pomppu_collisions = pygame.sprite.Group()
        #Raketteja ampuvat tankit, ei välitetä törmäyksistä tämän ryhmän kanssa, koska pelaajan ei ole tarkoitus suoraa vuorovaikuttaa niiden kanssa
        self.tankkiryhmä = pygame.sprite.Group()
        #Törmäykset rakettien kanssa
        self.raketti_collisions = pygame.sprite.Group()

        
        self.luo_taso()


        #Kuvat "loppuanimaatiota", eli laskeutuvaa mustaa "esirippua" varten. Loppuanimaatio suoritetaan, kun pelaajan elämät putoavat nollille.
        self.loppuruutu = 0
        self.loppu1 = pygame.image.load('./Kuvat/loppu1.png').convert_alpha()
        self.loppu2 = pygame.image.load('./Kuvat/loppu2.png').convert_alpha()
        self.loppu3 = pygame.image.load('./Kuvat/loppu3.png').convert_alpha()
        self.loppu4 = pygame.image.load('./Kuvat/loppu4.png').convert_alpha()
        self.loppu5 = pygame.image.load('./Kuvat/loppu5.png').convert_alpha()
        self.loppu6 = pygame.image.load('./Kuvat/loppu6.png').convert_alpha()
        self.loppu7 = pygame.image.load('./Kuvat/loppu7.png').convert_alpha()
        self.loppu8 = pygame.image.load('./Kuvat/loppu8.png').convert_alpha()
        self.loppu9 = pygame.image.load('./Kuvat/loppu9.png').convert_alpha()
        self.loppu10 = pygame.image.load('./Kuvat/loppu10.png').convert_alpha()
        self.loppu11 = pygame.image.load('./Kuvat/loppu11.png').convert_alpha()
        self.loppu12 = pygame.image.load('./Kuvat/loppu12.png').convert_alpha()
        self.loppu13 = pygame.image.load('./Kuvat/loppu13.png').convert_alpha()
        self.loppu14 = pygame.image.load('./Kuvat/loppu14.png').convert_alpha()
        self.loppu15 = pygame.image.load('./Kuvat/loppu15.png').convert_alpha()
        self.loppu16 = pygame.image.load('./Kuvat/loppu16.png').convert_alpha()
        self.loppu17 = pygame.image.load('./Kuvat/loppu17.png').convert_alpha()
        self.loppu18 = pygame.image.load('./Kuvat/loppu18.png').convert_alpha()
        self.loppu19 = pygame.image.load('./Kuvat/loppu19.png').convert_alpha()
        self.loppu20 = pygame.image.load('./Kuvat/loppu20.png').convert_alpha()
        self.loppu21 = pygame.image.load('./Kuvat/loppu21.png').convert_alpha()
        self.loppu22 = pygame.image.load('./Kuvat/loppu22.png').convert_alpha()
        self.loppu23 = pygame.image.load('./Kuvat/loppu23.png').convert_alpha()
        self.loppu24 = pygame.image.load('./Kuvat/loppu24.png').convert_alpha()
        self.loppu25 = pygame.image.load('./Kuvat/loppu25.png').convert_alpha()
       
        self.loput = [self.loppu1, self.loppu2, self.loppu3, self.loppu4, self.loppu5, self.loppu6, self.loppu7, self.loppu8, self.loppu9, self.loppu10, self.loppu11, self.loppu12, self.loppu13, self.loppu13, self.loppu14, self.loppu15, self.loppu16, self.loppu17, self.loppu18, self.loppu19, self.loppu20, self.loppu21, self.loppu22, self.loppu23, self.loppu24, self.loppu25]
        self.loppu = False

    #Ylempänä mainittu loppuanimaatio-metodi. Vaihtelee siis ylempiä kuvia listalta järjestyksessä tietyin väliajoin, jotta käyttäjälle syntyisi illuusio liikkuvasta kuvasta.
    #Jos koko lista on käyty läpi, luodaan alkuruutu.
    def loppuanimaatio(self):    
        self.loppuruutu += 0.3
        if self.pelaaja.rect.y < 640:
            self.loppu = True
        if self.loppuruutu >= 9:
            self.loppu = True
        if self.loppuruutu >= len(self.loput):
            self.luo_alkuruutu()
            self.loppuruutu = 0

        self.display_surface.blit(self.loput[int(self.loppuruutu)], (0,0))

    #Tämä metodi asettaa oliot ja niitä edustavat kuvat oikeille paikoilleen asetukset-tiedoston tasokartan perusteella.
    def luo_taso(self):
        for rivi_indeksi,rivi in enumerate(tasokartta1):
            for sarake_indeksi,sarake in enumerate(rivi):
                x = sarake_indeksi * tile_koko
                y = rivi_indeksi * tile_koko
                if sarake == 'X':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jäätilekeski1.png').convert_alpha())  
                if sarake == 'Z':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jäätilekeski1_japohja.png').convert_alpha()) 
                if sarake == 'i':
                    Tile((x,y), [self.visible_sprites, self.puu_collisions], pygame.image.load('./Kuvat/puu3.png').convert_alpha())
                if sarake == 'x':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää1.png').convert_alpha())  
                if sarake == 'u':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää2_yläreuna.png').convert_alpha()) 
                if sarake == 'U':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää1_molemmatsivut.png').convert_alpha()) 
                if sarake == '1':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää1_vasensivu.png').convert_alpha())  
                if sarake == '2':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää2_vasensivu.png').convert_alpha())  
                if sarake == '3':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää1_vasensivujapohja.png').convert_alpha())  
                if sarake == '4':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää1_oikeasivujapohja.png').convert_alpha())  
                if sarake == '5':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää1_japohja.png').convert_alpha()) 
                if sarake == '6':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää2_oikeasivu.png').convert_alpha()) 
                if sarake == '7':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää1_oikeasivu.png').convert_alpha()) 
                if sarake == 'P':
                    self.pelaaja = Pelaaja((x,y), [self.visible_sprites,self.active_sprites], self.collision_sprites, self.enemy_collisions, self.enemy_kill_collisions, self.liikkuva_collisions, self.vesi_collisions, self.puu_collisions, self.pommi_collisions, self.marjaryhmä, self.pomppu_collisions, self.raketti_collisions, self.tankkiryhmä)
                if sarake == 'y':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jää2.png').convert_alpha())
                if sarake == 'Y':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/jäätilekeski2.png').convert_alpha())
                if sarake == 'V':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/vasenpäätile1.png').convert_alpha())
                if sarake == 'v':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/vasenpäätile2.png').convert_alpha())
                if sarake == 'L':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/vasenpäätile1_japohja.png').convert_alpha())
                if sarake == 'R':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/oikeapäätile1_japohja.png').convert_alpha())
                if sarake == 'O':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/oikeapäätile1.png').convert_alpha())
                if sarake == 'o':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/oikeapäätile2.png').convert_alpha())
                if sarake == 'M':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/molemmatreunattile2.png').convert_alpha())
                if sarake == 'm':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/molemmatreunattile1.png').convert_alpha())
                if sarake == '*':
                    Tile((x,y), [self.visible_sprites], pygame.image.load('./Kuvat/lyhyt_ylävesi.png').convert_alpha())
                if sarake == '-':
                    Tile((x,y), [self.visible_sprites], pygame.image.load('./Kuvat/pitkä_ylävesi2.png').convert_alpha())
                if sarake == '_':
                    Tile((x,y), [self.visible_sprites, self.vesi_collisions], pygame.image.load('./Kuvat/pitkä_vesi2.png').convert_alpha())
                if sarake == 's':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/silta.png').convert_alpha())
                if sarake == 'c':
                    CrabEnemy((x,y), [self.visible_sprites, self.enemy_collisions, self.active_sprites])
                if sarake == '.':
                    Törmäystile((x,y), [self.visible_sprites, self.enemy_kill_collisions], pygame.image.load('./Kuvat/törmäystile.png').convert_alpha())
                if sarake == ',':
                    LiikkuvaTörmäystile((x,y), [self.visible_sprites, self.active_sprites, self.enemy_kill_collisions], pygame.image.load('./Kuvat/törmäystile_lyhyempi_siniselle_tyypille.png').convert_alpha(), self.enemy_collisions)
                if sarake == 'a':
                    MarjaEnemy((x,y), [self.visible_sprites, self.active_sprites, self.marjaryhmä], 2)
                if sarake == 'A':
                    MarjaEnemy((x,y), [self.visible_sprites, self.active_sprites, self.marjaryhmä], -2)
                if sarake == 'b':
                    Pommi((x,y), [self.visible_sprites, self.active_sprites, self.pommi_collisions])
                if sarake == 'd':
                    VihannesPomppu((x,y), [self.visible_sprites, self.active_sprites, self.pomppu_collisions])
                if sarake == 'e':
                    SininenTyyppi((x,y), [self.visible_sprites, self.active_sprites, self.enemy_collisions], 35)
                if sarake == 'E':
                    SininenTyyppi((x,y), [self.visible_sprites, self.active_sprites, self.enemy_collisions], 200)
                if sarake == 'F':
                    Tankki((x,y), [self.visible_sprites, self.tankkiryhmä], 'vasen')
                if sarake == 'f':
                    Tankki((x,y), [self.visible_sprites, self.tankkiryhmä], 'oikea')
                if sarake == 'T':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites], pygame.image.load('./Kuvat/tiilitile.png').convert_alpha())  
                if sarake == 'G':
                    Raketti((x,y), [self.visible_sprites, self.active_sprites, self.raketti_collisions], 'vasen', "ylempi")
                if sarake == 'H':
                    Raketti((x,y), [self.visible_sprites, self.active_sprites, self.raketti_collisions], 'oikea', "ylempi")
                if sarake == "K":
                    self.ystävä2 = Ystävä((x , y - 8), [self.visible_sprites, self.active_sprites], "ei")
                if sarake == "k":
                    self.ystävä1 = Ystävä((x + 10 , y - 4), [self.visible_sprites, self.active_sprites], "kyllä")
                if sarake == "j":
                    self.alkupuhekupla = Tile((x - 138 , y - 10), [self.visible_sprites], pygame.image.load('./Kuvat/tarina1_0.png').convert_alpha())
                if sarake == "J":
                    self.loppupuhekupla = Tile((x - 10 , y), [self.visible_sprites], pygame.image.load('./Kuvat/tarina3.png').convert_alpha())

    #Tämä metodi päivittää ja piirtää olioita tasolle, niin kauan kuin pelaajan elämät eivät ole nollassa eikä tämä ole pudonnut veteen (pelaaja ei osaa uida). 
    #Jos pelaaja putoaa tai elämät menevät nollille muusta syystä, palataan alkuvalikkoon, vaikka se ei tästä vielä ilmene.
    def run(self):
        if self.loppu == False:
            self.active_sprites.update()
            self.visible_sprites.custom_draw(self.pelaaja, self.ystävä1, self.ystävä2, self.alkupuhekupla, self.loppupuhekupla)

        if self.pelaaja.rect.y > 750 or self.pelaaja.elämät == 0:
            self.loppuanimaatio()

#Tämä luokka edustaa nimensä mukaisesti kameraa, joka "seuraa" pelaajaa.
class Kamera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100,300)

        self.kolme_elämää = pygame.image.load('./Kuvat/3elämää.png').convert_alpha()
        self.kaksi_elämää = pygame.image.load('./Kuvat/2elämää.png').convert_alpha()
        self.yksi_elämää = pygame.image.load('./Kuvat/1elämää.png').convert_alpha()

        self.tausta_vuoret = pygame.image.load('./Kuvat/tausta_vuoret2.png').convert()
        self.tausta_pilvet = pygame.image.load('./Kuvat/tausta_pilvet.png').convert()
        self.tausta_yläpilvet = pygame.image.load('./Kuvat/tausta_yläpilvet1.png').convert()

        self.tarina1 = pygame.image.load('./Kuvat/tarina1.png').convert_alpha()
        self.tarina2 = pygame.image.load('./Kuvat/tarina2.png').convert_alpha()

        self.tarina1_1 = pygame.image.load('./Kuvat/tarina1_1.png').convert_alpha()
        self.tarina1_2 = pygame.image.load('./Kuvat/tarina1_2.png').convert_alpha()
        self.tarina1_3 = pygame.image.load('./Kuvat/tarina1_3.png').convert_alpha()
        self.tarina1_4 = pygame.image.load('./Kuvat/tarina1_4.png').convert_alpha()
        self.tarina1_5 = pygame.image.load('./Kuvat/tarina1_5.png').convert_alpha()
        self.tarina1_6 = pygame.image.load('./Kuvat/tarina1_6.png').convert_alpha()
        self.tarina1_7 = pygame.image.load('./Kuvat/tarina1_7.png').convert_alpha()
        self.tarina1_8 = pygame.image.load('./Kuvat/tarina1_8.png').convert_alpha()
        self.tarina1_9 = pygame.image.load('./Kuvat/tarina1_9.png').convert_alpha()
        self.tarina1_10 = pygame.image.load('./Kuvat/tarina1_10.png').convert_alpha()
        self.tarina1_11 = pygame.image.load('./Kuvat/tarina1_11.png').convert_alpha()
        self.tarina1_12 = pygame.image.load('./Kuvat/tarina1_12.png').convert_alpha()
        self.tarina1_13 = pygame.image.load('./Kuvat/tarina1_13.png').convert_alpha()
        self.tarina1_14 = pygame.image.load('./Kuvat/tarina1_14.png').convert_alpha()
        self.tarina1_15 = pygame.image.load('./Kuvat/tarina1_15.png').convert_alpha()
        self.tarina1_16 = pygame.image.load('./Kuvat/tarina1_16.png').convert_alpha()
        self.tarina1_17 = pygame.image.load('./Kuvat/tarina1_17.png').convert_alpha()
        self.tarina1_18 = pygame.image.load('./Kuvat/tarina1_18.png').convert_alpha()
        self.tarina1_19 = pygame.image.load('./Kuvat/tarina1_19.png').convert_alpha()
        self.tarina1_20 = pygame.image.load('./Kuvat/tarina1_20.png').convert_alpha()
        self.tarina1_21 = pygame.image.load('./Kuvat/tarina1_21.png').convert_alpha()
        self.tarina1_22 = pygame.image.load('./Kuvat/tarina1_22.png').convert_alpha()
        self.tarina1_23 = pygame.image.load('./Kuvat/tarina1_23.png').convert_alpha()
        self.tarina1_24 = pygame.image.load('./Kuvat/tarina1_24.png').convert_alpha()
        self.tarina1_25 = pygame.image.load('./Kuvat/tarina1_25.png').convert_alpha()
        self.tarina1_26 = pygame.image.load('./Kuvat/tarina1_26.png').convert_alpha()
        self.tarina1_27 = pygame.image.load('./Kuvat/tarina1_27.png').convert_alpha()
        self.tarina1_28 = pygame.image.load('./Kuvat/tarina1_28.png').convert_alpha()
        self.tarina1_29 = pygame.image.load('./Kuvat/tarina1_29.png').convert_alpha()
        self.tarina1_30 = pygame.image.load('./Kuvat/tarina1_30.png').convert_alpha()
        self.tarina1_31 = pygame.image.load('./Kuvat/tarina1_31.png').convert_alpha()
        self.tarina1_32 = pygame.image.load('./Kuvat/tarina1_32.png').convert_alpha()
        self.tarina1_33 = pygame.image.load('./Kuvat/tarina1_33.png').convert_alpha()
        self.tarina1_34 = pygame.image.load('./Kuvat/tarina1_34.png').convert_alpha()
        self.tarina1_35 = pygame.image.load('./Kuvat/tarina1_35.png').convert_alpha()

        self.tarina2_1 = pygame.image.load('./Kuvat/tarina2_1.png').convert_alpha()
        self.tarina2_2 = pygame.image.load('./Kuvat/tarina2_2.png').convert_alpha()
        self.tarina2_3 = pygame.image.load('./Kuvat/tarina2_3.png').convert_alpha()
        self.tarina2_4 = pygame.image.load('./Kuvat/tarina2_4.png').convert_alpha()
        self.tarina2_5 = pygame.image.load('./Kuvat/tarina2_5.png').convert_alpha()
        self.tarina2_6 = pygame.image.load('./Kuvat/tarina2_6.png').convert_alpha()
        self.tarina2_7 = pygame.image.load('./Kuvat/tarina2_7.png').convert_alpha()
        self.tarina2_8 = pygame.image.load('./Kuvat/tarina2_8.png').convert_alpha()
        self.tarina2_9 = pygame.image.load('./Kuvat/tarina2_9.png').convert_alpha()
        self.tarina2_10 = pygame.image.load('./Kuvat/tarina2_10.png').convert_alpha()
        self.tarina2_11 = pygame.image.load('./Kuvat/tarina2_11.png').convert_alpha()
        self.tarina2_12 = pygame.image.load('./Kuvat/tarina2_12.png').convert_alpha()
        self.tarina2_13 = pygame.image.load('./Kuvat/tarina2_13.png').convert_alpha()
        self.tarina2_14 = pygame.image.load('./Kuvat/tarina2_14.png').convert_alpha()
        self.tarina2_15 = pygame.image.load('./Kuvat/tarina2_15.png').convert_alpha()
        self.tarina2_16 = pygame.image.load('./Kuvat/tarina2_16.png').convert_alpha()
        self.tarina2_17 = pygame.image.load('./Kuvat/tarina2_17.png').convert_alpha()
        self.tarina2_18 = pygame.image.load('./Kuvat/tarina2_18.png').convert_alpha()
        self.tarina2_19 = pygame.image.load('./Kuvat/tarina2_19.png').convert_alpha()

        self.tarinat1 = [self.tarina1_1, self.tarina1_2, self.tarina1_3, self.tarina1_4, self.tarina1_5, self.tarina1_6, self.tarina1_7, self.tarina1_8, self.tarina1_9, self.tarina1_10, self.tarina1_11, self.tarina1_12, self.tarina1_13, self.tarina1_14, self.tarina1_15, self.tarina1_16, self.tarina1_17, self.tarina1_18, self.tarina1_19, self.tarina1_20, self.tarina1_21, self.tarina1_21, self.tarina1_21, self.tarina1_22, self.tarina1_23, self.tarina1_24, self.tarina1_25, self.tarina1_26, self.tarina1_27, self.tarina1_28, self.tarina1_29, self.tarina1_30, self.tarina1_31, self.tarina1_32, self.tarina1_33, self.tarina1_34, self.tarina1_34, self.tarina1_34, self.tarina1_35 ]
        self.tarinat2 = [self.tarina2_1, self.tarina2_2, self.tarina2_3, self.tarina2_4, self.tarina2_5, self.tarina2_5, self.tarina2_5, self.tarina2_6, self.tarina2_7, self.tarina2_8, self.tarina2_9, self.tarina2_10, self.tarina2_11, self.tarina2_12, self.tarina2_13, self.tarina2_14, self.tarina2_15, self.tarina2_16, self.tarina2_17, self.tarina2_18, self.tarina2_18, self.tarina2_18, self.tarina2_19]

        self.background_leveys = self.tausta_pilvet.get_width()
        self.tiles = math.ceil(naytto_leveys / self.background_leveys) + 1
        self.scroll = 0
        self.scroll2 = 0

        kamera_v = kamera_rajat['vasen']
        kamera_y = kamera_rajat['ylä']
        kamera_leveys = self.display_surface.get_size()[0]-(kamera_v + kamera_rajat['oikea'])
        kamera_korkeus = self.display_surface.get_size()[1]-(kamera_y + kamera_rajat['ala'])

        self.kamera_rect = pygame.Rect(kamera_v,kamera_y,kamera_leveys,kamera_korkeus)

        self.index = 0
        self.index2 = 0
        self.animation_speed = 0.13

    #Tällä metodilla animoidaan pelin alussa piirrettävä puhekupla. Käytännössä siis käydään läpi listaa, jonka sisältämät kuvat piirretään näytölle yksi kerrallaan.
    def animoi1(self,alkupuhekupla,pelaaja):
        self.index += self.animation_speed
        if self.index >= len(self.tarinat1):
            self.index = 0
            self.tarinat1 = [self.tarina1_35]
            pelaaja.animaatio1_käynnissä = False

        alkupuhekupla.image = self.tarinat1[int(self.index)]
    
    #Samanlainen metodi kuin ylempi, mutta lopussa piirrettävää puhekuplaa varten. Nämä olisi toki voinut yhdistää yhdeksikin metodiksi.
    def animoi2(self,loppupuhekupla,pelaaja):
        self.index2 += self.animation_speed
        if self.index2 >= len(self.tarinat2):
            self.index2 = 0
            self.tarinat2 = [self.tarina2_19]
            pelaaja.animaatio2_käynnissä = False

        loppupuhekupla.image = self.tarinat2[int(self.index2)]

    #Ja sitten varsinainen piirtometodi. Kun pelaaja liikkuu, kamera näyttää seuraavan häntä. Se toteutetaan niin, että
    #näkyviä spritejä (visible_sprites) siirretään vastaamaan pelaajan liikkeitä, kun pelaaja ylittää tietyn rajan.

    #Metodi vastaa myös taustan ja elämäpisteiden piirtämisestä, jotka taas eivät seuraa pelaajan liikkeitä, vaan niiden paikka on vakio.
    #Metodin lopusta löytyy myös alku- ja loppupuhekuplien animointi, joiden ajamista kontrolloidaan muuttujien avulla.
    def custom_draw(self,pelaaja, ystävä1, ystävä2, alkupuhekupla, loppupuhekupla):
        for i in range(0, self.tiles):
            self.display_surface.blit(self.tausta_pilvet, (i * self.background_leveys + self.scroll, 0))
        for i in range(0, self.tiles):
            self.display_surface.blit(self.tausta_yläpilvet, (i * self.background_leveys + self.scroll2, 0))

        self.scroll -= 0.3
        self.scroll2 -= 0.7

        self.display_surface.blit(self.tausta_vuoret, (0,450))

        if abs(self.scroll) > self.background_leveys:
            self.scroll = 0
        if abs(self.scroll2) > self.background_leveys:
            self.scroll2 = 0

        if pelaaja.rect.left < self.kamera_rect.left and pelaaja.rect.x > 850:
            self.kamera_rect.left = pelaaja.rect.left
        if pelaaja.rect.right > self.kamera_rect.right and pelaaja.rect.x < 19000:
            self.kamera_rect.right = pelaaja.rect.right

        self.offset = pygame.math.Vector2(self.kamera_rect.left - kamera_rajat['vasen'],self.kamera_rect.top - kamera_rajat['ylä'])
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        if pelaaja.elämät == 3:
            self.display_surface.blit(self.kolme_elämää, (naytto_leveys - 57, naytto_korkeus - 710))
        elif pelaaja.elämät == 2:
            self.display_surface.blit(self.kaksi_elämää, (naytto_leveys - 57, naytto_korkeus - 710))
        elif pelaaja.elämät == 1:
            self.display_surface.blit(self.yksi_elämää, (naytto_leveys - 57, naytto_korkeus - 710))

        if pelaaja.cutscene == True:
            ystävä1.cutscene = True
            self.animoi1(alkupuhekupla,pelaaja)
        else:
            ystävä1.cutscene = False 
            alkupuhekupla.kill()     

        if pelaaja.rect.x > 19000:
            pelaaja.loppucutscene = True
            ystävä2.cutscene = True
            self.animoi2(loppupuhekupla,pelaaja)
            
#Nimensä mukaisesti pelaajaa varten luotu luokka, sisältää myös monia yleisesti pelin kannalta keskeisiä metodeita, kuten syötteen tarkkailun.
class Pelaaja(pygame.sprite.Sprite):
    def __init__(self, paikka,ryhma,collision_sprites, enemy_collisions, enemy_kill_collisions, liikkuva_collisions, vesi_collisions, puu_collisions, pommi_collisions, marjaryhmä, pomppu_collisions, raketti_collisions, tankkiryhmä):
        super().__init__(ryhma)

        #Pelaajan kuvat ja niistä luodut listat
        self.paikallaan = pygame.image.load('./Kuvat/paikallaan.png').convert_alpha()
        self.juoksu1 = pygame.image.load('./Kuvat/juoksu1.png').convert_alpha()
        self.juoksu2 = pygame.image.load('./Kuvat/juoksu2.png').convert_alpha()
        self.hyppy = pygame.image.load('./Kuvat/hyppy.png').convert_alpha()
        self.putoaa = pygame.image.load('./Kuvat/putoaa.png').convert_alpha()

        self.paikallaan_vasen = pygame.image.load('./Kuvat/paikallaan_vasen.png').convert_alpha()
        self.juoksu1_vasen = pygame.image.load('./Kuvat/juoksu1_vasen.png').convert_alpha()
        self.juoksu2_vasen = pygame.image.load('./Kuvat/juoksu2_vasen.png').convert_alpha()
        self.hyppy_vasen = pygame.image.load('./Kuvat/hyppy_vasen.png').convert_alpha()
        self.putoaa_vasen = pygame.image.load('./Kuvat/putoaa_vasen.png').convert_alpha()

        self.tanssi1 = pygame.image.load('./Kuvat/tanssi11.png').convert_alpha()
        self.tanssi2 = pygame.image.load('./Kuvat/tanssi22.png').convert_alpha()
        self.tanssi3 = pygame.image.load('./Kuvat/tanssi333.png').convert_alpha()
        self.tanssit = [self.tanssi1, self.tanssi2, self.tanssi1, self.tanssi3]

        self.juoksut = [self.juoksu1,self.juoksu2]
        self.juoksut_vasen = [self.juoksu1_vasen, self.juoksu2_vasen]

        self.tanssi_index = 0
        self.juoksu_index = 0
        self.paikallaan_index = 0
        self.animation_speed = 0.10
        self.image = self.paikallaan
        self.rect = self.image.get_rect(topleft = paikka)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        #Pelaajan liikkuminen
        self.position = pygame.math.Vector2(self.rect.topleft)
        self.suunta = pygame.math.Vector2(0,0)
        self.nopeus = 6
        self.painovoima = 0.8
        self.hyppy_nopeus = -15
        self.dx = 0
        self.dy = 0

        self.collision_sprites = collision_sprites
        self.enemy_collisions = enemy_collisions
        self.enemy_kill_collisions = enemy_kill_collisions
        self.liikkuva_collisions = liikkuva_collisions
        self.vesi_collisions = vesi_collisions
        self.puu_collisions = puu_collisions
        self.pommi_collisions = pommi_collisions
        self.pomppu_collisions = pomppu_collisions
        self.raketti_collisions = raketti_collisions
        self.marjaryhmä = marjaryhmä
        self.tankkiryhmä = tankkiryhmä
        self.maassa = False
        self.tormays_cooldown = False
        self.tormays_aika = 0
        self.vedessä = False
        self.elämät = 3
        self.animaatio1_käynnissä = True
        self.animaatio2_käynnissä = True
        self.cutscene = True
        self.loppucutscene = False

        self.collision_raja = 25
        
        self.status = 'paikallaan'
        self.katsoo_oikealle = False

    #Tällä metodilla tarkkaillaan syötettä.
    def hae_syote(self):
        #Jos "cutscene" ei ole käynnissä (eli puhekuplaa ei ole piirrettynä näytölle), puhekuplan animointi ei ole käynnissä
        #eikä pelaaja ole vedessä, voi käyttäjä käyttää vasenta ja oikeaa nuolinäppäintä liikkumiseen ja välilyöntinäppäintä hyppäämiseen. 
        if self.vedessä == False and self.cutscene == False and self.loppucutscene == False and self.animaatio1_käynnissä == False:
            self.dx = 0
            self.dy = 0
            nappain = pygame.key.get_pressed()
            if nappain[pygame.K_RIGHT]:
                self.suunta.x = 1
                self.dx += 6
                self.katsoo_oikealle = True
            elif nappain[pygame.K_LEFT]:
                self.suunta.x = -1
                self.dx -= 6
                self.katsoo_oikealle = False
            else:
                self.suunta.x = 0

            if nappain[pygame.K_SPACE] and self.maassa == True:
                self.suunta.y = self.hyppy_nopeus
        #Jos alkupuhekupla on piirrettynä näytölle mutta se on animoitu jo loppuun saakka, voi käyttäjä painaa enteriä siirtyäkseen eteenpäin. Sen jälkeen hän voi liikkua, sitä ennen ei.
        elif self.cutscene == True and self.animaatio1_käynnissä == False:
            self.dx = 0
            self.dy = 0
            nappain = pygame.key.get_pressed()
            if nappain[pygame.K_RETURN]:
                self.cutscene = False
        #Jos loppupuhekupla on piirrettynä näytölle ja sen animointi on kesken, asetetaan pelaajahahmo "tanssimaan". Käyttäjä ei voi tällöin liikkua eikä edetä painamalla mitään näppäintä.
        elif self.loppucutscene == True and self.animaatio2_käynnissä == True:
            self.dx = 0
            self.dy = 0
            self.status = 'tanssii'
            self.katsoo_oikealle = True
        #Jos loppupuhekupla on piirrettynä näytölle ja se on animoitu loppuun saakka, voi käyttäjä painaa enteriä jatkaakseen. (Tällöin peli loppuu ja siirrytään alkuvalikkoon.)
        elif self.loppucutscene == True and self.animaatio2_käynnissä == False:
            self.dx = 0
            self.dy = 0
            self.suunta.x = 0
            nappain = pygame.key.get_pressed()
            if nappain[pygame.K_RETURN]:
                self.elämät = 0
        else:
            self.dx = 0
            self.dy = 0

    #Tämä metodi hakee pelaajan "statuksen", eli mitä pelaaja juuri nyt tekee, esim. onko paikallaan vai hyppääkö.
    def get_status(self):
        if self.loppucutscene == False:
            if self.suunta.y < 0:
                self.status = 'hyppää'
            elif self.suunta.y > 6:
                self.status = 'tippuu'
            else:
                if self.suunta.x != 0 and self.maassa == True:
                    self.status = 'juoksee'
                elif self.maassa == True:
                    self.status = 'paikallaan'

    #Edellisen metodin avulla haettua tietoa sitten käytetään tämän metodin avulla sen päättämiseen, mikä kuva pelaajasta piirretään.   
    def animoi(self):
        if self.status == 'paikallaan':
            if self.katsoo_oikealle == True:
                self.image = self.paikallaan
            else:
                self.image = self.paikallaan_vasen
        elif self.status == 'hyppää':
            if self.katsoo_oikealle == True:
                self.image = self.hyppy
            else:
                self.image = self.hyppy_vasen
        elif self.status == 'tippuu':
            if self.katsoo_oikealle == True:
                self.image = self.putoaa
            else:
                self.image = self.putoaa_vasen
        elif self.status == 'tanssii':
            self.tanssi_index += self.animation_speed * 0.7
            if self.tanssi_index >= len(self.tanssit):
                self.tanssi_index = 0

            self.image = self.tanssit[int(self.tanssi_index)]
        else:
            if self.katsoo_oikealle == True:
                self.juoksu_index += self.animation_speed
                if self.juoksu_index >= len(self.juoksut):
                    self.juoksu_index = 0

                self.image = self.juoksut[int(self.juoksu_index)]
            else:
                self.juoksu_index += self.animation_speed
                if self.juoksu_index >= len(self.juoksut_vasen):
                    self.juoksu_index = 0

                self.image = self.juoksut_vasen[int(self.juoksu_index)]
             
    #Tämä metodi tarkkailee pelaajan ja vihollisten pudottamien pommien keskinäisiä törmäyksiä. Metodi on melkoinen epäoptimoitu sekasotku, mutta olen käyttänyt tähän projektiin jo
    #opintojakson laajuuteen nähden miltei kaksinkertaisen ajan, niin rehellisesti sanoen en jaksa enää lähteä kirjoittamaan sitä uudelleen, sillä se kuitenkin toimii, vaikka se toki
    #voisi olla kauniimmin kirjoitettu. Tämä toteutus kuitenkin aiheuttaa sen, että metodia joudutaan kutsua myöhemmässä update-metodissa yhtä monta kertaa kuin pommeja on.

    #Käytännössä tämä metodi siis tarkistaa, että törmääkö pelaaja pommiin kun se ei vielä ole räjähtänyt (eli sen kuva on räjähdys0), eli se ei ole osunut maahan taikka räjähtänyt vedessä.
    #Jos pelaaja törmää siihen, vähennetään pelaajalta yksi elämäpiste, ja käynnistetään laskuri (pelaaja on pienen hetken immuuni muille törmäyksille niin, että hän ei törmätessään menetä toista elämää
    #välittömästi ensimmäisen elämäpisteen menetyksen perään). Mikäli pommi törmää lattiaan, veteen tai pelaajaan, käynnistetään räjähdysanimaatio.
    def pommi_tormays(self, num):
        if self.pommi_collisions.sprites()[num].rect.colliderect(self.rect) and self.pommi_collisions.sprites()[num].image == self.pommi_collisions.sprites()[num].räjähdys0:
            if self.tormays_cooldown == False:
                self.elämät -= 1
                self.tormays_cooldown = True
                self.tormays_aika = pygame.time.get_ticks()
            self.pommi_collisions.sprites()[num].räjähdys = True
            self.pommi_collisions.sprites()[num].nopeus = 0
        if self.pommi_collisions.sprites()[num].image == self.pommi_collisions.sprites()[num].räjähdys4:
            self.pommi_collisions.sprites()[num].image = self.pommi_collisions.sprites()[num].räjähdys0
            self.pommi_collisions.sprites()[num].räjähdys = False
            self.pommi_collisions.sprites()[num].rect.x = self.marjaryhmä.sprites()[num].rect.x
            self.pommi_collisions.sprites()[num].rect.y = self.marjaryhmä.sprites()[num].rect.y + 40
            self.pommi_collisions.sprites()[num].nopeus = 3
        for sprite1 in self.collision_sprites.sprites():
            if self.pommi_collisions.sprites()[num].rect.colliderect(sprite1):
                self.pommi_collisions.sprites()[num].räjähdys = True
                self.pommi_collisions.sprites()[num].nopeus = 0
            if self.pommi_collisions.sprites()[num].image == self.pommi_collisions.sprites()[num].räjähdys4:
                    self.pommi_collisions.sprites()[num].image = self.pommi_collisions.sprites()[num].räjähdys0
                    self.pommi_collisions.sprites()[num].räjähdys = False
                    self.pommi_collisions.sprites()[num].rect.x = self.marjaryhmä.sprites()[num].rect.x
                    self.pommi_collisions.sprites()[num].rect.y = self.marjaryhmä.sprites()[num].rect.y + 40
                    self.pommi_collisions.sprites()[num].nopeus = 3    
        for sprite2 in self.vesi_collisions.sprites():
            if self.pommi_collisions.sprites()[num].rect.colliderect(sprite2):
                self.pommi_collisions.sprites()[num].räjähdys = True
                self.pommi_collisions.sprites()[num].nopeus = 0
            if self.pommi_collisions.sprites()[num].image == self.pommi_collisions.sprites()[num].räjähdys4:
                    self.pommi_collisions.sprites()[num].image = self.pommi_collisions.sprites()[num].räjähdys0
                    self.pommi_collisions.sprites()[num].räjähdys = False
                    self.pommi_collisions.sprites()[num].rect.x = self.marjaryhmä.sprites()[num].rect.x
                    self.pommi_collisions.sprites()[num].rect.y = self.marjaryhmä.sprites()[num].rect.y + 40
                    self.pommi_collisions.sprites()[num].nopeus = 3   

    #Tämä metodi tarkistaa, törmäävätkö raketit pelaajaan (jolloin pelaaja menettää elämäpisteen) tai muihin tileihin. Raketit voivat myös lentää vain tietyn maksimimatkan päähän,
    #ja kun ne sen saavuttavat, ne räjähtävät riippumatta siitä, törmäsivätkö ne mihinkään. 
    def raketti_tormays2(self):
        for sprite in self.raketti_collisions.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.tormays_cooldown == False:
                    self.elämät -= 1
                    self.tormays_cooldown = True
                    self.tormays_aika = pygame.time.get_ticks()
                sprite.räjähdys = True
                sprite.nopeus = 0
            if abs(sprite.lähtöx - sprite.rect.x) > 1600:
                sprite.räjähdys = True
                sprite.nopeus = 0
            if sprite.image == sprite.räjähdys4:
                sprite.image = sprite.räjähdys0
                sprite.räjähdys = False
                sprite.rect = sprite.image.get_rect(topright = sprite.paikka)
                sprite.rect.y += 30
                if sprite.vasenvaioikea == 'vasen':
                    sprite.nopeus = -6
                    sprite.rect.x += 15
                else:
                    sprite.nopeus = 6
                    sprite.rect.x -= 15
            for sprite1 in self.collision_sprites.sprites():
                if sprite.rect.colliderect(sprite1):
                    sprite.räjähdys = True
                    sprite.nopeus = 0
                if sprite.image == sprite.räjähdys4:
                    sprite.image = sprite.räjähdys0
                    sprite.räjähdys = False
                    sprite.rect = sprite.image.get_rect(topright = sprite.paikka)
                    sprite.rect.y += 30
                    if sprite.vasenvaioikea == 'vasen':
                        sprite.nopeus = -6
                        sprite.rect.x += 15
                    else:
                        sprite.nopeus = 6
                        sprite.rect.x -= 15

    #Tämä metodi tarkistaa, onko pelaaja pudonnut veteen, ja jos on, niin muutetaan pelaajan
    #putoamisnopeutta, simuloidaksemme veden kannattelukykyä (putoaminen hidastuu).
    def tormays_vesi(self):
        for sprite in self.vesi_collisions.sprites():
            if sprite.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.suunta.y = 2
                self.dy = self.suunta.y
                self.vedessä = True
                self.elämät = 0

    #Tätä metodia käytetään tarkistaessa, törmääkö pelaaja staattisiin tileihin, eli seiniin ja lattioihin ym.
    #Mikäli pelaaja törmää niihin, pelaajaa estetään liikkumasta tilen läpi, ja näin syntyy illuusio siitä,
    #että pelaaja seisoo tilen päällä tai on seinää vasten.
    def tormays(self):
        for sprite in self.collision_sprites.sprites():
            #Tarkistaa törmäisikö pelaaja liikkuessaan staattisiin spriteihin x-suunnassa.
            if sprite.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0

            #Tarkistaa törmäisikö pelaaja liikkuessaan staattisiin spriteihin y-suunnassa.
            if sprite.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                if self.suunta.y < 0:
                    self.dy = sprite.rect.bottom - self.rect.top
                    self.suunta.y = 0
                    
                elif self.suunta.y >= 0:
                    self.dy = sprite.rect.top - self.rect.bottom
                    self.suunta.y = 0
                    self.maassa = True
            if self.maassa == True and self.suunta.y != 0:
                self.maassa = False

    def tormays_liikkuva(self):
        for sprite in self.liikkuva_collisions.sprites():
            #Tarkista törmäisikö pelaaja liikkuviin spriteihin x-suunnassa.
            if sprite.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
            #Tarkista törmäisikö pelaaja liikkuviin spriteihin y-suunnassa.
            if sprite.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                if abs((self.rect.top + self.dy) - sprite.rect.bottom) < self.collision_raja:
                    self.suunta.y = 0
                    self.dy = sprite.rect.bottom - self.rect.top
                elif abs((self.rect.bottom + self.dy) - sprite.rect.top) < self.collision_raja:
                    self.rect.bottom = sprite.rect.top - 3
                    self.maassa = True
                    self.dy = 0
                                 
                if sprite.pysty == 0:
                    self.rect.x += sprite.nopeus
                      
    #Tällä metodilla tarkistetaan, törmääkö pelaaja viholliseen. Törmätessä vihollinen tönäisee
    #pelaajaa poispäin, ja pelaaja menettää yhden elämän. Mikäli pelaaja on kuitenkin juuri äsken
    #(kahden sekunnin aikaikkunan sisällä) törmännyt viholliseen, hän ei menetä toista elämää putkeen.
    def enemy_tormays(self):
        for sprite in self.enemy_collisions.sprites():
            if sprite.rect.colliderect(self.rect):
                if sprite.rect.left >= self.rect.left - 10 and self.rect.right < sprite.rect.centerx - 4:
                    self.rect.x -= 30
                    self.suunta.y -= 2
                    if self.tormays_cooldown == False:
                        self.elämät -= 1
                        self.tormays_cooldown = True
                        self.tormays_aika = pygame.time.get_ticks()
                elif sprite.rect.right <= self.rect.right + 10 and self.rect.left > sprite.rect.centerx + 4:
                    self.rect.x += 30
                    self.suunta.y -= 2
                    if self.tormays_cooldown == False:
                        self.elämät -= 1
                        self.tormays_cooldown = True
                        self.tormays_aika = pygame.time.get_ticks()

    #Tämä metodi taas tarkistaa, törmääkö pelaaja VihannesPomppu-luokan olioon, ja jos törmää silloin kun olio on noususuunnassa, pelaaja "heitetään" ylöspäin.
    def pomppu_tormays(self):
        for sprite in self.pomppu_collisions.sprites():
            if sprite.rect.colliderect(self.rect):
                    if sprite.image == sprite.kuva2:
                        self.suunta.y = -26
                        self.maassa = False
                    else:
                        self.rect.bottom = sprite.rect.top
                        self.maassa = True
                        self.suunta.y = 0
                    

    #Pelaajan mahdollisuus kukistaa viholliset on toteutettu niin, että vihollisen ylle on sijoitettu 
    #ylimääräinen tile, ja jos pelaaja törmää siihen, vihollinen alla kuolee. Käytännössä käyttäjälle itselleen
    #näyttää silti siltä, että mikäli hän hyppää vihollisen pään päälle, vihollinen kuolee, sillä tämä tile on
    #näkymätön.
    def enemy_kill_tormays(self):
        for sprite in self.enemy_kill_collisions.sprites():
            if sprite.rect.colliderect(self.rect):
                for sprite1 in self.enemy_collisions.sprites():
                    if abs(sprite1.rect.x - sprite.rect.x) < 100:
                        self.suunta.y = -10
                        sprite1.kill()
                sprite.kill()
    
    #Laskuri törmäyksien aiemmin mainittuja "cooldowneja" varten.
    def laskuri(self):
        if self.tormays_cooldown == True:
            aika_nyt = pygame.time.get_ticks()
            if aika_nyt - self.tormays_aika >= 2000:
                self.tormays_cooldown = False

    #Tällä metodilla luodaan illuusio painovoimasta, joka työntää pelaajaa takaisin maata kohti, kun tämä hyppää ilmaan.
    def luo_painovoima(self):
        self.suunta.y += self.painovoima
        if self.suunta.y >= 18:
            self.suunta.y = 18
        self.dy += self.suunta.y

    #Tässä metodissa ajetaan edellä määriteltyjä metodeja.
    def update(self):
        self.old_rect = self.rect.copy()
        self.hae_syote()
        self.get_status()
        self.animoi()
        
        self.luo_painovoima()
        self.tormays()
        self.tormays_liikkuva()
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.tormays_vesi()
        self.enemy_kill_tormays()
        self.enemy_tormays()
        self.pomppu_tormays()
        self.pommi_tormays(0)
        self.pommi_tormays(1)
        self.pommi_tormays(2)
        self.pommi_tormays(3)
        self.pommi_tormays(4)
        self.pommi_tormays(5)
        self.pommi_tormays(6)
        self.pommi_tormays(7)
        self.pommi_tormays(8)
        self.pommi_tormays(9)
        self.pommi_tormays(10)
        self.pommi_tormays(11)
        self.pommi_tormays(12)
        self.pommi_tormays(13)
        self.pommi_tormays(14)
        self.pommi_tormays(15)
        self.pommi_tormays(16)

        self.raketti_tormays2()
        
        self.laskuri()       

#Tässä luokassa määritellään vihollisista ensimmäiseen liittyvät seikat.
class CrabEnemy(pygame.sprite.Sprite):
    def __init__(self,paikka,ryhma):
        super().__init__(ryhma)
        self.paikka = paikka
        self.frame_index = 0
        self.animation_speed = 0.1
        self.crab1 = pygame.image.load('./Kuvat/crab1.png').convert_alpha()
        self.crab2 = pygame.image.load('./Kuvat/crab2.png').convert_alpha()
        self.crab3 = pygame.image.load('./Kuvat/crab3.png').convert_alpha()
        self.crab4 = pygame.image.load('./Kuvat/crab4.png').convert_alpha()
        self.crab5 = pygame.image.load('./Kuvat/crab5.png').convert_alpha()
        self.crab6 = pygame.image.load('./Kuvat/crab6.png').convert_alpha()
        self.crab7 = pygame.image.load('./Kuvat/crab7.png').convert_alpha()

        self.crab11 = pygame.image.load('./Kuvat/crab11.png').convert_alpha()
        self.crab22 = pygame.image.load('./Kuvat/crab22.png').convert_alpha()
        self.crab33 = pygame.image.load('./Kuvat/crab33.png').convert_alpha()
        self.crab44 = pygame.image.load('./Kuvat/crab44.png').convert_alpha()
        self.crab55 = pygame.image.load('./Kuvat/crab55.png').convert_alpha()
        self.crab66 = pygame.image.load('./Kuvat/crab66.png').convert_alpha()
        self.crab77 = pygame.image.load('./Kuvat/crab77.png').convert_alpha()

        self.crabs = [self.crab1, self.crab2, self.crab3, self.crab4, self.crab5, self.crab6, self.crab7, self.crab11, self.crab22, self.crab33, self.crab44, self.crab55, self.crab66, self.crab77]
        

        self.image = self.crabs[int(self.frame_index)]
        self.rect = self.image.get_rect(topright = paikka)

    #Tällä metodilla animoidaan vihollinen, käyttäen ja vaihdellen ylempiä kuvia.
    def animoi(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.crabs):
            self.frame_index = 0

        self.image = self.crabs[int(self.frame_index)]
        if self.frame_index <= 7:
            self.rect = self.image.get_rect(topright = self.paikka)
        else:
            self.rect = self.image.get_rect(topleft = self.paikka)
            self.rect.x -= 45
    
    #Tämä ei tarvinne edes selitystä, mutta update-metodin sisällä kuitenkin ajetaan ylempi animoi-metodi.
    def update(self):
        self.animoi()

#Tässä luokassa määritellään pommeihin liittyvät seikat.
class Pommi(pygame.sprite.Sprite):
    def __init__(self,paikka,ryhma):
        super().__init__(ryhma)
        self.paikka = paikka
        self.image = pygame.image.load('./Kuvat/pommi1.png').convert_alpha()
        self.räjähdys0 = pygame.image.load('./Kuvat/pommi1.png').convert_alpha()
        self.räjähdys1 = pygame.image.load('./Kuvat/pommi2.png').convert_alpha()
        self.räjähdys2 = pygame.image.load('./Kuvat/pommi3.png').convert_alpha()
        self.räjähdys3 = pygame.image.load('./Kuvat/pommi4.png').convert_alpha()
        self.räjähdys4 = pygame.image.load('./Kuvat/pommi5.png').convert_alpha()
        self.räjähdykset = [self.räjähdys1, self.räjähdys2, self.räjähdys3, self.räjähdys4]
        self.rect = self.image.get_rect(topright = paikka)
        self.nopeus = 3

        self.animation_speed = 0.1
        self.frame_index = 0
        self.rect.y += 20

        self.räjähdys = False

    #Update-metodi vastaa sekä olion liikkumisesta sekä animaatiosta, animaatioon käytettävä koodi miltei tismalleen sama kuin ylemmässä luokassa.
    def update(self):
        self.rect.y += self.nopeus

        if self.räjähdys == True:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.räjähdykset):
                self.frame_index = 0

            self.image = self.räjähdykset[int(self.frame_index)]
        else:
            self.frame_index = 0

#Tässä luokassa määritellään vihollisista toinen, joka pudottelee pommeja. Pitkälti samanlainen kuin ensimmäinenkin vihollisluokka, pienillä eroilla.
class MarjaEnemy(pygame.sprite.Sprite):
    def __init__(self,paikka,ryhma,nopeus):
        super().__init__(ryhma)
        self.paikka = paikka
        self.image = pygame.image.load('./Kuvat/marjavihollinen1.png').convert_alpha()

        self.kuva1 = pygame.image.load('./Kuvat/marjavihollinen1.png').convert_alpha()
        self.kuva2 = pygame.image.load('./Kuvat/marjavihollinen2.png').convert_alpha()
        self.kuva11 = pygame.image.load('./Kuvat/marjavihollinen11.png').convert_alpha()
        self.kuva22 = pygame.image.load('./Kuvat/marjavihollinen22.png').convert_alpha()
        self.kuvat = [self.kuva1, self.kuva2]
        self.kuvat2 = [self.kuva11, self.kuva22]
        self.rect = self.image.get_rect(topright = paikka)
        self.liikkumis_laskuri = 0
        self.nopeus = nopeus
        self.pommi_cooldown = False
        self.frame_index = 0
        self.animation_speed = 0.1

    def animoi(self):
        if self.nopeus < 0:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.kuvat):
                self.frame_index = 0

            self.image = self.kuvat[int(self.frame_index)]
        else:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.kuvat2):
                self.frame_index = 0

            self.image = self.kuvat2[int(self.frame_index)]

    #Tässä mainittavaa on oikeastaan vain se, että olion vaakasuuntaista liikkumissuunta muutetaan vastakkaiseksi, mikäli liikkumis_laskuri saavuttaa arvon 200 tai -200.
    def update(self):
        self.animoi()
        self.rect.x += self.nopeus
        self.liikkumis_laskuri += 1
        if abs(self.liikkumis_laskuri) > 200:
            self.nopeus *= -1
            self.liikkumis_laskuri *= -1

#Tätä käytetään törmäyksissä apuna edellä mainitulla tavalla, eli se asetetaan vihollisen pään päälle ja mikäli pelaaja törmää siihen, vihollinen alla kuolee.
class Törmäystile(pygame.sprite.Sprite):
    def __init__(self, paikka, ryhma, image):
        super().__init__(ryhma)
        self.image = image
        self.rect = self.image.get_rect(topright = paikka)
        self.rect.x -= 8
        self.rect.y += 25

#Sama kuin edellinen, mutta tarkoitettu vihollisille, jotka liikkuvat x-suunnassa.
class LiikkuvaTörmäystile(pygame.sprite.Sprite):
    def __init__(self, paikka, ryhma, image, enemyn_ryhmä):
        super().__init__(ryhma)
        self.image = image
        self.rect = self.image.get_rect(topright = paikka)
        self.rect.y += 35
        self.enemyn_ryhmä = enemyn_ryhmä
        self.nopeus = 0
        self.välimatka = 100000000
        self.enemy = 0

    #Tällä metodilla tarkistetaan, mikä on lähin enemysprite törmäystileen nähden, ja tätä
    #tietoa käytetään sitten alempana siihen, että voidaan asettaa törmäystile enemyn ylle
    #ja muuttaa sen x-koordinaattia enemyn x-koordinaattimuutoksen mukaan
    def määritä_lähin_enemy(self):
        for sprite in self.enemyn_ryhmä.sprites():
            if abs(sprite.rect.x - self.rect.x) < self.välimatka:
                self.välimatka = abs(sprite.rect.x - self.rect.x)
                self.enemy = sprite

    def update(self):
        self.määritä_lähin_enemy()    
        self.rect.x = self.enemy.rect.centerx - 5

#Tässä luokassa määritellään ylempänä sivuttuun hahmoon liittyviä seikkoja. Hahmo siis hyppii edestakaisin vedessä, ja heittää pelaajan ilmaan mikäli pelaaja hyppää sen päälle.
#Hyvin pitkälti samaa koodia kuin aiemmissa vihollisluokissa, joten ei oikeastaan enempää selitettävää.
class VihannesPomppu(pygame.sprite.Sprite):
    def __init__(self,paikka,ryhma):
        super().__init__(ryhma)
        self.paikka = paikka
        self.image = pygame.image.load('./Kuvat/vihannes1.png').convert_alpha()
        self.kuva1 = pygame.image.load('./Kuvat/vihannes1.png').convert_alpha()
        self.kuva2 = pygame.image.load('./Kuvat/vihannes2.png').convert_alpha()
        self.kuva22 = pygame.image.load('./Kuvat/vihannes2.png').convert_alpha()
        self.kuva222 = pygame.image.load('./Kuvat/vihannes2.png').convert_alpha()
        self.kuva2222 = pygame.image.load('./Kuvat/vihannes2.png').convert_alpha()
        self.kuva3 = pygame.image.load('./Kuvat/vihannes3.png').convert_alpha()
        self.kuvat = [self.kuva1, self.kuva2, self.kuva22, self.kuva222, self.kuva2222, self.kuva3]
        self.rect = self.image.get_rect(topright = paikka)
        self.rect.y -= 5
        self.frame_index = 0
        self.animation_speed = 0.1

    def animoi(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.kuvat):
            self.frame_index = 0

        self.image = self.kuvat[int(self.frame_index)]
        if self.image == self.kuva2:
            self.rect.y -= 7
        elif self.image == self.kuva22:
            self.rect.y += 0.5
        elif self.image == self.kuva222:
            self.rect.y += 2
        elif self.image == self.kuva2222:
            self.rect.y += 4.5
        else:
            self.rect.y = 660

    def update(self):
        self.animoi()

#Luokka, jossa määritellään vihollisista kolmas. Edelleen hyvin samanlaista koodia. Luokkia olisi voinut yhdistää/käyttää periytymistä, mutta oh well.
class SininenTyyppi(pygame.sprite.Sprite):
    def __init__(self,paikka,ryhma,raja):
        super().__init__(ryhma)
        self.paikka = paikka
        self.image = pygame.image.load('./Kuvat/sininentyyppi1.png').convert_alpha()
        self.kuva1 = pygame.image.load('./Kuvat/sininentyyppi1.png').convert_alpha()
        self.kuva2 = pygame.image.load('./Kuvat/sininentyyppi2.png').convert_alpha()
        self.kuva3 = pygame.image.load('./Kuvat/sininentyyppi3.png').convert_alpha()
        self.kuvat = [self.kuva1, self.kuva2]
        self.kuva11 = pygame.image.load('./Kuvat/sininentyyppi11.png').convert_alpha()
        self.kuva22 = pygame.image.load('./Kuvat/sininentyyppi22.png').convert_alpha()
        self.kuva33 = pygame.image.load('./Kuvat/sininentyyppi3.png').convert_alpha()
        self.kuvat2 = [self.kuva11, self.kuva22]
        self.rect = self.image.get_rect(topright = paikka)
        self.rect.y += 4
        self.rect.x += 14
        self.frame_index = 0
        self.animation_speed = 0.05
        self.nopeus = 1
        self.liikkumis_laskuri = 1
        self.raja = raja

    def animoi(self):
        if self.nopeus < 0:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.kuvat):
                self.frame_index = 0

            self.image = self.kuvat[int(self.frame_index)]
        else:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.kuvat2):
                self.frame_index = 0

            self.image = self.kuvat2[int(self.frame_index)]

    def update(self):
        self.animoi()
        if self.liikkumis_laskuri % 2 == 0:
            self.rect.x += self.nopeus
        self.liikkumis_laskuri += 1
        if abs(self.liikkumis_laskuri) > self.raja:
            self.nopeus *= -1
            self.liikkumis_laskuri *= -1

#Luokka tankeille, jotka ampuvat raketteja. Ainoa logiikka liittyy lähinnä siihen, onko tankin tarkoitus olla oikealle vai vasemmalle
#päin kääntynyt. Asetetaan oikea kuva ja säädetään x-koordinaattia riippuen siitä, onko tankki asetettu oikeaksi vai vasemmaksi.
class Tankki(pygame.sprite.Sprite):
    def __init__(self,paikka,ryhma,vasenvaioikea):
        super().__init__(ryhma)
        self.paikka = paikka
        self.vasenvaioikea = vasenvaioikea
        if self.vasenvaioikea == 'vasen':
            self.image = pygame.image.load('./Kuvat/tankki1.png').convert_alpha()
        else:
            self.image = pygame.image.load('./Kuvat/tankki2.png').convert_alpha()

        self.rect = self.image.get_rect(topright = paikka)
        self.rect.y += 7

        if self.vasenvaioikea == 'oikea':
            self.rect.x += 55
        else:
            self.rect.x -= 27

#Luokka, jossa määritellään tankkien ampumiin raketteihin liittyvät seikat. Alunperin tarkoituksena oli, että kaikki tankit ampuisivat
#kaksi rakettia, "ylemmän" ja "alemman", mutta yllätyksekseni niiden piirtäminen pudotti fps:ää jonkin verran eikä oikein ollut siis
#sen arvoista, joten jokaisesta tankista lähtee nyt vain yksi raketti. Jotakin alempaa ja ylempää rakettia koskevaa luokan koodiin on
#vielä jäänyt, mutta jätän sen siihen siltä varalta, että palaan tähän projektiin joskus ja mietin miten saisin toteutettua tuplamäärän
#raketteja ilman fps-pudotusta. Koodi on hyvin pitkälti samaa kuin muissakin luokissa.
class Raketti(pygame.sprite.Sprite):
    def __init__(self,paikka,ryhma,vasenvaioikea,alempiylempi):
        super().__init__(ryhma)
        self.paikka = paikka
        self.vasenvaioikea = vasenvaioikea
        self.alempiylempi = alempiylempi
        if self.vasenvaioikea == 'vasen':
            self.räjähdys0 = pygame.image.load('./Kuvat/raketti1.png').convert_alpha()
        else:
            self.räjähdys0 = pygame.image.load('./Kuvat/raketti2.png').convert_alpha()
        self.image = self.räjähdys0
        self.rect = self.image.get_rect(topright = paikka)
        self.rect.y += 11
        if self.vasenvaioikea == 'vasen':
            self.rect.x += 10
        else:
            self.rect.x -= 13
        if self.alempiylempi == 'ylempi':
            self.rect.y += 15

        self.räjähdys1 = pygame.image.load('./Kuvat/pommi2.png').convert_alpha()
        self.räjähdys2 = pygame.image.load('./Kuvat/pommi3.png').convert_alpha()
        self.räjähdys3 = pygame.image.load('./Kuvat/pommi4.png').convert_alpha()
        self.räjähdys4 = pygame.image.load('./Kuvat/pommi5.png').convert_alpha()
        self.räjähdykset = [self.räjähdys1, self.räjähdys2, self.räjähdys3, self.räjähdys4]
        if self.vasenvaioikea == 'vasen':
            self.nopeus = -6
        else:
            self.nopeus = 6
        self.animation_speed = 0.1
        self.frame_index = 0
        self.räjähdys = False
        self.lähtöx = self.rect.x

    def update(self):
        self.rect.x += self.nopeus

        if self.räjähdys == True:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.räjähdykset):
                self.frame_index = 0

            self.image = self.räjähdykset[int(self.frame_index)]
        else:
            self.frame_index = 0

#Luokka, jossa määritellään pelaajahahmon "ystävään" liittyvät seikat.
class Ystävä(pygame.sprite.Sprite):
    def __init__(self,paikka,ryhma, alku):
        super().__init__(ryhma)
        self.paikka = paikka
        self.alku = alku
        self.image = pygame.image.load('./Kuvat/ystävä1.png').convert_alpha()
        self.kuva1 = pygame.image.load('./Kuvat/ystävä1.png').convert_alpha()
        self.kuva2 = pygame.image.load('./Kuvat/ystävä2.png').convert_alpha()
        self.kuva3 = pygame.image.load('./Kuvat/ystävä3.png').convert_alpha()
        self.kuva4 = pygame.image.load('./Kuvat/ystävä5.png').convert_alpha()
        self.kuva44 = pygame.image.load('./Kuvat/ystävä55.png').convert_alpha()
        self.kuva4_ = pygame.image.load('./Kuvat/ystävä5_.png').convert_alpha()
        self.kuva44_ = pygame.image.load('./Kuvat/ystävä55_.png').convert_alpha()
        self.kuva5 = pygame.image.load('./Kuvat/ystävä66.png').convert_alpha()

        self.kuva22 = pygame.image.load('./Kuvat/ystävä22.png').convert_alpha()
        self.kuva33 = pygame.image.load('./Kuvat/ystävä33.png').convert_alpha()
        self.kuvat = [self.kuva22, self.kuva22, self.kuva22, self.kuva33, self.kuva22, self.kuva22, self.kuva22, self.kuva22, self.kuva22, self.kuva33]
        self.kuvat2 = [self.kuva44, self.kuva44, self.kuva44, self.kuva44_, self.kuva44, self.kuva44, self.kuva44, self.kuva44, self.kuva44, self.kuva44_]
        self.kuvat3 = [self.kuva1, self.kuva1, self.kuva1, self.kuva2, self.kuva1, self.kuva1, self.kuva1, self.kuva1, self.kuva1, self.kuva2]
    
        self.rect = self.image.get_rect(topright = paikka)
        if self.alku == "kyllä":
            self.image = self.kuva1
        self.frame_index = 0
        self.animation_speed = 0.05
        self.nopeus = 1
        self.liikkumis_laskuri = 1
        self.cutscene = False

        self.xnopeus = 4

    #Tällä metodilla animoidaan ystävää räpyttämässä silmiään, jos hän katsoo vasemmalle.
    def animoi(self):      
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.kuvat):
            self.frame_index = 0

        self.image = self.kuvat[int(self.frame_index)]

    #Tällä metodilla animoidaan ystävää hyppäämässä.
    def animoi2(self):      
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.kuvat2):
            self.frame_index = 0

        self.image = self.kuvat2[int(self.frame_index)]

    #Tällä metodilla animoidaan ystävää räpyttämässä silmiään, jos hän katsoo oikealle.
    def animoi3(self):      
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.kuvat3):
            self.frame_index = 0

        self.image = self.kuvat3[int(self.frame_index)]

    #Tällä metodilla päivitetään ystävä-oliota riippuen siitä, onko kyseessä alussa vai lopussa oleva olio, ja onko "cutscene" käynnissä eli onko näytölle piirrettynä puhekuplaa.
    def update(self):
        if self.alku == "kyllä" and self.cutscene == True:
                self.animoi3()
        elif self.alku == "kyllä" and self.cutscene == False:
                self.animoi2()
                self.rect.x -= self.xnopeus
                self.rect.y -= 4
                if self.rect.x < 500:
                    self.frame_index = 0
                    self.kuvat2 = [self.kuva4, self.kuva4, self.kuva4, self.kuva4_, self.kuva4, self.kuva4, self.kuva4, self.kuva4, self.kuva4, self.kuva4_]
                    self.xnopeus *= -1
                    self.image = self.kuva4
                if self.rect.y < -40:
                    self.kill()
        elif self.alku == 'ei' and self.cutscene == True:
            self.animoi()
        else:
            self.animoi()

#Tässä luokassa määritellään alkuruutuun/alkuvalikkoon liittyvät seikat.
class Alkuruutu:
    #Init-metodi ottaa parametrina vastaan Taso-luokan luo_taso-metodin, jotta Alkuruutu-luokan olio voi sitä kutsua.
    def __init__(self, luo_taso):
        self.display_surface = pygame.display.get_surface()
        self.luo_taso = luo_taso
        self.alkuruutu = pygame.image.load('./Kuvat/alkuruutu.png').convert()
        self.hahmo = pygame.image.load('./Kuvat/alkuruutu_hahmo.png').convert_alpha()

        self.tiles = math.ceil(naytto_leveys / 1200) + 1
        self.scroll = 0
        self.y_suunta = 20
        self.x_suunta = 800
        self.lisäys = 100

    #Tämä metodi käynnistää alkuruudun/alkuvalikon.
    def run(self):
        #Tässä piirretään näytölle pilvellä lentävä pelaajahahmo, joka näytön reunan ylittäessään (x-suunnassa) siirtyy
        #takaisin toiseen reunaan ja muuttaa y-koordinaattiaan hieman.
        self.display_surface.blit(self.alkuruutu, (0,0))

        for i in range(0, self.tiles):
            self.display_surface.blit(self.hahmo, (1040 + self.scroll, self.y_suunta))

        self.scroll -= 2

        if abs(self.scroll) > 1200:
            self.scroll = 0
            self.y_suunta += self.lisäys
            if self.y_suunta > 600 or self.y_suunta < 100:
                self.lisäys *= -1

        #Jos alkuvalikossa oltaessa käyttäjä painaa enteriä, luodaan uusi taso.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.luo_taso()

#Ja vielä viimeisenä peli-luokka, jonka avulla kontrolloidaan sitä, näytetäänkö käyttäjälle alkuruutu/-valikko vai itse peli/taso.
#Käytetään status-muuttujaa apuna määriteltäessä, kumpi näytetään.
class Peli:
    def __init__(self):
        self.alkuruutu = Alkuruutu(self.luo_taso)
        self.status = 'alkuruutu'

    def luo_taso(self):
        self.taso = Taso(self.luo_alkuruutu)
        self.status = 'taso'

    def luo_alkuruutu(self):
        self.alkuruutu = Alkuruutu(self.luo_taso)
        self.status = 'alkuruutu'

    def run(self):
        if self.status == 'alkuruutu':
            self.alkuruutu.run()
        else:
            self.taso.run()