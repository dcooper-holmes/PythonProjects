
with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_content = starting_letter.read()

for name in names:
    new_letter_content = letter_content.replace("[name]", name.strip())

    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", "x") as new_letter:
        new_letter.write(new_letter_content)