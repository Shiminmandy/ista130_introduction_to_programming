# -*- coding:utf-8 -*-
# @Description
# @Author: Shimin
# @Copyright
# @Version:0.0.1
def chases(predator, prey_animal):
    # print("the{}chases the{}".format(predator, prey_animal))
    print(f"The {predator} chases the {prey_animal}")

def sum3(var1, var2, var3):
    print(f"The sum of the arguments is: {var1 + var2 + var3}")


def main():
    chases('dragon', 'human')
    chases('coyote', 'roadrunner')
    sum3(1, 2, 3)
    sum3(4, 5, 6)
if __name__ == '__main__':  # 只会在本文件进行以下方法调用
    main()





