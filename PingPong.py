from pygame import *
from random import randint
from time import time as timer

print("Управление на WASD, UP DOWN LEFT RIGHT")

back = (100, 200, 255)
font.init()
font1 = font.SysFont(None, 80)
win_l = font1.render("Left won!", True, (255,25,255))
win_r = font1.render("Right won!", True, (255,25,255))

img_racket = "racket.png"
img_tennisball = "tennis_ball.png"

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

win_width = 500
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))
window.fill(back)

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        display.update()
    
    time.delay(50)