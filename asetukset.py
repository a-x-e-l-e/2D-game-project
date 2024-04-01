#Axel Eloniemi NTIS21K

#Tässä tiedostossa on määritetty tiettyjä asetuksia kuten tilejen koko ja näytön mitat.
#Lisäksi olennaisimpana osana tiedostoa löytyy myös tasokartta, jota käytetään tason piirtämiseen.
#Alla lyhyet selitykset tasokartan symboleille:

#w tarkoittaa vettä(pintavesi) ja W (pinnan alla)
#T tiili-tileä
#P tarkoittaa pelaajaa
#s tarkoitaa siltaa
#. tarkoittaa törmäystileä -> jos pelaaja törmää siihen, alla oleva vihollinen kuolee/katoaa
#i tarkoittaa puuta --> jätä alle kaksi tyhjää ruutua, jotta puu olisi maassa
#a tarkoittaa vihollista, joka pudottelee pommeja (liikkuu ensin oikealle)
#A tarkoittaa vihollista, joka pudottelee pommeja (liikkuu ensin vasemmalle)
#b tarkoittaa pommia
#c tarkoittaa crab (vihollinen)
#d tarkoittaa pomppivaa vihannesta (heittää pelaajan ilmaan)
#e tarkoittaa sinistä tyyppiä (vihollinen)
#E tarkoittaa sinistä tyyppiä (vihollinen), joka liikkuu leveämmällä alueella
#F tarkoittaa vasemmalle osoittavaa tankkia
#f tarkoittaa oikealle osoittavaa tankkia
#G tarkoittaa vasemmalle osoittavaa, ylempää rakettia
#g tarkoittaa vasemmalle osoittavaa, alempaa rakettia
#H tarkoittaa oikealle osoittavaa, ylempää rakettia
#h tarkoittaa oikealle osoittavaa, alempaa rakettia
#k tarkoittaa ystävää alussa
#K tarkoittaa ystävää lopussa

#X tarkoittaa "keskitileä", eli tileä jonka molemmille sivuille ja alle voi liittää tilejä
#x tarkoittaa "sisätileä", eli tileä jonka kaikille sivuille voi liittää tilejä
#u tarkoittaa sisätileä, jonka kaikille muille puolille paitsi ylle voi liittää tilejä
#U tarkoittaa sisätileä, jonka ala- ja yläpuolelle voi liittää tilejä

#1 tarkoittaa sellaista sisätileä, jonka kaikille muille paitsi vasemmalle puolelle voi liittää tilejä
#2 on toinen variaatio (y) ylemmästä

#3 tarkoittaa sellaista sisätileä, jonka oikealle puolelle ja yläpuolelle voi liittää tilejä
#4 tarkoittaa sellaista sisätileä, jonka vasemmalle puolelle ja yläpuolelle voi liittää tilejä

#5 tarkoittaa sellaista sisätileä, jonka kaikille muille puolille paitsi alapuolelle voi liittää tilejä

#7 tarkoittaa sellaista sisätileä, jonka kaikille muille puolille paitsi oikealle puolelle voi liittää tilejä
#6 on toinen variaatio (y) ylemmästä 

#L tarkoittaa tileä, jonka oikealle puolelle voi liittää tilejä
#R tarkoittaa tileä, jonka vasemmalle puolelle voi liittää tilejä

#Z tarkoittaa tileä, jonka oikealle ja vasemmalle puolelle voi liittää tilejä

#Y on toinen variaatio X-tilestä
#y on toinen variaatio x-tilestä

#O tarkoittaa tileä, jonka vasemmalle puolelle ja alapuolelle voi liittää tilejä
#o on toinen variaatio O-tilestä

#V tarkoittaa tileä, jonka oikealle puolelle ja alapuolelle voi liittää tilejä
#v on toinen variaatio V-tilestä

#M tarkoittaa tileä, jonka millekään puolelle ei voi liittää tilejä
#m tarkoittaa tileä, jonka alapuolelle voi liittää tilejä

#J tarkoittaa loppupuhekuplaa
#j tarkoitaa alkupuhekuplaa

