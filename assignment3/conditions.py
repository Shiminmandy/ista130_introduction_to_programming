# -*- coding:utf-8 -*-
# @Description: python assignment3
# @Author: Shimin
# @Copyright
# @Version:0.0.1

def word_length(str, int):
    if len(str) > int:
        print(f"Longer than {int} characters: {str}")
    elif len(str) == int:
        print(f"Exactly {int} characters: {str}")
    else:
        print(f"Shorter than {int} characters: {str}")


def stop_light(current_color, showing_time):
    if showing_time > 60:
        return 'yellow'
    elif showing_time > 55 and showing_time < 60:
        return 'green'
    elif showing_time > 5 and showing_time < 55:
        return 'red'
    else:
        return current_color


def is_normal_blood_pressure(systolic_blood_pressure, diastolic_blood_pressure):
    if systolic_blood_pressure < 120 and diastolic_blood_pressure < 80:
        return True
    else:
        return False


def doctor():
    systolic_blood_pressure = input("Enter your systolic reading:")
    diastolic_blood_pressure = input("Enter your diastolic reading:")
    if systolic_blood_pressure < 120 and diastolic_blood_pressure < 80:
        print("Your blood pressure is normal.")
    else:
        print("Your blood pressure is high.")


def pants_size(size_number):
    if size_number >= 34:
        return 'large'
    elif size_number >= 30 and size_number < 34:
        return 'medium'
    else:
        return 'small'
def main():
    word_length('liversnaps', 7)
    word_length('earwax', 5)
    word_length('chickenfat', 10)
    word_length('Gross!', 13)
    stop_light('green', 61)
    stop_light('yellow', 5)
    stop_light('yellow',6)
    stop_light('red', 12)
    stop_light('red', 56)
    stop_light('red', 54)
    stop_light('green', 59)
    stop_light('green', 60)
    is_normal_blood_pressure(120, 80)
    is_normal_blood_pressure(119, 80)
    is_normal_blood_pressure(119, 79)
    is_normal_blood_pressure(120, 79)
    pants_size(38)

if __name__ == '__main__':
    main()