def calculator():
    print("ввидите 1 число")
    num_a = int(input(': '))
    print("ввидите 2 число")
    num_b = int(input(': '))
    print("ввыбирите действие(1. + 2. - 3. * 4. /)")
    a = input(": ")
    if a == "+":
        print(num_a + num_b)
    elif a == "-":
        print(num_a - num_b)
    elif a == "*":
        print(num_a * num_b)
    elif a == "/":
        print(num_a / num_b)
    else:
        print("Неизвестная операция ")
calculator()