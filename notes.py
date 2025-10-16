#SMART STUDY ASSISTANT

from datetime import datetime

def addnotes():
    note = input("Enter your note: ").strip()
    if not note:
        print("Empty note not saved.")
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("notes.txt", "a") as f:
            f.write(f"[{timestamp}] {note}\n")
        print("Note saved with timestamp!")
    except IOError:
        print("Error: Could not write to notes.txt")


def viewnotes():
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
        if not notes:
            print("No notes found.")
            return
        print("\nYour Notes")
        for n in notes:
            print("-", n.strip())
    except FileNotFoundError:
        print("notes.txt file not found. Please add a note first.")
    except IOError:
        print("Error: Could not read notes.txt")

def deletenotes():
    notes = viewnotes()
    if not notes:
        return
    try:
        num = int(input("Enter the note number to delete: ").strip())
        if num < 1 or num > len(notes):
            print("Invalid note number.")
            return
        removed_note = notes.pop(num - 1)
        with open("notes.txt", "w") as f:
            f.writelines(notes)
        print(f"Deleted note: {removed_note.strip()}")
    except ValueError:
        print("Please enter a valid number.")
    except IOError:
        print("Error: Could not update notes.txt")

def searchnotes():
    keyword = input("Enter keyword to search: ").strip().lower()
    if not keyword:
        print("Empty keyword, please enter something to search.")
        return
    notes = []
    try:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
    except FileNotFoundError:
        print("notes.txt file not found. Please add a note first.")
        return
    except IOError:
        print("Error: Could not read notes.txt")
        return
    results = [(idx+1, note.strip()) for idx, note in enumerate(notes) if keyword in note.lower()]
    if not results:
        print(f"No notes found containing '{keyword}'.")
    else:
        print(f"\nNotes containing '{keyword}':")
        for num, note in results:
            print(f"{num}. {note}")


def notes_choice():
    print("\t\t\t\t    Menu\n\t\t\t\t1. Add Notes\n\t\t\t\t2. View Notes\n\t\t\t\t3.Search Notes\n\t\t\t\t4.Delete Notes\n\t\t\t\t5.Exit.")
    ch = input("Enter your choice: ").strip()
    match ch:
        case "1":
            addnotes()
        case "2":
            viewnotes()
        case "3":
            searchnotes()
        case "4":
            deletenotes()
        case "5":
                print("Goodbye!")
                break
        case _:
            print("Invalid choice, please enter a number mentioned in the menu")
            
notes_choice()