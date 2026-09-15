# RC, Fixing Inputs
while True:
    color = input("Tell me a color that is only 1 word: ").lower().strip()
    ()
    if color.isnumeric():
        print("sorry that is a number")
        elif " " in color:

print("I said one word")
    



print(f"I painted your walls {color}!")








# When you want a number
while True:
    try:
        age = int(input("How old are you: "))
        break
    except:
        print("that isnt a number")
        

print(f"Wow you are {age} that is reaally old!")