tasokartta1 = [
'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ',
'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ',
'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ',
'                                                                      M                    .                                                                                                                                                                                                            A                     A                     A                     A                     A                     A                                                                                                                                                                                                                                                 ',
'                                                                                           c                        ,                                                                                                                                                                                   b                     b                     b                     b                     b                     b                                                                                                                                                                                                                                                 ',
'                                                          e    M                   MsssssssssssssM    M             e                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ',
'                                                         LR                                                M     LZZZR                                                                                                                          a                                            a                     a                     a                     a                     a                     a                                                                       .                                                                                                                                                                                    ',
'                                                                                                                                                                                                                                                b                                            b                     b                     b                     b                     b                     b                                                       M               c                                                             M     TTTTTTTTTTT      M                                                                                               ',
'                             i                                              M                                                                                                                                                                                                                                                                                                                                                                                                  LZZZZR                                                      M           G  FTTT  f  H          M                                                                                         ',
'                                i                                                                                                                                                                                                     A                    A                      A                                                                                                                                                                          LR         M                                                                              g   TTT     h                                                                                                    ',
'                                                                                                                          LZR           M                                                                                             b                    b                      b                                                                                                                                                                                                     M                                              M               TTTTTTTTTTT              M      M                                    M                                           ',
'                             VXO                     M                        LR                                                              M              M                                                                                                                                                                                                                                                                                                                                                                    LR                   G  FTTT  f  H                                                                                                    ',
'                             2yyYYo            LR                  LR                           LR                                M                                                                                        a                     a                     a                                                                                                                                                                                                                     M                   M                                     g   TTT     h                                                    M                                  J            ',
'                             355554          LR                                                                 LR                                   LZZR                                                                  b                     b                     b                                                                                                                                                                                                                                                M    LR                        TTTTTTTTTTT                        M                                        LZZZR                                ',
'                                      m                     vo            LR                                                                                                                                                                                                                                                                                                                                                                                                                                  M                                        G  FTTT  f  H                                                M                                                   ',
'                                      U                     3xO                                        M                                                                                                                                                                                                                                                                             M                                                                                LR                          M                                                    g   TTT     h                                      M                                                i    i       ',
'                          j           2YYo             vo    2yXo                                                     M                                                                                                                                                                                                                                                       M                  LZR                                                                                                     LR                                            TTTTTTTTTTT           M                M      M           M                          M                           ',
'                                      1xxxO            34    3554                                                                                                                                                                                                                                                LR                                       M                                              M         M         M                                                                                                                         G  FTTT  f  H              M                                                                            K        ',
'                                 LR   2yyy6      i                                       M                                                                                                         VXO                                                                                                                   M            LR       LZZR                      LR                M                  M         M                                                     M                                                                        g   TTT     h                                                                              LXXXXXXXXXXXXXXXR     ',
'                                      1xxx7                                                                                  M                                                          vYYYO      2yyYo                         LR                   LR                   LR                        LZR    LR                                                                                                                                                                                       LR                                                TTTTTTTTTTT                                                                                 3xxxxxxxxxxxxx4      ',
'                                     vyyyy6                               M     M                                                                                          ,        VXXXxxxx7      1xxx7              ,                     ,                    ,                   ,         M                                 M                              LZR                                                                 M           ,                                                                                                      G  FTTT  f  H                                                                                3555555555554       ',
'                           k P VXXXXXxxxxxxXXXXXXXXXXo*wwwvXXXXXXO                                                                                                         E     vYYyyyyyyyy6      2yyy6              E                     E                    E                   E                                                                                                                                                          E        d                                                                                             g   TTT     h                                                                                                    ',
'-wwwwwwwwwwwwwwwwwwwwwwwwwvYYYYyyyyyyyyyyyyyyyyyyyyyyyuuuuyyyyyyyyowwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwVXXXXXXXXXXXxxxxxxxxxxx7wwwwww1xxx7wwwVXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXO-wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwVXXXXXXXOwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww-wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwTTTTTTTTTTTwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
'_WWWWWWWWWWWWWWWWWWWWWWWWW1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxXXXOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW1yyyyyyyyyyyyyyyyyyyyyy6WWWWWW2yyy6WWW1yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy6_WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW1xxxxxxx6WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW_WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWTTTTTTTTTTTWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
]

tile_koko = 30
naytto_leveys = 1000

naytto_korkeus = len(tasokartta1) * tile_koko 

kamera_rajat = {
    'oikea': 300,
    'vasen': 300,
    'ylä': 300,
    'ala': 300
}
