import termcolor2
import pyfiglet

while True:
    try:
        fishWeight = int(input(termcolor2.colored("Hi, how much fish did you catch?: ", color = "green")))
    except:
            print("That is not a number")
    else:
        break

total_price = 0


print("------------------------------------")


if fishWeight < 40:
    total_price += fishWeight 
    print("we pay you:")
    print(pyfiglet.figlet_format(str(total_price) + ' $'))
elif fishWeight >= 40 and fishWeight < 80:
    total_price += fishWeight * 2
    print("we pay you:")
    print(pyfiglet.figlet_format(str(total_price) + ' $'))
elif fishWeight >= 80 and fishWeight < 120:
    total_price += fishWeight * 3
    print("we pay you:")
    print(pyfiglet.figlet_format(str(total_price) + ' $'))
elif fishWeight >= 120 and fishWeight < 500:
    total_price += fishWeight * 4
    print("we pay you:")
    print(pyfiglet.figlet_format(str(total_price) + ' $'))
elif fishWeight >= 500:
  print(termcolor2.colored("We dont accept that much fish", color = "red"))

    
