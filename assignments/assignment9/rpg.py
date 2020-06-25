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


def combat_round(InstanceFighter1, InstanceFighter2):
    num1 = random.randrange(1, 6)
    num2 = random.randrange(1, 6)
    if num1 == num2:
        print('Simultaneous!')
        InstanceFighter1.attack(InstanceFighter2)
        InstanceFighter2.attack(InstanceFighter1)
    elif num1 > num2:
        InstanceFighter1.attack(InstanceFighter2)
        if InstanceFighter2.is_alive():
            InstanceFighter2.attack(InstanceFighter1)
    else:
        InstanceFighter2.attack(InstanceFighter1)
        if InstanceFighter1.is_alive():
            InstanceFighter1.attack(InstanceFighter2)


def main():
    InstanceFighter1 = Fighter('Death_Mongrel')
    InstanceFighter2 = Fighter('Hurt_then_Pain')
    round_num = 1
    while InstanceFighter2.hit_points > 0 and InstanceFighter1.hit_points > 0:
        print(f'{"=" * 19} ROUND {round_num} {"=" * 19}')
        print(InstanceFighter1)
        print(InstanceFighter2)
        #answer = ''
        #while True:
        #if answer == '':
        input('Enter to Fight! ')
            #break
        # else:
        #     answer = input('Enter to Fight! ')
        combat_round(InstanceFighter1, InstanceFighter2)
        round_num += 1
    print('The battle is over!')
    print(InstanceFighter1)
    print(InstanceFighter2)

if __name__ == '__main__':
    main()