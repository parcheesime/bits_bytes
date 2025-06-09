import tkinter as tk

notes = []


def add_note():
    note = entry.get()
    if note:
        notes.append(note)
        listbox.insert(tk.END, note)
        entry.delete(0, tk.END)


def clear_notes():
    notes.clear()
    listbox.delete(0, tk.END)


window = tk.Tk()
window.title("Notepad List")
window.geometry("400x300")

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

add_button = tk.Button(window, text="Add Note", command=add_note)
add_button.pack()

listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

clear_button = tk.Button(window, text="Clear All", command=clear_notes)
clear_button.pack(pady=5)

window.mainloop()
