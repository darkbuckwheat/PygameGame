import pygame


sprite_group = pygame.sprite.Group()
buttons = pygame.sprite.Group()
text_group = pygame.sprite.Group()
information = pygame.sprite.Group()
icons = pygame.sprite.Group()
value_buttons = pygame.sprite.Group()
upgrades = pygame.sprite.Group()
upgrade_buttons = pygame.sprite.Group()
foun = pygame.sprite.Group()
closed = pygame.sprite.Group()

names = ['Рабочий', 'Станок', 'Мастерская', 'Завод', 'Комбинат', 'Компания', 'Корпорация',
         'Банановая республика', 'Континент', 'Планета', 'Система планет',
         'Рукав галактики', 'Галактика', 'Скопление галактик']
costs = [5, 50, 25, 250, 125, 1250, 500, 5000, 5000, 50000, 50000, 500000, 500000, 5000000,
         5000000, 50000000, 50000000, 500000000, 500000000, 5000000000, 5000000000, 50000000000, 50000000000,
         500000000000, 500000000000, 5000000000000, 5000000000000, 50000000000000]
pri = [1, 5, 25, 100, 1000, 10000, 100000, 1000000, 10000000,
       100000000, 1000000000, 10000000000, 100000000000, 1000000000000]
upcosts = [1250, 5000, 50000, 500000, 5000000, 50000000,
           500000000, 5000000000, 50000000000, 500000000000, 5000000000000, 50000000000000,
           500, 2500, 12500, 50000, 500000, 5000000, 50000000, 500000000, 5000000000,
           50000000000, 500000000000, 5000000000000, 50000000000000, 500000000000000,
           10 ** 17]
texts = []
buts = []
ic = []
sdv = -1


try:
    fa = open('Upgrades.txt', mode='r')
    ups = list(map(lambda x: x[:-1], fa.readlines()))
    uluch = list(map(lambda x: int(x.split('_')[1]), ups))
    ups = list(map(lambda x: x.split('_')[0], ups))
except Exception:
    fa = open('GameData.txt', mode='w')
    ups = ['Открыть мастерская', 'Открыть завод', 'Открыть комбинат', 'Открыть компания', 'Открыть корпорация',
          'Открыть банановая республика', 'Открыть континент', 'Открыть планета', 'Открыть система планет',
          'Открыть рукав галактики', 'Открыть галактика', 'Открыть скопление галактик', 'Курс повышения квалификации',
          'Качественные детали', 'Посменная работа', 'Улучшенная планировка', 'Найм специалистов', 'Ребрендинг',
          'Улучшенная логистика', 'Специальные льготы', 'Уменьшение пошлин', 'Глобализация', 'Улучшенные ракеты',
          'Перевозки через кротовые норы', 'Сверхсветовые двигатели', '"Звёздные врата"', 'Конец игры']
    uluch = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in ups:
        fa.write(i + '_0\n')
fa.close()

for i in range(len(pri)):
    if uluch[i + 12] == 1:
        pri[i] *= 2


class UpgradeFon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(upgrades)
        test = pygame.image.load('Icons/Магазин.png')
        test = pygame.transform.scale(test, (1300, 2150))
        test = test.convert_alpha()
        self.image = test
        self.rect = self.image.get_rect().move(0, 0)

    def update(self, a=0):
        if self.rect.y == 0 and a == 10:
            a = 0
        if self.rect.y == -950 and a == -10:
            a = 0
        self.rect = self.rect.move(0, a)


