friendships = {}

while True:
    command = input("Enter friendship (e.g., Salome - Keti) or FINISH: ")
    #ციკლის შეწყვეტა
    if command.strip().upper() == "FINISH":
        break
#რადგან ორნაირი ტირე არსებობს, ორივე გავითვალისწინო
    if " – " in command:
        separator = " – "
    elif " - " in command:
        separator = " - "
    else:
        print("Please write in this format 'Person_1 - Person_2' or 'Person_1 – Person_2'")
        continue


    person_1, person_2 = map(str.strip, command.split(separator))

    #ყველას მეგობარი რომ დაიწეროს
    friendships.setdefault(person_1, set()).add(person_2)
    friendships.setdefault(person_2, set()).add(person_1)


print("\nFriends:")
for person, friends in friendships.items():
    print(f"{person} – {', '.join(sorted(friends))}")