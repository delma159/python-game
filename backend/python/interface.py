from tkinter import *
from map import *
from items import Items



class MyApp:

    def test(self):
        Map = MapPrincess(0, 0)
        item = Items()
        game = Controleur(liste_map=Map.generate_map())
        print('test')
        game.affichage_map()
        #print(game.liste_map)

    def __init__(self):
        self.window = Tk()
        self.window.title("Princess Rescue")
        self.window.geometry("1080x720")
        self.window.minsize(480, 360)
        self.window.iconbitmap("")
        self.window.config(background='#373C3C')

        # initialization des composants
        self.frame = Frame(self.window, bg='#41B77F')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_button()

    def create_title(self):
        label_title = Label(self.frame, text="Princess Rescue", font=("Courrier", 40), bg='#537272',fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Commencez la partie", font=("Courrier", 25), bg='#41B77F', fg='white')
        label_subtitle.pack()

    def create_button(self):
        #Map = MapPrincess(0,0)
        #game = Controleur(liste_map=Map.generate_map())
        #item = Items()
        label_button = Button(self.frame, text="start", font=('Courrier', 25), bg='White', command=self.test)
        label_button.pack()


#command=game.afficher_map


# afficher
app = MyApp()
app.window.mainloop()