#Импорт модулей
from pygame import *
from random import randint
font.init()
#Создание текста
font1 = font.SysFont('Arial', 150)
font4 = font.SysFont('Arial', 150)
font3 = font.SysFont('Arial', 100)
font2 = font.SysFont('Arial', 100)
#Переменные


global score_2
global finish
finish = False
game = True
score_1 = 0
score_2 = 0
#Cоздание классов  

class GameSprite(sprite.Sprite):
    def __init__(self, player_height , player_wight , player_image , player_x , player_y , player_speed_y , player_speed_x):
        super().__init__()
        self.height = player_height
        self.wight = player_wight
        self.image = transform.scale(image.load(player_image),(player_height , player_wight))
        self.speed_y = player_speed_y
        self.speed_x = player_speed_x
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < 560:
            self.rect.y += self.speed_y
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed_y
    

class Player3(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < 560:
            self.rect.y += self.speed_y
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed_y


class Ball(GameSprite):
    
    def update(self): 
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x          
        if self.rect.y > 635:   
            self.speed_y = -1* self.speed_y
            self.speed_x = 1* self.speed_x                    
        if self.rect.y < 10:
            self.speed_y = -1* self.speed_y
            self.speed_x = 1* self.speed_x  
        if self.rect.x < 10:
            self.speed_y = 1* self.speed_y
            self.speed_x = -1* self.speed_x  
            global score_2
            score_2 += 1
        if self.rect.x > 830:
            self.speed_y = 1* self.speed_y
            self.speed_x = -1* self.speed_x  
            global score_1
            score_1 += 1     
           

            
    # def finnish(self): 
    #     self.rect.y += self.speed
    #     self.rect.x += self.speed           
    #     if self.rect.x > 845:
    #         finish == True   
    #         window.blit(win2,(10, 10))
    #     if self.rect.x < 10: 

    #         finish == True  
    #         window.blit(win3,(10, 10))




             



#Прорисовка обьектов
#mixer.init()
#mixer.music.load('zvuki-goroda-shosse.ogg')
#mixer.music.play()

window = display.set_mode((900,700))
display.set_caption('Пинг Понг')
background = transform.scale(image.load("doroga.png"), (900,700))
clock = time.Clock()
FPS = 160
x1 = 1
y1 = 250
x2 = 829
y2 = 250
speed_y = 15
speed_x = 15
#Основный обьекты
platforms = sprite.Group()
player1 = Player(80 , 125 ,"free-icon-step-6117127.png" , x1 , y1 , 19 , 0)
player2 = Player3(80 , 125 ,"free-icon-step-61171272323.png" , x2 , y2 , 19 , 0)
ball1 = Ball(50 , 50 ,"free-icon-ball-802340.png" , 500 , 500 , speed_y , speed_x)
platforms.add(player1)
platforms.add(player2)
#

while game:

    window.blit(background,(0, 0))

    background = transform.scale(image.load("doroga.png"), (900,700))
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
      
      

    #Игра
    if finish != True:
        window.blit(background,(0, 0))

        text = font1.render(str(score_1),1,(255, 255, 255))
        window.blit(text,(25, 10))
        text2 = font1.render(str(score_2),1,(255, 255, 255))
        window.blit(text2,(800, 10))        
        #Победа
        #Поражение
       # sprites_list = sprite.spritecollide(
        #    player , cars, False
       # )          
        #if sprite.spritecollide(player1 , ball1, False):
         #   self.rect.y -= self.speed
         #   self.rect.x -= self.speed 
        sprites_list = sprite.spritecollide(
            ball1 , platforms, False
        )    
        if sprite.spritecollide(ball1 , platforms, False):
            ball1.speed_y = 1* ball1.speed_y
            ball1.speed_x = -1* ball1.speed_x  

        
        if score_1 >= 25:
            finish = True
            text3 = font3.render('PLAYER 1 WIN!',1,(255, 0, 0))
            window.blit(text3,(150, 250))   
        if score_2 >= 25:
            finish = True
            text4 = font2.render('PLAYER 2 WIN!',1,(255, 0, 0))
            window.blit(text4,(150, 250))               
        player1.update()
        player1.reset()     
    
        player2.update()
        player2.reset()     

        ball1.update()
        # ball1.finnish()       
        ball1.reset()    

        display.update()    
    
