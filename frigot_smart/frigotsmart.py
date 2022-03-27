import datetime
from tkinter import *
import mysql.connector
from functools import partial


def voiraliment():
    #connection de la base de données pour voir les aliments

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="dylaniron",
        database="aliments")

    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM aliment")
    de = mycursor.fetchall()

    voir = Toplevel()

    voir.title("Les aliments")
    voir.resizable(False, False)
    voir.geometry("600x600")
    #pour l'image de fond
    bg1 = PhotoImage(file="bonaliment.ppm")
    im = Label(voir, image=bg1)
    im.place(x=0, y=0, relheight=1, relwidth=1)
    #les variables de type char pour ajouter les aliments
    ar = Text(voir, bg="yellow")
    ad = Text(voir)
    peri = Text(voir,bg="white", fg="red")
    perimer = Text(voir, bg="white", fg="black")

    #pour afficher le logo
    voir.iconphoto(False, PhotoImage(file="frigotlogo.png"))

    for x in de:

        #pour les aliments
        ar.insert(END, x[1]+'\n')
        ar.place(x=100, y=50, width=100, height=500)
        #pour les dates
        ad.insert(END, x[2]+'\n')
        ad.place(x=200, y=50, width=100, height=500)
        #pour la date de l'aliment périmer

    now = datetime.datetime.now()
    day = now.strftime("%d")
    mouth = now.strftime("%m")
    years = now.strftime("%Y")


    ldat = f"{day}/{mouth}/{years}"

    db1 = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="dylaniron",
        database="aliments")

    mycursor1 = db1.cursor()
    mycursor1.execute(f"SELECT *  FROM aliment WHERE date = ('{ldat}')")



    for y in mycursor1:

        perimer.insert(END, "les aliments ci-dessous seront supprimé:" + '\n')
        perimer.place(x=240, y=20, width=320, height=20)
        peri.insert(END, y[1] + '\n')
        peri.place(x=350, y=55, width=100, height=100)

        if len(y[1]) > 10:
            perimer.place(x=240, y=20, width=320, height=20)
            peri.insert(END, y[1] + '\n')
            peri.place(x=350, y=55, width=200, height=100)


        db2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="dylaniron",
            database="aliments")

        mycursor2 = db2.cursor()
        mycursor2.execute(f"""DELETE FROM aliment WHERE idaliment = {y[0]}""")

        db2.commit()

        db2 = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="dylaniron",
            database="aliments")

        mycursor2 = db2.cursor()
        mycursor2.execute(f"""DELETE FROM aliment WHERE idaliment = {y[0]}""")

    voir.mainloop()

def ajouteraliment():

    def ajoutage(ila, date):
        print("l'aliment:", ila.get())
        print("la date:", date.get())

        ali = ila.get()
        datum = date.get()

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="dylaniron",
            database="aliments")


        mycursor = db.cursor()
        mycursor.execute("INSERT INTO aliment (ali, date) VALUES (%s,%s)",(ali, datum))
        db.commit()

    ajou= Toplevel()
    ajou.geometry("500x400")
    ajou.title("Frigot intelligent")
    ajou.resizable(False, False)
    #pour le logo
    ajou.iconphoto(False, PhotoImage(file="frigotlogo.png"))
    #fond pour l'image
    bg1 = PhotoImage(file="bonaliment.ppm")
    im = Label(ajou, image=bg1)
    im.place(x=0, y=0, relheight=1, relwidth=1)
    #entree pour
    # pour le mail
    monalim = Label(ajou, text="Nom de l'aliment", bg="yellow", fg="black")
    monalim.place(x=120, y=60, width=240)
    ila = StringVar()
    meali = Entry(ajou, textvariable=ila, bg="#DEFEFF", fg="black")
    meali.place(x=120, y=80, width=240)
    # pour le mot de passe
    mondat = Label(ajou, text="Date de l'aliment", bg="yellow", fg="black")
    mondat.place(x=120, y=140, width=240)
    date = StringVar()
    medate = Entry(ajou, textvariable=date, bg="white", fg="black")
    medate.place(x=120, y=160, width=240)
    #partial pour get
    ajoutage = partial(ajoutage, ila, date)
    #le bouton
    ajbutton = Button(ajou, text="ajouter", bg="yellow", fg="black", command=ajoutage)
    ajbutton.place(x=300, y=220, width=100)

    ajou.mainloop()

#fenetre princinpale
fen = Tk()





















































































































































































































def datum():


    now = datetime.datetime.now()
    dat = now.strftime("%d/%m/%Y")
    huur = now.strftime("%H:%M")

    lab1.config(text=f"{dat}")
    lab1.after(100, datum)

    if huur == "00:00":
        lab1.config(text=f"{dat}")
        lab1.after(100, clock)


fen.geometry("800x600")
fen.title("Frigot intelligent")
fen.iconphoto(False, PhotoImage(file="frigotlogo.png"))
#pour l'image de fond du programme
bg = PhotoImage(file="fondprincipale.ppm")
nb = Label(fen, image=bg)
nb.place(x=0, y=0, relheight=1, relwidth=1)
fen.resizable(False, False)
#pour l'heure
lab = Label(fen, text="", font=("arial",20), fg="blue", bg="white")
lab.place(x=40, y=50)
clock()
#pour la date
lab1 = Label(fen, text="", font=("arial",20), fg="blue", bg="white")
lab1.place(x=20, y=5)
datum()
#la date en fonction de l'heure

#bouton pour voir les aliments
bout_voir = PhotoImage(file="button_voir-aliments.png")
bout_vue = Label(image=bout_voir)
mybout1 = Button(fen, image=bout_voir, borderwidth=0, bg="#46474b", fg="#46474b", command=voiraliment)
mybout1.place(x=260, y=202)
#bouton pour ajouter les aliments
bout_ajouter = PhotoImage(file="button_ajouter-aliments.png")
bout_ajou = Label(image=bout_ajouter)
mybout1 = Button(fen, image=bout_ajouter, borderwidth=0, bg="#46474b", fg="#46474b", command=ajouteraliment)
mybout1.place(x=260, y=290)
fen.mainloop()