from PygameGameUpgrades import *
import random
import os


col = []
op = []
try:
    f = open('GameData.txt', mode='r')
    data = f.readlines()
    col = list(map(lambda x: int(x), data[0].split(',')))
    op = list(map(lambda x: x.split('\n')[0], data[2:]))
    m = float(data[1])
    openn = False
except Exception:
    f = open('GameData.txt', mode='w')
    f.write('0,0,0,0,0,0,0,0,0,0,0,0,0,0\n')
    f.write('10')
    op = ['open', 'open', 'closed', 'closed', 'closed', 'closed', 'closed', 'closed',
         'closed', 'closed', 'closed', 'closed', 'closed', 'closed']
    for i in op:
        f.write(i)
    col = list(map(lambda x: int(x), '0,0,0,0,0,0,0,0,0,0,0,0,0,0'.split(',')))
    m = 10
    openn = True
f.close()

pygame.init()
screen = pygame.display.set_mode((1300, 650))


class Foun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(foun)
        f = pygame.image.load('Icons/Фон.png')
        f = pygame.transform.scale(f, (750, 400))
        f = f.convert_alpha()
        self.image = f
        self.rect = self.image.get_rect().move(0, 0)


class Shop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(sprite_group)
        test = pygame.image.load('Icons/Магазин.png')
        test = pygame.transform.scale(test, (750, 2150))
        test = test.convert_alpha()
        self.image = test
        self.rect = self.image.get_rect().move(0, 400)

    def update(self, a=0):
        if self.rect.y == 400 and a == 10:
            a = 0
        if self.rect.y == -1500 and a == -10:
            a = 0
        self.rect = self.rect.move(0, a)


