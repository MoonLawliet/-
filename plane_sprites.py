import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT =  pygame.USEREVENT + 1



class GameSprites(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=5):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect =self.image.get_rect()
        self.speed = speed
    def update(self, *args):
        self.rect.y += self.speed

class Background(GameSprites):
    def __init__(self, alt = False):
        super().__init__("./images/background.png")
        if alt:
            self.rect.y = -self.rect.height            
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
        pass

class Enemy(GameSprites):
    def __init__(self):
        super().__init__("./images/enemy1.png") 
        #敌机随机速度
        self.speed = random.randint(5,10)
        #敌机随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            #print("从精灵组删除")
            self.kill()
            
    def __del__(self):
        #print("敌机销毁"%self.rect)
        pass
                
class Hero(GameSprites):
    def __init__(self,speedy = 0):
        #调用父类，设置图片和速度
        super().__init__("./images/me1.png",0)
        #设置英雄初始位置
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.rect.centerx = SCREEN_RECT.centerx
        #垂直移动初始化
        self.speedy = speedy
        #子弹精灵组
        self.bullets = pygame.sprite.Group()
    def update(self):
        #水平方向移动    
        self.rect.x += self.speed
        #垂直方向移动
        self.rect.y += self.speedy
        #英雄不离开屏幕
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
    def fire(self):
        #print("发射子弹")
        #发射3枚子弹
        for i in (0,1,2):
            #创建子弹精灵
            bullet = Bullet()
            #设置精灵位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx =self.rect.centerx
            #子弹精灵添加到子弹精灵组
            self.bullets.add(bullet)

            
class Bullet(GameSprites):
    def __init__(self):
        super().__init__("./images/bullet1.png",-8)

        
    def update(self):
        super().update()
        #子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()
    def __del__(self):
        #print("子弹销毁")
        pass
          
