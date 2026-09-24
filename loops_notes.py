# RC, loops notes, CSP 6th
import random
# code that will repeat over and over again
count = 1

while count <= 1:
    print(count)
    count += 1


goose = random.randint(1,100000)
ducks = 1

while True:
    print("duck")
    if ducks == goose:
        break
    ducks += 1
print("GOOSE!!!!")



siblings = ["Alex", 'Katie', "andrew", "tia", "trayson", "xavier", "jake"]