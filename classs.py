import fastapi
import colorama
class Hero:
    human = 'human'
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

class hero_super(Hero):
    human = 'human'

    def __init__(self, name, ability):
        super().__init__(name, ability)
        self.name = name
        self.ability = ability

    def __str__(self):
        return {self.name}

    def get_name(self):
        return f"super_hero's name is: {self.name}"

    def power(self):
        return f'Способность: {self.ability}'

Sup = hero_super('Luffy', 'gomo gomo fruit')

print(Sup.get_name())
print(Sup.power())
