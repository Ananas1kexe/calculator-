from colorama import init
init()
from colorama import Fore, Back, Style

print(Back.YELLOW + Fore.BLACK+ "Добро пожаловать в калькулятор")

while True:
    
    num1 = float(input("Ввидите первое число: "))
    b = input("Выберите знак действия + - * /: ")
    num2 =float(input("Ввидите второе число: "))
    if b == "+":
        print(num1+num2)
        break
    elif b == "-":
        print(num1-num2)
        break  
    elif b == "*":
        print(num1*num2)
        break
    elif b == "/":
        print(num1/num2)
        break
    else:
        print("Я вас не понимаю попробуйте еще раз")
        