import json
import os

if not os.path.exists("notes.json"):
    with open("notes.json", "w") as f:
        json.dump([], f)


def load_notes():
    try:
        with open("notes.json", "r") as f:
          return json.load(f)
        
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    
    
def save_notes(notes):
    with open("notes.json", "w")as f:
         json.dump(notes, f, indent=4)

def add_note():
    note=input("Enter your note here:")
    notes= load_notes()
    notes.append({"note": note})
    save_notes(notes)
    print("Note added succesfully")


def list_notes():
    notes= load_notes()

    if  not notes:
        print("Notes not found")
    else:
        for i,n in enumerate (notes,1):
            print(f"{i}. {n['note']}")

def search_note():
    keyword=input("Enter a keyword for serach: ")
    notes= load_notes()
    found=False
    for n in notes:
        if keyword.lower() in n["note"].lower():
            print(f"Found {n['note']}")
            found=True
    
    if not found:
        print("No matching note found")

def delete_note():
    notes= load_notes()
    for i,n in enumerate (notes,1):
        print(f"{i}. {n['note']}")
    number=int (input("Enter a index number"))
    if 0<number <= len(notes):
        removed= notes.pop(number-1)
        save_notes(notes)
        print(f" Deleted: {removed['note']}")
    else:
        print(" Invalid index number.")

while True:
    print("\n == Notes Manager ==")
    print("1. Add Notes")
    print("2. List Notes")
    print("3. Search Note")
    print("4. Delete Note")
    print("5. Exit")

    choice = input(" Enter your choice (1-5): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        list_notes()
    elif choice == "3":
        search_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        print(" Exiting Notes Manager... Goodbye!")
        break
    else:
        print(" Invalid choice, please try again.")
    
    
    