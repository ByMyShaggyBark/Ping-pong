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
img_tennisball = "tenis_ball.png"

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
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

l_racket = Player(img_racket, 30, 200, 4, 50, 150)
r_racket = Player(img_racket, 430, 200, 4, 50, 150)
ball = GameSprite(img_tennisball, 250, 250, 4, 50, 50)

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


    l_racket.update_l()
    r_racket.update_r()
    ball.update()

    l_racket.reset()
    r_racket.reset()
    ball.reset()
    display.update()
    
    time.delay(50)