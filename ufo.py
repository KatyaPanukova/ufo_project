import turtle as t
import math

# Интерфес класса -  то,как могу взаимодействовать с классом.
# Описать класс вещей
# Метод - действие, которое мы описываем
# Атрибут - свойство
# Магические методы это : __ __ вот эти подчеркивания, ими мы переопределяем.

# Свойства внешне очень похожи на атрибуты. (made_in = 'Russia')Свойства всегда определяются __ подчеркиванием!!!
# Это св-во, тк когда пишем set ,get  мы используем декоратор - @property(функция, у которой параметр функция)
# Он позовляет в каждую функцию, добавить новые возможности.


class Ufo:
    # Инициализируем нашу вещь; метод инициализации; создание экземпляра класса
    def __init__(self, name, x, y, size, color, count_pillars, count_lamps,pillors_down=True, show_name=True,
                 made_in='Russia',engine_grade='Turbo UFO'):
        # Атрибуты(свойства) нашего объекта     # self.#атрибут = #атрибут
        self._name = name    # если _name то атрибут внутренний, но доступ есть, он не добавляется в интерфейс
        self.x = x           # если __name то более сильная защита от пользователя, доступ есть только внутри класса!
        self.y = y           # также можно защищать методы, __ .По стандарту используют _ .
        self.size = size
        self.color = color
        self.count_pillars = count_pillars
        self.count_lamps = count_lamps
        self.pillars_down = pillors_down     # говорит о состоянии   # не нарисует ноги ,если False
        self.show_name = show_name
        self.__maid_in = made_in  # тут это атрибут       # свойство!!
        self.__engine_grade = engine_grade


    @property
    def engine_grade(self):
        if self.__engine_grade == 'Turbo UFO':
            return 'standart'
        return self.__engine_grade
    @engine_grade.setter     # для того чтобы в main можно было обратиться так ufo1.engine_grade                     #
    def engine_grade(self, new_grade):
        if new_grade == '':
            print('Марка не может быть пустой!')
        else:
            self.__engine_grade = new_grade


    @property # после этого made_in это теперь свойство; превращает метод в метод по работе с свойством.
    # Теперь эта функция свойство.
# Декораторы. @staticmethod : тогда нету ссылки на экземпляр класса.
# Декоратор приписывается к функции ,которую необходимо доработать(задекорировать).
#
    def set_made_in(self, made_in):
        countries = ['USA', 'Russia']
        if made_in in countries:
            self.__maid_in = made_in
        else:
            self.__maid_in = None
    # Если мы хотим изменить имя, то мы хотим сделать метод, который может менять это имя.
    @property
    def get_made_in(self, made_in):
        return self.__maid_in

    def set_name(self, name):             # создали функцию, чтобы обратиться из вне
        self.__name = name

    def get_name(self):             # позволяет это имя получить
        return self.__name

    # метод str - если нужно распечатать; методы строкового вывода
    def __str__(self):
        s = 'Сконструировано НЛО'
        if self.show_name:
            s += ' под названием {name}\n'.format(name=self.name)
        else:
            s += ' с неизвестным названием\n'
        s += 'Координаты НЛО: ({x}; {y})\n'.format(x=self.x, y=self.y)
        s += 'Размер: {size}\n'.format(size=self.size)
        s += 'Размер: {size}\n'.format(size=self.size)
        if self.pillars_down:
            s += 'Опроы опущены\n'
        else:
            s += 'Опроы подняты\n'
        s += 'Количество опор: {count}'.format(count=self.count_pillars)
        s += 'Количество фонарей: {count}'.format(count=self.count_lamps)
        return s


    def __repr__(self):
        return self.__str__()

    def show(self):
        t.ht()
        if self.pillars_down:
            for i in range(self.count_pillars):              # Рисуем опоры
                lx = self.x - self.size / 2 + i * (self.size / (self.count_pillars - 1))
                t.penup()
                t.goto(self.x, self.y + self.size/3)
                t.pendown()
                t.goto(lx, self.y - self.size/6)

        t.penup()
        t.goto(self.x, self.y - self.size / 12)
        t.pendown()
        t.fillcolor('black')
        t.begin_fill()
        t.circle(self.size / 4)
        t.end_fill()

        t.penup()
        t.fillcolor(self.color)
        t.goto(self.x - self.size / 2, self.y + self.size / 4)
        t.pendown()
        t.begin_fill()
        t.fd(self.size)
        i = math.pi / 2
        while i <= 3 * math.pi / 2:
            sx = (self.size / 2) * math.sin(i)
            sy = (self.size / 3) * math.cos(i)
            t.goto(self.x + sx, self.y + self.size/4 + sy)
            i += math.pi / self.size
        t.end_fill()

        t.fillcolor('red')
        n = self.count_lamps + 2
        for i in range(1, n - 1):
            dx = self.size / (n - 1)
            t.begin_fill()
            t.penup()
            t.goto(self.x -self.size / 2 + i * dx, self.y + self.size / 14)
            t.pendown()
            t.circle(dx/4)
            t.end_fill()

        t.penup()
        if self.show_name:
            t.goto(self.x, self.y + self.size / 2)
            t.pendown()
            t.write(self.name, align='center')
            t.penup()
        t.goto(0, 0)
        t.st()