# # OPENING AND READING A FILE METHOD 1
# file = open("my_name.txt")
# contents = file.read()
# print(contents)
# file.close()

# # OPENING AND READING A FILE METHOD 2
# with open("my_name.txt") as file:
#     contents = file.read()
#     print(contents[-1])

# WRITING A FILE
# with open("my_name.txt", mode='a') as file:
#     file.write("\nNew text")


# mail merging
# names = ["Pikachu", "Squirtle", "Charmander", "Bulbasaur", "Charmeleon"]
# with open("./Input/Names/invited_names.txt", 'w') as file:
#     for name in names:
#         file.write(name+"\n")

PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt", 'r') as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", 'r') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", 'w') as completed_letters:
            completed_letters.write(new_letter)