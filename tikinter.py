from tkinter import *
import datetime
window = Tk()
#window maken
window.title("weclcome to the age machine")
#format
window.geometry('200x200')
#vakken
dag = Label(window, text="dag geboorte")
maand = Label(window, text="maand geboorte")
jaar = Label(window, text="jaar geboorte")
antwoord = Label(window, text="")
#invoer
daginvoer = Entry(window,width=2)
maandinvoer = Entry(window, width=2)
jaarinvoer = Entry(window, widt=4)

#grid
daginvoer.grid(column=1, row=0)
maandinvoer.grid(column=1, row=1)
jaarinvoer.grid(column=1, row=2)
antwoord.grid(column=0, row=4)
#grid
dag.grid(column=0, row=0)
maand.grid(column=0, row=1)
jaar.grid(column=0, row=2)


#functie leeftijd
def calculateAge():
    invoerDatum = datetime.datetime.now() - datetime.datetime(int(jaarinvoer.get()),int(maandinvoer.get()),int(daginvoer.get()))
    resultaat = (invoerDatum.total_seconds()/31558150) #devided by exact year in seconds 365 + a bit days
    antwoord.configure(text= resultaat)
#functie clear
def Clear():
    daginvoer.delete(0, "end")
    maandinvoer.delete(0,"end")
    jaarinvoer.delete(0,"end")


#de helle mooie knopppen
button1 = Button(window, text="bereken", command=calculateAge)
button1.grid(column=1, row=3)

button2 = Button(window, text="wis", command= Clear)
button2.grid(column=1, row=5)
#mainloop test
window.mainloop()