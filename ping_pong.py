# модули
from pygame import *
import os
from random import *
init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
mixer.init()
font.init()
clock = time.Clock()

# текст
text = font.SysFont('Arial', 40)

loose_red = text.render(
    'LOOSE RED!', True, (255, 215, 0)
)

loose_blue = text.render(
    'LOOSE BLUE!', True, (255, 215, 0)
)


# ФПС
fps = 60

# положение
x1 = 30
y1 = 200

x2 = 720
y2 = 200

# экран
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
window = display.set_mode((800, 500))
display.set_caption('Шутер')

# цвет
color = (255, 250, 205)

# скорость мяча
d_x = 3
d_y = 3

# классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 160))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

# спрайты
player1 = Player('red.png', 5, x1, y1)
player2 = Player('blue.png', 5, x2, y2)
ball = GameSprite('ball.png', 3, 200, 200)
ball.image = transform.scale(image.load('ball.png'),(50, 50))


run = True
finish = False
timer = 300
# цикл
while run:
    for e in event.get():
        keys_pressed = key.get_pressed()
        if e.type == QUIT:
            run = False
            
    if finish != True:
        # фон
        window.fill((255, 255, 255))

        # проверка столкновения мяча
        ball.rect.x += d_x
        ball.rect.y += d_y

        if sprite.collide_rect(player1, ball):
            d_x *= -1
        if sprite.collide_rect(player2, ball):
            d_x *= -1
        if ball.rect.y < 0 or ball.rect.y > SCREEN_HEIGHT - 50:
            d_y *= -1
        if ball.rect.x < 0:
            window.blit(loose_red, (200, 200))
            finish = True
        if ball.rect.x > SCREEN_WIDTH - 50:
            window.blit(loose_blue, (200, 200))
            finish = True
        # увеличение скорости каждые 5 секунд
        if timer == 0:
            timer = 300
            if d_x < 0:
                d_x -= 1
            else:
                if d_y > 0:
                    d_y += 1
        else:
            timer -= 1

        # отрисовка спрайтов
        player1.draw()
        player1.update1()
        player2.draw()
        player2.update2()
        ball.draw()




    # обновление экрана и ФПС
    display.update()
    clock.tick(fps)
