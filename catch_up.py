from pygame import *

#створи вікно гри
WIDTH, HEIGHT = 800, 600
window = display.set_mode((WIDTH, HEIGHT))
FPS = 60
display.set_caption("Доганялки")
clock = time.Clock() #Стоворюємо ігровий таймер
#задай фон сцени
bg = image.load("background.png")
sprite1_img =image.load("sprite1.png")
sprite2_img =image.load("sprite2.png")

bg = transform.scale(bg, (WIDTH, HEIGHT))
#створи 2 спрайти та розмісти їх на сцені
class GameSprite:
    def __init__(self, sprite_image, width, height, x, y):
        self.image = transform.scale(sprite_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, window):
        window.blit(self.image, self.rect)

player1 = GameSprite(sprite1_img, 60, 60, 100, 250,)
player2 = GameSprite(sprite1_img, 60, 60, 400, 250,)


while True:
#оброби подію «клік за кнопкою "Закрити вікно"»
    for e in event.get():
        if e.type == QUIT:
            quit()
    keys = key.get_pressed()
    if keys[K_w]:
        player1.rect.y -= 5
    if keys[K_s]:
        player1.rect.y += 5
    if keys[K_a]:
        player1.rect.x -= 5
    if keys[K_d]:
        player1.rect.x += 5

    if keys[K_UP]:
        player2.rect.y -= 5
    if keys[K_DOWN]:
        player2.rect.y += 5
    if keys[K_LEFT]:
        player2.rect.x -= 5
    if keys[K_RIGHT]:
        player2.rect.x += 5
    
        



    window.blit(bg, (0,0))
    player1.draw(window)
    player2.draw(window)
    display.update()
    clock.tick(FPS)