class UpgradeIcon(pygame.sprite.Sprite):
    def __init__(self, n, x, y, data):
        super().__init__(upgrades)
        self.nom = n
        self.yes = False
        self.strel = pygame.image.load('Icons/Стрелка.png')
        if data[n].split()[0] == 'Открыть':
            name = names[names.index((' '.join(data[n].split()[1:])).capitalize())]
        elif data[n] == 'Конец игры':
            name = 'Рабочий'
        else:
            self.yes = True
            name = names[self.nom - 12]
        self.image = pygame.Surface([120, 120], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect().move(750, 0)
        self.ic = pygame.image.load('Icons/' + name + '.png')
        self.ic = pygame.transform.scale(self.ic, (100, 100))
        self.rect = self.image.get_rect().move(x, y)
        self.image.blit(self.ic, (0, 0))
        if self.yes:
            self.image.blit(self.strel, (80, 60))

    def update(self, a=0):
        if self.rect.y == 50 + self.nom * 150 and a == 10:
            a = 0
        if self.rect.y == -3450 + self.nom * 150 and a == -10:
            a = 0
        self.rect = self.rect.move(0, a)


class UpgradeText(pygame.sprite.Sprite):
    def __init__(self, n, x, y, data):
        super().__init__(upgrades)
        self.font = pygame.font.Font('Anonymous_Pro.ttf', 22)
        self.coin = pygame.image.load('Icons/Валюта.png')
        self.nom = n
        g = upcosts[self.nom]
        s = ''
        while float(g) > 1000:
            g = str(round(float(g) / 1000, 2))
            while (g[-1] == '0' or g[-1] == '.') and '.' in g:
                g = g[:-1]
            s += 'k'
        g = str(g) + s
        self.t = self.font.render(data[self.nom], True, (255, 255, 255))
        if self.nom < 12:
            self.t2 = self.font.render('Открывает новую производственную', True, (255, 255, 255))
            self.t3 = self.font.render(f'единицу - {names[self.nom + 2]}', True, (255, 255, 255))
        elif self.nom < 25:
            self.t2 = self.font.render('Увеличивает производительность', True, (255, 255, 255))
            self.t3 = self.t3 = self.font.render(f'{names[self.nom - 12]} на 100%', True, (255, 255, 255))
        else:
            self.t2 = self.font.render('Заканчивает игру', True, (255, 255, 255))
            self.t3 = self.font.render('', True, (255, 255, 255))
        self.t4 = self.font.render(f'Стоимость: {g}', True, (255, 255, 255))
        self.image = pygame.Surface([500, 200], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect().move(x, y)
        self.image.blit(self.t, (0, 0))
        self.image.blit(self.t2, (0, 25))
        self.image.blit(self.t3, (0, 50))
        self.image.blit(self.t4, (0, 75))
        self.image.blit(self.coin, (len(f'Стоимость: {g}') * 12 + 5, 70))

    def update(self, a=0):
        if self.rect.y == 50 + self.nom * 150 and a == 10:
            a = 0
        if self.rect.y == -3450 + self.nom * 150 and a == -10:
            a = 0
        self.rect = self.rect.move(0, a)


class UpgradeInformation(pygame.sprite.Sprite):
    def __init__(self, money):
        super().__init__(upgrades)
        self.font = pygame.font.Font('Anonymous_Pro.ttf', 25)
        self.image = pygame.Surface([600, 200], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect().move(850, 50)
        self.coin = pygame.image.load('Icons/Валюта.png')
        self.money = money

    def update(self, a=0):
        m = round(self.money.get_val())
        s = ''
        while float(m) > 1000:
            m = str(round(float(m) / 1000, 1))
            s += 'k'
        m = str(m) + s
        self.t = self.font.render(f'У вас {m} гришакоинов', True, (255, 255, 255))
        self.image = pygame.Surface([600, 200], pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()
        self.image.blit(self.t, (0, 0))
        self.image.blit(self.coin, (len(f'У вас {m} гришакоинов') * 14, 0))


class UpgradeBuy(pygame.sprite.Sprite):
    def __init__(self, n, x, y, money):
        super().__init__(upgrade_buttons)
        self.nom = n
        self.money = money
        self.yes = True
        if uluch[n] == 0:
            self.image = pygame.image.load('Icons/Купить.png')
        else:
            self.image = pygame.image.load('Icons/Куплено.png')
        self.rect = self.image.get_rect().move(x, y)

    def update(self, a=0, pos=None):
        if pos is not None:
            self.check_click(pos)
        if self.rect.y == 75 + self.nom * 150 and a == 10:
            a = 0
        if self.rect.y == -3425 + self.nom * 150 and a == -10:
            a = 0
        self.rect = self.rect.move(0, a)

    def check_click(self, pos):
        if sdv == 1 and self.rect.x <= pos[0] <= self.rect.x + 150 and self.rect.y <= pos[1] <= self.rect.y + 50:
            if upcosts[self.nom] <= self.money.get_val() and self.yes:
                self.image = pygame.image.load('Icons/Куплено.png')
                self.money.money_change(upcosts[self.nom])
                self.yes = False
                uluch[self.nom] = 1
                if 11 < self.nom < 26:
                    pri[self.nom - 12] *= 2


class ToMainButton(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(upgrade_buttons)
        self.image = pygame.image.load('Icons/Назад.png')
        self.rect = self.image.get_rect().move(x, y)

    def update(self, a=0, pos=None):
        if pos is not None:
            self.check_click(pos)

    def check_click(self, pos):
        global sdv
        if self.rect.x <= pos[0] <= self.rect.x + 150 and self.rect.y <= pos[1] <= self.rect.y + 50:
            sdv *= -1


class SwitchButton(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(buttons)
        self.image = pygame.image.load('Icons/Улучшения.png')
        self.rect = self.image.get_rect().move(x, y)

    def update(self, a=0, pos=None):
        if pos is not None:
            self.check_click(pos)

    def check_click(self, pos):
        global sdv
        if self.rect.x <= pos[0] <= self.rect.x + 150 and self.rect.y <= pos[1] <= self.rect.y + 50:
            sdv *= -1
