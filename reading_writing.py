# RC, Reading And Writing to file Notes, CSP 6th

with open('practice.txt',"r") as file:
    content = file.read()
    print(content)
    word = content.find("LaRose")
    lengh = len("LaRose")
    content += "trayson!"
    file.write(content)

with open('practice.txt',"a") as file:
        file.write("hello")  