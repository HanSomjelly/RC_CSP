# RC, Ceaser Cipher, CSP 6th

cipher = input("give me a message to (E)encode or (D)decode")
code = input("TELL ME A MESSAGE")
shift = int(input("tell me how much you"))
def caeser_shift(message, shift):
    new_message = ""
    for letter in message:
        if letter.isalpha():
            number = ord(letter)
            number = number + shift
            if letter.isupper():
                if number > 90:
                    number = number - 26
                if number < 65:
                    number = number + 26
            else:
                if number > 122:
                    number = number - 26
                if number < 97:
                    number = number + 26
            letter = chr(number)
        new_message = new_message + letter
    return new_message
if cipher == "E":
    code = caeser_shift(code, shift)
    print("Your encrypted message is:", code)
else:
    code = caeser_shift(code, -shift)
    print("Your new massage is", code)