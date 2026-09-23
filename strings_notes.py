# RC, Strings Notes, CSP, 6th
Last_name = 'LaRose'
first_name = "Vienna"
# concatination => to add two strings together
name = first_name +" "+ Last_name
# escape char lets the program ignore the next charechter in the string
print(f'{name} told the class "you can\'t drive my car."')

user = input("please tell me youre name:\n").strip().title()

print(f"new user recognized\nWelcome {user}")

sentance = "The quick brown fox jumped over the lazy dog"

print(f"the sentance is {len(sentance)} charechters long.")
print(sentance)
print(sentance.replace("dog", name))
