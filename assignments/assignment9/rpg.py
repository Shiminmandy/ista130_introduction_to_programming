# -*- coding:utf-8 -*-
# @Description: pyhton assignment9
# @Author: Shimin
# @Copyright
# @Version:0.0.1

class Fighter:
    def __init__(self, name):
        self.name = name
        self.hit_points = 10

    def __repr__(self):
        return f'{self.name} (HP: {self.hit_points})'
