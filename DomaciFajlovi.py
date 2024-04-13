import os
import tkinter as tk
from tkinter import simpledialog, filedialog

def kreiraj_foldere(sifra_predmeta, broj_foldera, pocetni_broj):
    # Prikaži dijalog za odabir direktorijuma
    root = tk.Tk()
    root.withdraw()  # Sakrij glavni prozor
    direktorijum = filedialog.askdirectory(title="Izaberite direktorijum za kreiranje foldera")

    # Kreiraj foldere
    for i in range(pocetni_broj, pocetni_broj + broj_foldera):
        ime_foldera = f"{sifra_predmeta}_DZ{i}_Darko.Pajevic.5384"
        putanja_foldera = os.path.join(direktorijum, ime_foldera)
        try:
            os.makedirs(putanja_foldera)
            print(f"Folder '{ime_foldera}' uspešno kreiran.")
        except OSError as e:
            print(f"Neuspelo kreiranje foldera '{ime_foldera}': {e}")

def main():
    # Prikaži UI popup za unos podataka
    root = tk.Tk()
    root.withdraw()  # Sakrij glavni prozor

    sifra_predmeta = simpledialog.askstring("Unos podataka", "Unesite Sifru predmeta: ")
    broj_foldera = simpledialog.askinteger("Unos podataka", "Unesite broj potrebnih foldera: ")
    pocetni_broj = simpledialog.askinteger("Unos podataka", "Unesite redni broj od kojeg početi kreiranje foldera: ")

    if sifra_predmeta is not None and broj_foldera is not None and pocetni_broj is not None:
        kreiraj_foldere(sifra_predmeta, broj_foldera, pocetni_broj)

if __name__ == "__main__":
    main()
