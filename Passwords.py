# Rc, Passwords Homework, CSP 6th
password = input('choose a password.') 

if len(password) < 8:
 length = True

for letter in password:
 if letter.islower():
  lower = True

if length is True:
print()