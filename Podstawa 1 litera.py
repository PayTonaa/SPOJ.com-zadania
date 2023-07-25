def are_you_playing_banjo(name):
    name1 = name
    name = name[0]
    if name == "R" or name == "r":
        name = name1 + " plays banjo"
    else:
        name = name1 + " does not play banjo"
    return name

name = input("podaj imie ")
x = are_you_playing_banjo(name)
print(x)
