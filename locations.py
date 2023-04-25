locations = { "Grote Kerk" : ["Bordjes", "De zonnewijzer"],
              "Oude Markt" : ["Fontein", "Horeca", "Gekke kromme man"],
               "Volkspark" : ["Standbeelden", "Restaurant", "Vijver"],
               "Cafe Friends" : ["Games/Activeiten", "Locatie eromheen", "Radje met shots"],
               "Rijksmuseum Twenthe" : ["Grote steen", "Vraag informatie aan medewerker", "Kunstvorm binnen het museum"]}

index = 1
for location in locations:
    while True:
        print(f"Location {index}")
        print(f"Please go to {location}")
        print(f"And look out for these aspects:")
        for aspect in locations[location]:
            print(f"  - {aspect}")
        while True:
            try:
                is_finished = input("Did you finish this location? [yes/no]")
                if is_finished != "yes" and is_finished != "no":
                    raise ValueError()
                break
            except ValueError:
                print(f"Incorrect input")
        if is_finished == 'yes':
            break
    index += 1

while True:
    try:
        start_quiz = input("Are you ready to do the quiz? [yes]")
        if start_quiz != 'yes':
            raise ValueError()
        break
    except ValueError:
        print("Incorrect input")