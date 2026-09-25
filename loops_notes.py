# RC, loops notes, CSP 6th
import random
# code that will repeat over and over again
count = 1

while count <= 1:
    print(count)
    count += 1


goose = random.randint(1,11)
ducks = 1

while True:
    print("duck")
    if ducks == goose:
        break
    ducks += 1
print("GOOSE!!!!")


siblings = ["Alex", 'Katie', "andrew", "tia", "trayson", "xavier", "jake"]

print(siblings[2])
print(siblings)
#add to the list
item = input("what needds to be added to the list:")
siblings.append("Jayshree")
siblings.insert(3,item)
#remove from list
print(siblings)
siblings.pop(3)
print(siblings)

#for loops
for number in range(1,50,10):
    print(number)

for sibling in siblings:
    print(sibling + " LaRose")