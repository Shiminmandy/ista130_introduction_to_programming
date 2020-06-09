#Shiyu Cheng
#Discuttion rocks_discussion.py
# 1. Set total price = 0
# 2. Set a while loop flag called wanna_quit which initial is False
# 3. start the while loop which judge by wanna_quit
#   3.1 set type question to user with options
#   3.2 set weight question and assign to weight_answer
#   3.3 set unit question and assign to unit_answer
#   3.4 user unit_convert helper function and get the weight (for unify the unit)
#       3.4.1 pass weight_answer and unit_answer
#       3.4.2 return converted weight
#   3.5 count the price by purchasing conditions of different type of rocks
#   3.6 ask if user want to quit and assign the answer to wanna_quit
#   3.7 if wanna quit == True
#       3.7.1 print the final price message
#       3.7.2 return to break the while loop
#   3.8 otherwise set wanna_quit to false to  continue the while loop



def price_of_rocks():
    wanna_quit = False
    price = 0
    while not wanna_quit:
        type = input("What type of rocks that you want? (quartz crystals / garnets / meteorite) ")
        weight_answer = input(f"How much weights of {type}? ")
        unit_answer = input("What unit of weight did you use ? (pound / gram) ")

        weight = unit_convert(float(weight_answer), unit_answer)

        if type == "quartz crystals":
            price += 23 * weight
        elif type == "garnets":
            price += 160 * weight
        elif type == "meteorite":
            price += 15.5 * weight

        wanna_quit = input("Wanna quit? (False / True) ")

        if wanna_quit == "True":
            print(f"The total price is $ {price}, thank you for your shopping.")
            return price
        else:
            print("\nAlright, please continue your shopping....\n")
            wanna_quit = False


def unit_convert(weight, unit):
    if unit == "gram":
        return weight / 453.592
    return weight


def main():
    price_of_rocks()


if __name__ == '__main__':
    main()
