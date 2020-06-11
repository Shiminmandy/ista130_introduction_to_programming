# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
import random
import math
def chases(predator, prey_animal):
    # print("the{}chases the{}".format(predator, prey_animal))
    print(f"The {predator} chases the {prey_animal}")

def sum3(var1, var2, var3):
    print(f"The sum of the arguments is: {var1 + var2 + var3}")

def forecast():
    print(f"Chance of rain today: {random.randrange(101)} %")

def radians(degrees):
    """
     The behavior of round() for floats can be surprising.
     Notice round(2.675, 2) gives 2.67
     instead of the expected 2.68. This is not a bug:
    it's a result of the fact that most decimal fractions
    can't be represented exactly as a float.
    """
    print(f"The angle in radians is: {round(degrees * (math. pi) / 180, 3)}")

def decimal(var4):
    print(f"Decimal part: {round(var4 - math.floor(var4), 3)}")

def erf_plus_gamma(var5):
    print(f"Result: {round(math.erf(var5) + math.gamma(var5), 3)}")

def main():
    chases('dragon', 'human')
    chases('coyote', 'roadrunner')
    sum3(1, 2, 3)
    sum3(4, 5, 6)
    forecast()
    forecast()
    radians(200)
    radians(30)
    decimal(5.983)
    decimal(5.9839)
    erf_plus_gamma(0.6)
    erf_plus_gamma(0.22)
if __name__ == '__main__':  # 只会在本文件进行以下方法调用
    main()





