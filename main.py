import tkinter as tk
from tkinter import ttk

# Szkielet
root = tk.Tk()
root.title('Kalkulator')
root.geometry('300x200+50+50')
root. resizable(False, False)
wynik = tk.StringVar(value="0")
# Funkcje
def klik(znak):
    aktualny = wynik.get()
    if aktualny == "0":
        wynik.set(znak)
    else:
        wynik.set(aktualny + znak)

def oblicz():
    try: 
        dzialanie = wynik.get()
        koncowy_wynik = eval(dzialanie)
        wynik.set(str(koncowy_wynik))
    except:
        wynik.set("Błąd")
def czysc():
    wynik.set("0")
def usun():
    aktualny = wynik.get()
    nowy_tekst = aktualny[:-1]
    if nowy_tekst == "":
        wynik.set("0")
    else:
        wynik.set(nowy_tekst)

# GUI
przywitanie = tk.Label(root, text="Kalkulator")
przywitanie.pack(side=tk.TOP, fill=tk.X)
ramka_wyniku = tk.Frame(root, bg="grey", highlightbackground="black", highlightthickness="2")
ramka_wyniku.pack(side=tk.TOP, fill=tk.X)
tekst_wyniku = tk.Label(ramka_wyniku, textvariable=wynik, bg="grey")
tekst_wyniku.pack()

rzad1 = tk.Frame(root)
rzad1.pack(side = tk.TOP, fill=tk.X, pady=0)

clear = tk.Button(rzad1, text="CL", padx=0, bg="lightgrey", command=czysc)
clear.pack(side=tk.LEFT, expand=True, fill=tk.X)
delete = tk.Button(rzad1, text="<-", padx=0, bg="lightgrey", command=usun)
delete.pack(side=tk.LEFT, expand=True, fill=tk.X)


rzad2 = tk.Frame(root)
rzad2.pack(side = tk.TOP, fill=tk.X, padx=0)

p7 = tk.Button(rzad2, text="7", command=lambda: klik("7"))
p7.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
p8 = tk.Button(rzad2, text="8", command=lambda: klik("8"))
p8.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
p9 = tk.Button(rzad2, text="9", command=lambda: klik("9"))
p9.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
pdiv = tk.Button(rzad2, text="/", bg="lightgrey", command=lambda: klik("/"))
pdiv.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)


rzad3 = tk.Frame(root)
rzad3.pack(side = tk.TOP, fill=tk.X, padx=0)

p4 = tk.Button(rzad3, text="4", command=lambda: klik("4"))
p4.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
p5 = tk.Button(rzad3, text="5", command=lambda: klik("5"))
p5.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
p6 = tk.Button(rzad3, text="6", command=lambda: klik("6"))
p6.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
pmul = tk.Button(rzad3, text="*", bg="lightgrey", command=lambda: klik("*"))
pmul.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)


rzad4 = tk.Frame(root)
rzad4.pack(side = tk.TOP, fill=tk.X, padx=0)

p3 = tk.Button(rzad4, text="1", command=lambda: klik("1"))
p3.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
p2 = tk.Button(rzad4, text="2", command=lambda: klik("2"))
p2.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
p1 = tk.Button(rzad4, text="3", command=lambda: klik("3"))
p1.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
pode = tk.Button(rzad4, text="-", bg="lightgrey", command=lambda: klik("-"))
pode.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)

rzad5 = tk.Frame(root)
rzad5.pack(side = tk.TOP, fill=tk.X, padx=0)


n = tk.Button(rzad5, text=" , ", bg="lightgrey", command=lambda: klik("."))
n.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
p0 = tk.Button(rzad5, text="0 ", command=lambda: klik("0"))
p0.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
pprz = tk.Button(rzad5, text="= ", bg="lightblue", command=oblicz)
pprz.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)
pdod = tk.Button(rzad5, text="+", bg="lightgrey",  command=lambda: klik("+"))
pdod.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=0)

root.mainloop()