class Button(pygame.sprite.Sprite):
    def __init__(self, a):
        super().__init__(buttons)
        self.nom = a
        self.money = money
        self.work = True
        if a % 2 == 0:
            self.image = pygame.image.load('Icons/Buy1.png')
            self.rect = self.image.get_rect().move(575, 450 + a * 75)
            self.text = Text(a // 2, 175, 450 + a * 75)
            self.icon = Icon(a // 2, 25, 450 + a * 75)
            texts.append(self.text)
            ic.append(self.icon)
        else:
            self.image = pygame.image.load('Icons/Buy10.png')
            self.rect = self.image.get_rect().move(575, 515 + (a - 1) * 75)
            self.text = texts[a // 2]

    def update(self, a=0, pos=None):
        if pos is not None:
            self.check_click(pos)
        if self.nom % 2 == 0:
            if self.rect.y == 450 + self.nom * 75 and a == 10:
                a = 0
            if self.rect.y == -1450 + self.nom * 75 and a == -10:
                a = 0
        else:
            if self.rect.y == 515 + (self.nom - 1) * 75 and a == 10:
                a = 0
            if self.rect.y == -1385 + (self.nom - 1) * 75 and a == -10:
                a = 0
        self.rect = self.rect.move(0, a)

    def check_click(self, pos):
        if self.work and sdv == -1 and 575 <= pos[0] <= 725 and self.rect.y <= pos[1] <= self.rect.y + 50:
            if self.nom % 2 == 0 and self.money.get_val() > costs[self.nom] - 1:
                col[self.nom // 2] += 1
                self.text.change_col()
                self.money.money_change(costs[self.nom])
            elif self.money.get_val() > costs[self.nom] - 1:
                col[self.nom // 2] += 10
                self.text.change_col()
                self.money.money_change(costs[self.nom])


class Text(pygame.sprite.Sprite):
    def __init__(self, n, x, y):
        super().__init__(text_group)
        self.font = pygame.font.Font('Anonymous_Pro.ttf', 21)
        self.nom = n
        c = costs[self.nom * 2]
        s = ''
        while float(c) > 1000:
            c = str(round(float(c) / 1000))
            s += 'k'
        c = str(c) + s
        d = pri[self.nom]
        s = ''
        while float(d) >= 1000:
            d = str(round(float(d) / 1000))
            s += 'k'
        d = str(d) + s
        self.t = self.font.render(names[self.nom] + f'  {c} за штуку', True, (255, 255, 255))
        self.t2 = self.font.render(f'Производит {d} носков в день', True, (255, 255, 255))
        self.t3 = self.font.render(f'У вас {col[self.nom]} штук', True, (255, 255, 255))
        self.image = pygame.Surface([400, 200], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect().move(x, y)
        self.image.blit(self.t, (0, 0))
        self.image.blit(self.t2, (0, 30))
        self.image.blit(self.t3, (0, 60))

    def update(self, a=0):
        if a == 0:
            self.change_col()
        if self.rect.y == 450 + self.nom * 150 and a == 10:
            a = 0
        if self.rect.y == -1450 + self.nom * 150 and a == -10:
            a = 0
        self.rect = self.rect.move(0, a)

    def change_col(self):
        c = costs[self.nom * 2]
        s = ''
        while float(c) > 1000:
            c = str(round(float(c) / 1000))
            s += 'k'
        c = str(c) + s
        d = pri[self.nom]
        s = ''
        while float(d) >= 1000:
            d = str(round(float(d) / 1000))
            s += 'k'
        d = str(d) + s
        self.t = self.font.render(names[self.nom] + f'  {c} за штуку', True, (255, 255, 255))
        self.t2 = self.font.render(f'Производит {d} носков в день', True, (255, 255, 255))
        self.t3 = self.font.render(f'У вас {col[self.nom]} штук', True, (255, 255, 255))
        self.image = pygame.Surface([400, 200], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.image.blit(self.t, (0, 0))
        self.image.blit(self.t2, (0, 30))
        self.image.blit(self.t3, (0, 60))


class Information(pygame.sprite.Sprite):
    def __init__(self, val):
        super().__init__(information)
        self.val = val
        self.font = pygame.font.Font('Anonymous_Pro.ttf', 25)
        self.image = pygame.Surface([600, 200], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.coin = pygame.image.load('Icons/Валюта.png')
        self.rect = self.image.get_rect().move(850, 50)

    def money_change(self, m):
        self.val -= m
        a = round(self.val)
        s = ''
        while float(a) > 1000:
            a = str(round(float(a) / 1000, 1))
            s += 'k'
        a = str(a) + s
        b = round(new() * 100)
        s = ''
        while float(b) > 1000:
            b = str(round(float(b) / 1000, 1))
            s += 'k'
        b = str(b) + s
        self.t = self.font.render(f'У вас {a} гришакоинов', True, (255, 255, 255))
        self.t2 = self.font.render(f'{b} носков в день', True, (255, 255, 255))
        self.image = pygame.Surface([600, 200], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect().move(850, 50)
        self.image.blit(self.t, (0, 0))
        self.image.blit(self.t2, (0, 35))
        self.image.blit(self.coin, (len(f'У вас {a} гришакоинов') * 14, 0))

    def money_add(self, m):
        self.val += m
        a = round(self.val)
        s = ''
        while float(a) > 1000:
            a = str(round(float(a) / 1000, 1))
            s += 'k'
        a = str(a) + s
        b = round(new() * 100)
        s = ''
        while float(b) > 1000:
            b = str(round(float(b) / 1000, 1))
            s += 'k'
        b = str(b) + s
        self.t = self.font.render(f'У вас {a} гришакоинов', True, (255, 255, 255))
        self.t2 = self.font.render(f'{b} носков в день', True, (255, 255, 255))
        self.image = pygame.Surface([600, 200], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect().move(850, 50)
        self.image.blit(self.t, (0, 0))
        self.image.blit(self.t2, (0, 35))
        self.image.blit(self.coin, (len(f'У вас {a} гришакоинов') * 14, 0))

    def get_val(self):
        return self.val


class Icon(pygame.sprite.Sprite):
    def __init__(self, n, x, y):
        super().__init__(icons)
        self.nom = n
        self.image = pygame.image.load('Icons/' + names[self.nom] + '.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect().move(x, y)

    def update(self, a=0):
        if self.rect.y == 450 + self.nom * 150 and a == 10:
            a = 0
        if self.rect.y == -1450 + self.nom * 150 and a == -10:
            a = 0
        self.rect = self.rect.move(0, a)


class Animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(foun)
        self.image = pygame.Surface([750, 400], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect().move(0, 0)
        self.particle = pygame.image.load('Icons/Носок.png')
        self.particle = pygame.transform.scale(self.particle, (50, 50))
        self.fall = []
        self.count = 0
        self.dojd()

    def dojd(self):
        if len(self.fall) < 150:
            n = random.randint(1, 5)
            for _ in range(n):
                self.fall.append((random.randint(0, 700), -50))

    def update(self, a=0):
        self.image = pygame.Surface([750, 400], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        for i in range(-len(self.fall), -1):
            self.fall[i] = (self.fall[i][0], self.fall[i][1] + 1)
            if self.fall[i][1] >= 400:
                self.fall.pop(i)
            else:
                self.image.blit(self.particle, (self.fall[i][0], self.fall[i][1]))
        self.count += 1
        if self.count == 10:
            self.dojd()
            self.count = 0


class Closed(pygame.sprite.Sprite):
    def __init__(self, n, x, y):
        super().__init__(closed)
        self.nom = n
        self.image = pygame.image.load('Icons/Закрыто.png')
        self.rect = self.image.get_rect().move(x, y)

    def update(self, a=0):
        if uluch[self.nom - 2] == 1:
            buts[self.nom * 2].work = True
            buts[self.nom * 2 + 1].work = True
            op[self.nom] = 'open'
            self.kill()
        if self.rect.y == 454 + self.nom * 148 and a == 10:
            a = 0
        if self.rect.y == -1446 + self.nom * 148 and a == -10:
            a = 0
        self.rect = self.rect.move(0, a)


def new():
    s = 0
    for i in range(len(col)):
        s += pri[i] * col[i]
    return s / 100


def end_game():
    os.remove('GameData.txt')
    os.remove('Upgrades.txt')
    pygame.quit()
    os.startfile('PygameGameEnd.txt')
    raise SystemExit


pygame.display.set_caption('PygameGame')
Foun()
Shop()
Animation()
UpgradeFon()
SwitchButton(900, 150)
ToMainButton(1100, 550)
money = Information(m)
UpgradeInformation(money)
for i in range(28):
    buts.append(Button(i))
for i in range(len(op)):
    if op[i] == 'closed':
        Closed(i, 0, 454 + i * 148)
        buts[i * 2].work = False
        buts[i * 2 + 1].work = False
for i in range(len(ups)):
    UpgradeIcon(i, 25, 50 + i * 150, ups)
    UpgradeText(i, 175, 50 + i * 150, ups)
    UpgradeBuy(i, 600, 75 + i * 150, money)
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            if sdv == -1:
                for i in range(5):
                    sprite_group.update(a=10)
                    buttons.update(a=10)
                    text_group.update(a=10)
                    icons.update(a=10)
                    closed.update(a=10)
            else:
                for i in range(5):
                    upgrades.update(a=10)
                    upgrade_buttons.update(a=10)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            if sdv == -1:
                for i in range(5):
                    sprite_group.update(a=-10)
                    buttons.update(a=-10)
                    text_group.update(a=-10)
                    icons.update(a=-10)
                    closed.update(a=-10)
            else:
                for i in range(5):
                    upgrades.update(a=-10)
                    upgrade_buttons.update(a=-10)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            buttons.update(pos=event.pos)
            upgrade_buttons.update(pos=event.pos)
    screen.fill((0, 0, 0))
    from PygameGameUpgrades import uluch, pri, sdv
    if uluch[-1] == 1:
        end_game()
    money.money_add(new())
    upgrades.update()
    text_group.update()
    foun.update()
    closed.update()
    if sdv == -1:
        foun.draw(screen)
        sprite_group.draw(screen)
        buttons.draw(screen)
        icons.draw(screen)
        text_group.draw(screen)
        information.draw(screen)
        closed.draw(screen)
    else:
        upgrades.draw(screen)
        upgrade_buttons.draw(screen)
    f = open('GameData.txt', mode='w')
    _ = list(map(lambda x: str(x), col))
    f.write(','.join(_) + '\n')
    f.write(str(money.get_val()) + '\n')
    for i in op:
        f.write(i + '\n')
    f.close()
    fa = open('Upgrades.txt', mode='w')
    for i in range(len(ups)):
        fa.write(ups[i] + '_' + str(uluch[i]) + '\n')
    fa.close()
    if openn:
        os.startfile('PygameGameHelp.txt')
        openn = False
    clock.tick(100)
    pygame.display.flip()
pygame.quit()