from random import randrange
from time import sleep

from names_list import *
from characters import Character, Npc


class Elf(Character):

    def __init__(self):
        super().__init__()
        self.max_health = 98
        self.health = self.max_health
        self.max_mana = 98
        self.mana = self.max_mana
        self.damage = (12, 17)
        self.crit_damage = 3
        self.crit_chance = 7
        self.speed = 3
        self.hp_regeneration = 2
        self.mp_regeneration = 2

    def wind_slice(self):
        mana_cost = 30
        if self.mana >= mana_cost:

            self.mana -= mana_cost
            first_hit, crit_check = self.attack(1, 5)
            second_hit, crit_check = self.attack(0.5, 0)
            total_damage = first_hit + second_hit
            sleep(1)
            print(f"{self.name} striked twice using Wind Strike.")
            sleep(1)
            print(
                f"First hit dealt {first_hit} and a wave of air cut for {second_hit} damage")
            sleep(1)

            return total_damage
        else:
            print(f"Not enough mana! {self.mana}/{mana_cost}")
            return False

    def __len__(self):
        return len(self.skills)

    def __getitem__(self, skill):
        return self.skills[skill]

    skills = [wind_slice]


class Mage(Character):

    def __init__(self):
        super().__init__()

        self.max_health = 79
        self.health = self.max_health
        self.max_mana = 196
        self.mana = self.max_mana
        self.damage = (10, 13)
        self.crit_damage = 4
        self.crit_chance = 9
        self.speed = 2
        self.hp_regeneration = 1
        self.mp_regeneration = 4

    def set_stats(self):
        return super().set_stats(1, 4)

    def level_up(self):
        return super().level_up(1, 4)


class Goblin(Npc):
    def __init__(self):
        super().__init__()

        self.name = "Goblin " + goblins[randrange(0, len(goblins))]
        self.health = 15
        self.max_health = self.health
        self.mana = 0
        self.damage = 3
        self.crit_chance = 10
        self.crit_damage = 0
        self.speed = 1


class Orc(Npc):
    def __init__(self) -> None:
        super().__init__()

        self.name = orcs[randrange(0, len(orcs))] + " the Orc"
        self.health = 30
        self.max_health = self.health
        self.mana = 0
        self.damage = 8
        self.crit_chance = 9
        self.crit_damage = 5
        self.speed = 1


npc_races = ['Orc()', 'Goblin()']
hero_races = ['Elf', 'Mage']

con = Elf()
