# Szam tippelos alkalmazas > Binaris kereses
print("Gondolj egy számra 1 és 10 között")
min_interval = 1
max_interval = 10
answer = "x"
while answer != "e":
    guess = (min_interval + max_interval)//2
    answer = input("A következő számra tippelek: " + str(guess) + " Ez a helyes szám?")
    if answer == 'k':
        max_interval = guess-1
    elif answer == 'n':
        min_interval = guess+1
print("A gondolt szám", guess)
