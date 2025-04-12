persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33),
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]


while True:
    name = input("Enter name (or 'stop' for exit)")
    if name.lower() == "stop":
        break
    found_names = [person for person in persons if person[0] == name]

    if not found_names:
        print("There is no name in the list")
        continue
    else:
        surname = input("Please enter surname: ")
        found_person = [person for person in persons if person[1] == surname]
        if found_person:
            print(f"{name} {surname} is years old: {found_person[0][2]}")
        else:
            print("There is no surname in the list")
