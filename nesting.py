"""number = 0

while number <= 20:
    print(number)
    number += 2


    for number in range(0,21,2):
    print(number)"""


csp = ["Remy","alex", "gabe", "bliss"]
if len(csp) > 0:
    for student in csp:
        print(f"checking in {student}")
else:
    print("there is no one in this class")
    
while True:
    username = input("whats your username: ").strip()
    password = input("whats your password: ").strip()

    if username == "LaRose24" and password == "password":
        print("Welcome to the program!")
        break
    else:
        print("those credentionals were incorrect")