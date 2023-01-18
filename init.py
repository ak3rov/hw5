from classs import Hero, hero_super

hero1 = hero_super('Luffy', 'gomo gomo fruit')
hero2 = Hero('Chopper', 'hito hito fruit')

print(hero1.get_name())
print(hero1.power())

from turtle import *
color("green")
bgcolor("black")
speed(11)
hideturtle()
b = 0

while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1
