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


def pants_fitter():
    name = input("Enter your name:")
    print(f"Greetings {name} welcome to Pants-R-Us")
    waist_size = input("Enter your waist size in inches:")
    num_pants = input("How many pairs of pants would you like:")
    regular_or_fancy = input("Would you like regular or fancy pants?")
    if regular_or_fancy == 'fancy':
        cost = 100 * num_pants
    else:
        cost = 40 * num_pants
    print(f"{num_pants} pairs of {pants_size(waist_size)} {regular_or_fancy} pants: $ {cost}")


def digdug(int7):
    for i in range(1, int7+1):
        if i % 3 == 0 and i % 15 != 0:
            print(f"{i} : dig")
        elif i % 5 == 0 and i % 15 != 0:
            print(f"{i} : dug")
        elif i % 15 == 0:
            print(f"{i} : digdug")
            i += 1


def beef_type(percent_lean):
    if percent_lean < 78:
        return "Hamburger"
    elif percent_lean >= 78 and percent_lean < 85:
        return "Chuck"
    elif percent_lean >= 85 and percent_lean < 90:
        return "Round"
    elif percent_lean >= 90 and percent_lean <= 95:
        return "Sirloin"
    else:
        return "Unknown"


def species_height(H_or_K, height):
    if H_or_K == "Human" and height > 67:
        print("Above Average")
    elif H_or_K == "Human" and height < 67:
        print("Below Average")
    elif H_or_K == "Klingon" and height > 71:
        print("Above Average")
    elif H_or_K == "Klingon" and height < 71:
        print("Below Average")
    elif (H_or_K == "Klingon" and height == 71):
        print("Average")
    elif (H_or_K == "Human" and height == 67):
        print("Average")


def sooner_date(var1, var2, var3, var4):
    if var1 > var3:
        print(f"{var3} / {var4}")
    elif var1 < var3:
        print(f"{var1} / {var2}")
    elif var1 == var3 and var2 > var4:
        print(f"{var3} / {var4}")
    elif var1 == var3 and var2 < var4:
        print(f"{var1} / {var2}")
    elif var1 == var3 and var2 == var4:
        print(f"{var1} / {var2}")

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
    digdug(5)
    digdug(2)
    digdug(3)
    digdug(5)
    digdug(15)
    beef_type(91.2)
    beef_type(78)
    beef_type(87)
    beef_type(95.1)
    sooner_date(1, 1, 1, 2)
    sooner_date(2, 5, 1, 3)
    sooner_date(8, 25, 7, 30)
if __name__ == '__main__':
    main()