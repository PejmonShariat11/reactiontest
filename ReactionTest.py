import pygame, random, sys
from pygame.locals import *
from pygame.font import *
from pygame import *
from pygame.sprite import *

class Pepe(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load('peeposad.jpg')
        self.image2 = image.load('w_key.png')
        self.image3 = image.load('a_key.png')
        self.image4 = image.load('d_key.png')
        self.image5 = image.load('e_key.png')
        self.image6 = image.load('q_key.png')
        self.image7 = image.load('s_key.png')
        self.image8 = image.load('shift_key.png')
        self.rect = self.image.get_rect()
        self.rect = self.image2.get_rect()
        self.rect = self.image3.get_rect()
        self.rect = self.image4.get_rect()
        self.rect = self.image5.get_rect()
        self.rect = self.image6.get_rect()
        self.rect = self.image7.get_rect()
        self.rect = self.image8.get_rect()
        self.spot()
        self.draw(screen, 0)

    def spot(self):
        self.rect.top = random.randint(40, 680)
        self.rect.left = random.randint(0, 1520)
        self.rect.topleft = (self.rect.left, self.rect.top)

    def draw(self, screen, randnum):
        screen.blit(self.image, (self.rect.left, self.rect.top))
        self.drawnewkey(randnum)
        screen.blit(self.image9, (self.rect.left + 68, self.rect.top))
        pygame.display.update()

    def drawnewkey(self, randkey):

        if (randkey == 0):
            self.image9 = self.image2
        elif (randkey == 1):
            self.image9 = self.image3
        elif (randkey == 2):
            self.image9 = self.image4
        elif (randkey == 3):
            self.image9 = self.image5
        elif (randkey == 4):
            self.image9 = self.image6
        elif (randkey == 5):
            self.image9 = self.image7
        elif (randkey == 6):
            self.image9 = self.image8
        return self.image9



pygame.init()
display.set_caption('Whack a PePe reaction game')
screen = display.set_mode((1620, 780))
mypepe = Pepe()
black = (0, 0, 0)
white = (255, 255, 255)
score = 0
scorefont = pygame.font.SysFont("monospace", 40)
pygame.display.update()
running = True
clock = time.Clock()
timer1 = time.get_ticks() / 1000
randnum = random.randint(0, 6)
song1 =pygame.mixer.music.load('giornopiano.wav')
pygame.mixer.music.play(-1, 0)
effect = pygame.mixer.Sound('oof.wav')
effect2 = pygame.mixer.Sound('headshot.wav')
finalcount = 0
secondpress = False
while running:
    label1 = scorefont.render('Score: ' + str(score), 1, white)
    screen.blit(label1, (0, 0))
    timer = time.get_ticks() / 1000
    label2 = scorefont.render('time passed: ' + str(timer), 1, white)
    screen.blit(label2, (500, 0))
    pygame.display.update()
    screen.fill(black)
    screen.blit(label2, (500, 0))
    screen.blit(label1, (0, 0))
    mypepe.draw(screen, randnum)
    pygame.display.update()
    if (score>=0):
        for event in pygame.event.get():
            secondpress = False

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif (secondpress == False):
                print(randnum)
                if (event.type == KEYDOWN):
                    if event.key == K_w:
                        if randnum == 0:
                            score += 1
                            effect2.play()
                        else:
                            score -= 1
                        mypepe.spot()
                        screen.fill(black)
                        randnum = random.randint(0, 6)
                        mypepe.draw(screen, randnum)
                        secondpress = True
                    if event.key == K_a:
                        if randnum == 1:
                            score += 1
                            effect2.play()
                        else:
                            score -= 1
                        mypepe.spot()
                        screen.fill(black)
                        randnum = random.randint(0, 6)
                        mypepe.draw(screen, randnum)
                        secondpress = True
                    if event.key == K_d:
                        if randnum == 2:
                            score += 1
                            effect2.play()
                        else:
                            score -= 1
                        mypepe.spot()
                        screen.fill(black)
                        randnum = random.randint(0, 6)
                        mypepe.draw(screen, randnum)
                        secondpress = True
                    if event.key == K_e:
                        if randnum == 3:
                            score += 1
                            effect2.play()
                        else:
                            score -= 1
                        mypepe.spot()
                        screen.fill(black)
                        randnum = random.randint(0, 6)
                        mypepe.draw(screen, randnum)
                        secondpress = True
                    if event.key == K_q:
                        if randnum == 4:
                            score += 1
                            effect2.play()
                        else:
                            score -= 1
                        mypepe.spot()
                        screen.fill(black)
                        randnum = random.randint(0, 6)
                        mypepe.draw(screen, randnum)
                        secondpress = True
                    if event.key == K_s:
                        if randnum == 5:
                            score += 1
                            effect2.play()
                        else:
                            score -= 1
                        mypepe.spot()
                        screen.fill(black)
                        randnum = random.randint(0, 6)
                        mypepe.draw(screen, randnum)
                        secondpress = True
                    if event.key == K_LSHIFT:
                        if randnum == 6:
                            score += 1
                            effect2.play()
                        else:
                            score -= 1
                        mypepe.spot()
                        screen.fill(black)
                        randnum = random.randint(0, 6)
                        mypepe.draw(screen, randnum)
                        secondpress = True
                    timer1 = timer
        else:
            if(timer1<20):
                time_new = (time.get_ticks() / 1000) - timer1
                time_get = time_new % 3
                if (time_get >= 2.99 ):
                    score -= 1
                    mypepe.spot()
                    screen.fill(black)
                    randnum = random.randint(0, 6)
                    mypepe.draw(screen, randnum)
            elif(timer1>=20 and timer1<40):
                time_new = (time.get_ticks() / 1000) - timer1
                time_get = time_new % 2.5
                if (time_get >= 2.49):
                    score -= 1
                    mypepe.spot()
                    screen.fill(black)
                    randnum = random.randint(0, 6)
                    mypepe.draw(screen, randnum)
            elif(timer1>=40 and timer1<60):
                time_new = (time.get_ticks() / 1000) - timer1
                time_get = time_new % 2
                if (time_get >= 1.99):
                    score -= 1
                    mypepe.spot()
                    screen.fill(black)
                    randnum = random.randint(0, 6)
                    mypepe.draw(screen, randnum)
            elif (timer1 >= 60 and timer1 < 80):
                time_new = (time.get_ticks() / 1000) - timer1
                time_get = time_new % 1.5
                if (time_get >= 1.49):
                    score -= 1
                    mypepe.spot()
                    screen.fill(black)
                    randnum = random.randint(0, 6)
                    mypepe.draw(screen, randnum)
            elif (timer1 >= 80 and timer1 < 100):
                time_new = (time.get_ticks() / 1000) - timer1
                time_get = time_new % 1
                if (time_get >= .99):
                    score -= 1
                    mypepe.spot()
                    screen.fill(black)
                    randnum = random.randint(0, 6)
                    mypepe.draw(screen, randnum)
            elif (timer1 >= 100 and timer1 < 120):
                time_new = (time.get_ticks() / 1000) - timer1
                time_get = time_new % .75
                if (time_get >= .745):
                    score -= 1
                    mypepe.spot()
                    screen.fill(black)
                    randnum = random.randint(0, 6)
                    mypepe.draw(screen, randnum)
            elif (timer1 >= 120 and timer1 < 140):
                time_new = (time.get_ticks() / 1000) - timer1
                time_get = time_new % .5
                if (time_get >= .495):
                    score -= 1
                    mypepe.spot()
                    screen.fill(black)
                    randnum = random.randint(0, 6)
                    mypepe.draw(screen, randnum)
            elif (timer1 >= 140):
                time_new = (time.get_ticks() / 1000) - timer1
                time_get = time_new % .35
                if (time_get >= .345):
                    score -= 1
                    mypepe.spot()
                    screen.fill(black)
                    randnum = random.randint(0, 6)
                    mypepe.draw(screen, randnum)
    else:
        pygame.mixer.music.stop()
        finaltime = timer1
        screen.fill(black)
        label10 = scorefont.render("Game Over! You made it " + str(finaltime) + " seconds! Congratulations! ", 1, white)
        screen.blit(label10, (0, 500))
        effect.play()
        pygame.time.delay(1000)
        pygame.display.update()
        pygame.mixer.music.load('megalovania.wav')
        pygame.mixer.music.play(1, 0)
        finalcount += 1
        pygame.time.delay(20000)
        running = False









