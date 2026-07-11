# Task 1

file = open("notes.txt", "w")
file.write(f""" Hello Uday
           Learning Python
           Learning AI
            """)
file.close()

# Task 2

file = open("notes.txt", "r")
print(file.read())
file.close()

# Task 3

file = open("notes.txt", "a")
file.write("\nFuture AI Engineer")
print(file.read())
file.close()

# Task 4

with open("notes.txt", "r") as file:
    print(file.read())


# Mini Project (Personal Notes Manager V1)

class NotesManager:
    def __init__(self):
        pass

    def add_note(self):
        try:
            text = input("Enter input text to add: ")
            with open("notes.txt", "a") as file:
                file.write(text + "\n")
        except Exception as e:
            print("Exception", e)

    
    def view_notes(self):
        try:
            with open("notes.txt", "r") as file:
                print(file.read())
        except Exception as e:
            print("Exception", e)

    def exit(self):
        return
    

notes_manager = NotesManager()
action = input("Enter the menu from 1, 2, 3")
action_mapping = {
    "1": notes_manager.add_note,
    "2": notes_manager.view_notes,
    "3": notes_manager.exit
}

action_mapping[action]()

while True:

    action = input("Enter the menu from 1, 2, 3")
    if action == "3":
        break
    action_mapping = {
    "1": notes_manager.add_note,
    "2": notes_manager.view_notes,
    "3": notes_manager.exit
    }

    if action in action_mapping:
        action_mapping[action]()
    else:
        print("Invalid Choice")

# while loop ka kha use kru samajh nhi aa rha yha pr.

# Mentor Challenge 1  -- Hello World
# Mentor Challenge 2  -- AI


# w is used for write in file and it is basically replace the content prent in file. but a is used for append any content in the file without loosing any existing data.
# with open() preferred over open() + close() is because with open() is internally closed the file once everything is done and if we do not use this than manually we need to close the file after doing the work.
# Logs maintain krna and CSV create krna thats all are the example.

        