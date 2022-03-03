# Függvény ami paraméterül kap egy listát és kiírja a console-ra a konzolra a listában szereplő számok összegét
numbers = [1, 2, 10, 15, 3]
def sum_list(param):
    sum = 0
    for i in param:
        sum += i
    print(sum)


sum_list(numbers)
