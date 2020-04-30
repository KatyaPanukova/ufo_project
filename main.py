from ufo import *
import turtle as tr
#tr.tracer(0)
#tr.hideturtle()

ufo1 = Ufo('Пришелец - 1', 300, 200, 150, 'pink', 8, 6)
# ufo1.pillars_down = True
ufo1.set_name('Пришелец - 3')
print(ufo1.get_name())     # обращаемся через set и get ,чтобы у пользователя был доступ к конкретному эл-ту
# ufo1.engine_grade = ''
print(ufo1.engine_grade)
ufo1.show()   # изображает тарелку
tr.done()
# setter-присваевание  /getter-возвращение : методы которые определяют что происходит
# в момент присваивания / возвращния
#ufo1.set_made_in('China')
# если это св-во, то к нему можно обращаться. Это правильно. В отличае от атрбутов***
#print(ufo1.get_name())
# прописать метод moive смена координат
# написать метод который убирет летающую тарелку (удалять/закрашивать)