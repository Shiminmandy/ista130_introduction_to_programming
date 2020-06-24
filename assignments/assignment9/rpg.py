# -*- coding:utf-8 -*-
# @Description: pyhton assignment9
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import random


class Fighter:
    def __init__(self, name):
        self.name = name
        self.hit_points = 10

    def __repr__(self):
        return f'{self.name} (HP: {self.hit_points})'

    def take_damage(self, damage_amount):
        # self.hit_points = self.hit_points - damage_amount
        self.hit_points -= damage_amount
        if self.hit_points <= 0:
            print(f'\tAlas, {self.name} has fallen!')
        else:
            print(f'\t{self.name} has {self.hit_points} hit points remaining.')

    def attack(self, other):
        print(f'{self.name} attacks {other.name}!')
        attack_hits = random.randrange(1, 20)
        if attack_hits >= 12:
            hits = random.randrange(1, 6)
            print(f'\tHits for {hits} hit points!')
            other.take_damage(hits)
        else:
            print('\tMisses!')

    def is_alive(self):
        if self.hit_points > 0:
            return True
        else:
            return False