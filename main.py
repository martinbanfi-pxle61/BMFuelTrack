from tkinter import Tk, Label, Entry, Button, Listbox, END, messagebox
from bm_tankolas import BMTankolasManager


root = Tk()
root.title("app")
root.geometry("460x440")

manager = BMTankolasManager()

liter_label = Label(root, text="Tankolt mennyiség (liter):")
liter_label.pack()
liter_entry = Entry(root)
liter_entry.pack()

ar_label = Label(root, text="Ár (Ft/liter):")
ar_label.pack()
ar_entry = Entry(root)
ar_entry.pack()

tav_label = Label(root, text="Megtett távolság (km):")
tav_label.pack()
tav_entry = Entry(root)
tav_entry.pack()

lista = Listbox(root, width=70, height=8)
lista.pack(pady=10)

status_label = Label(root, text="")
status_label.pack()


def bm_hozzaad():
    try:
        liters = float(liter_entry.get().replace(",", "."))
        price = float(ar_entry.get().replace(",", "."))
        distance = float(tav_entry.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Hiba", "Minden mezőbe számot írj.")
        return
    try:
        record = manager.bm_add_record(liters, price, distance)
    except ValueError as e:
        messagebox.showerror("Hiba", str(e))
        return
    consumption = record["consumption"]
    total_cost = record["total_cost"]
    rec_id = record["id"]
    text = f"#{rec_id} | {distance:.0f} km, {liters:.1f} l, {consumption:.1f} l/100km, {total_cost:.0f} Ft"
    lista.insert(END, text)
    status_label.config(text="Tankolás hozzáadva.")


def bm_osszegzes():
    summary_text = manager.format_summary()
    messagebox.showinfo("Összegzés", summary_text)


def bm_torles_mezok():
    liter_entry.delete(0, END)
    ar_entry.delete(0, END)
    tav_entry.delete(0, END)
    status_label.config(text="")


def bm_torles_kivalasztott():
    sel = lista.curselection()
    if not sel:
        messagebox.showerror("Hiba", "Nincs kiválasztott tankolás.")
        return
    index = sel[0]
    success = manager.bm_delete_record(index)
    if success:
        lista.delete(index)
        status_label.config(text="Tankolás törölve.")
    else:
        messagebox.showerror("Hiba", "Nem sikerült törölni.")


hozzaad_button = Button(root, text="Tankolás hozzáadása", command=bm_hozzaad)
hozzaad_button.pack(pady=5)

osszegzes_button = Button(root, text="Összegzés", command=bm_osszegzes)
osszegzes_button.pack(pady=5)

torles_button = Button(root, text="Mezők törlése", command=bm_torles_mezok)
torles_button.pack(pady=5)

torles_kivalasztott_button = Button(root, text="Kiválasztott törlése", command=bm_torles_kivalasztott)
torles_kivalasztott_button.pack(pady=5)

root.mainloop()
