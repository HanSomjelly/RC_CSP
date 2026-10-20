# REMY C
print("You walk into the room. On a desk is a peice of paper")
print('its a word search!?')
print()
print('the word search says:')
print()
with open("search.txt", "r") as file:

    word_search = file.read()

print(word_search)
print()
