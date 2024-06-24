""" pembuatan game maze """

from pygame import*
import math as m
font.init()
init()

class karakter(sprite.Sprite):
    def __init__(self, filename, x, y, width, height):
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def tampil(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
class player(karakter):
    def kontrol(self, speed):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= speed
        if keys[K_s] and self.rect.y < (height-5):
           self.rect.y += speed
        if keys[K_a] and self.rect.x > 5:
           self.rect.x -= speed
        if keys[K_d] and self.rect.x < (width-5):
            self.rect.x += speed
class enemy(karakter):
    def mengejar(self, Player, speed):
        dx, dy = self.rect.x - Player.rect.x, self.rect.y - Player.rect.y
        dist = m.hypot(dx, dy)
        dx, dy = dx/dist, dy/dist
        self.rect.x -= dx * speed
        self.rect.y -= dy * speed


class wall():
    def __init__(self, x, y, width, height, color):
        self.rect = Rect(x,y,width,height)
        self.color = color
    def tampil(self):
        draw.rect(screen, self.color, self.rect)
    def touch_wall(self, player):
        return self.rect.colliderect(player)
        
width = 600
height = 600
p_width = 40
p_height = 40
p_speed = 5
e_width = 50
e_height = 50
e_speed = 2
k_width = 50
k_height = 50
k_speed = 0

screen = display.set_mode((width,height))
display.set_caption("Game labirin")
bg_image = transform.scale(image.load("penjara.png"),(width,height))

opal = player("opal.png", 300,20,p_width,p_height)
satpam = enemy("satpam.png",125,200,e_width,e_height)

warna_dinding = (0,0,0)
wall1 = wall(25,75,30,450,warna_dinding)
wall2 = wall(550,75, 30,450,warna_dinding)
wall3 = wall(25,75, 150,30,warna_dinding)
wall4 = wall(175,0,30,105, warna_dinding)
wall5 = wall(25,500,150,30,warna_dinding)
wall6 = wall(175,500,30,105,warna_dinding)
wall7 = wall(400,75,150,30,warna_dinding)
wall8 = wall(400,0,30,105,warna_dinding)
wall9 = wall(400,500,150,30,warna_dinding)
wall10 = wall(400,500,30,105,warna_dinding)
wall11 = wall(375,180,175,30,warna_dinding)
wall12 = wall(375,180,30,100,warna_dinding)
wall13 = wall(25,180,175,30,warna_dinding)
wall14 = wall(200,180,30,100,warna_dinding)
wall15 = wall(400,420,30,100,warna_dinding)
wall16 = wall(150,420,350,30,warna_dinding)
wall17 = wall(470,350,30,70,warna_dinding)
wall18 = wall(150,350,30,70,warna_dinding)


font1 = font.Font(None,70)
win = font1.render("OPAL UDAH BEBAS",True, (255, 234, 0))
lose = font1.render("OPAL DITANGKEP",True, (136, 8, 8))
sentuh_kunci = False
game_start = True

fps = time.Clock()
speedopal=8
speedsatpam=2
while game_start:
    screen.blit(bg_image, (0,0))
    opal.tampil()
    satpam.tampil()
    wall1.tampil()
    wall2.tampil()
    wall3.tampil()
    wall4.tampil()
    wall5.tampil()
    wall6.tampil()
    wall7.tampil()
    wall8.tampil()
    wall9.tampil()
    wall10.tampil()
    wall11.tampil()
    wall12.tampil()
    wall13.tampil()
    wall14.tampil()
    wall15.tampil()
    wall16.tampil()
    wall17.tampil()
    wall18.tampil()
    opal.kontrol(speedopal)
    satpam.mengejar(opal,speedsatpam)
    for e in event.get():
        if e.type == QUIT:
            quit()
    if sprite.collide_rect(opal,wall1) or sprite.collide_rect(opal,wall2) or sprite.collide_rect(opal,wall3) or sprite.collide_rect(opal,wall4) or sprite.collide_rect(opal,wall5) or sprite.collide_rect(opal,wall6) or sprite.collide_rect(opal,wall7) or sprite.collide_rect(opal,wall8) or sprite.collide_rect(opal,wall9) or sprite.collide_rect(opal,wall10) or sprite.collide_rect(opal,wall11) or sprite.collide_rect(opal,wall12) or sprite.collide_rect(opal,wall13) or sprite.collide_rect(opal,wall14) or sprite.collide_rect(opal,wall15) or sprite.collide_rect(opal,wall16) or sprite.collide_rect(opal,wall17) or sprite.collide_rect(opal,wall18):
        opal.rect.x=300
        opal.rect.y=20
    if sprite.collide_rect(opal,satpam):
        screen.blit(lose,(110,200))
        opal.rect.x=300
        opal.rect.y=20
        satpam.rect.x=125
        satpam.rect.y=200
    if (opal.rect.x>= 250 and opal.rect.x<350) and opal.rect.y>=585:
        screen.blit(win,(110,200))
        speedopal=0
        speedsatpam=0
    display.update()
    fps.tick(60)
    