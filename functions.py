#RC, Functions Notes, CSP 6th

#round()
#len()
#print()
def stupid_proof(money):
    while True:
        try:
            temp = float(input(f"what is your monthly {money}:"))
            return temp
        except:
            print("that is not a number :(")

income = stupid_proof("income")
rent = stupid_proof("rent")
income = stupid_proof("income")
transportation = stupid_proof("income")
groceries = stupid_proof("groceries")
save = round(income*.1, 2)

income = float(input("what is your monthly income: "))
rent = float(input("what is your monthly rent: "))
utilities = float(input("what is your monthly utilities: "))
transportation = float(input("what is your transportation : "))
groceries = float(input("what is your monthly groceries: "))
save = 20
# functions go second
def calc_percent(bill, income):
    return round(bill/income * 100)

print(f" your rent is ${rent} wich is {calc_percent(rent, income)}% of your income")
print(f" your utilities is ${utilities} wich is {calc_percent(utilities, income)}% of your income")
print(f" your transportation is ${transportation} wich is {calc_percent(transportation, income)}% of your income")
print(f" your groceries is ${groceries} wich is {calc_percent(groceries, income)}% of your income")
print(f"you should save is ${round(income*.1, 2)} which is 10 percent of your income")
print(f"that means you have {income-rent-utilities-transportation-groceries} left to spend")

