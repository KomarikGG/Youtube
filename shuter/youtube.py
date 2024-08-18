from typing import Any
from pygame import*
from random import randint
window = display.set_mode((800,700))
display.set_caption('back_shuter')
#back_shuter = transform.scale(image.load(''),(600,500))
font.init()
font1 = font.SysFont('Arial',36)
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,w,h,x,y,speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
granica = 450
knopka = GameSprite('perezagruzka.png',100,100,135,30,0)
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 710:
            self.rect.x += self.speed
    def fire(self):
        keys_pressed = key.get_pressed()
        bulit.add(Bullet('like.png',20,20,self.rect.x,self.rect.y,15))
        bulit.add(Bullet('like.png',20,20,self.rect.right -20,self.rect.y,15))  
        #if keys_pressed[K_SPACE]:
            #bulit.add(Bullet('like.png',20,20,self.rect.x,self.rect.y,15))
            #bulit.add(Bullet('like.png',20,20,self.rect.right -20,self.rect.y,15))            
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if sprite.collide_rect(self,canal):
            self.rect.y = 0
            self.rect.x = randint(0,750)
            global lost
            lost += 1
class  Bullet(GameSprite):
    def __init__(self, player_image, w, h, x, y, speed):
        super().__init__(player_image, w, h, x, y, speed)
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
bulit = sprite.Group()
bad_coments = sprite.Group()
for i in range(5):
    bad_coment = Enemy('coment.png',50,50, randint(0,750),0,randint(1,3))
    bad_coments.add(bad_coment)
YouTube = Player('player.png',90,60,310,500,10)
canal = GameSprite('canallll.png',800,130,0,570,0)
game = True
clock = time.Clock()
fps = 60
lost = 0
score = 0
win = transform.scale(image.load('wiinn.png'),(800,700))
no_win = transform.scale(image.load('no win.png'),(800,700))
finish = False
while game == True:
    #window.blit(back_shuter,(0,0))
    if finish == False:
        #YouTube.fire()
        window.fill((255,255,255))
        YouTube.reset()
        YouTube.update()
        canal.reset()
        bulit.update()
        bulit.draw(window)
        bad_coments.draw(window)
        bad_coments.update()
        text_lose = font1.render(
            'lost: ' + str(lost),1,(0,0,0)
        )
        window.blit(text_lose,(10,10))
        text_score = font1.render(
            'score: ' + str(score),1,(0,0,0)
        )
        window.blit(text_score,(10,50))
        if sprite.groupcollide(bad_coments,bulit,True,True):
            score += 1
            bad_coment = Enemy('coment.png',50,50, randint(0,750),0,randint(1,3))
            bad_coments.add(bad_coment) 
        if lost == 20 or sprite.spritecollide(YouTube,bad_coments,True):
            window.blit(no_win,(0,0))
            knopka.reset()
            finish = True
        if score == 100:
            window.blit(win,(0,0))
            knopka.reset()
            finish = True
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == MOUSEBUTTONDOWN:
            print(i.pos)
            x,y =  i.pos      
            if knopka.rect.collidepoint(x,y):
                finish = False
                score = 0
                lost = 0
                for m in bad_coments:
                    m.kill()
                for b in bulit:
                    b.kill()
                for g in range(5):
                    bad_coment = Enemy('coment.png',50,50, randint(0,750),0,randint(1,3))
                    bad_coments.add(bad_coment)                
        if i.type == KEYDOWN:
            if i.key ==  K_SPACE:
                YouTube.fire()
    display.update()
    clock.tick(fps)