print("=====TABUADA=====")
while True:
    try:
        num = int(input("Digite um número: "))
        if not num:
            print("Digite um número maior que ZERO (0)\n")
            continue       
        for i in range(1,11):
            res = num * i
            print(f"{num} X {i} = {res}")
        break
    except ValueError:
        print("Utilize somente números\n")
        continue
