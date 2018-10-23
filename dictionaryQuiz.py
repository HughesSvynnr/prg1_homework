nicknames = {'name1': "Griffin", 'name2': "Gargano", 'nick1': "Grof", 'nick2': "Gargamel"}
print(nicknames)

more_names = input("Please enter 3 more names with their nicknames > ")
nicknames.append(more_names)

for more_names in nicknames:
    print(nicknames)
