from tkinter import *


class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("Princess Rescue")
        self.window.geometry("1080x720")
        self.window.minsize(480, 360)
        self.window.iconbitmap("")
        self.window.config(background='#41B77F')

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
        label_title = Label(self.frame, text="Bienvenue sur Princess Rescue", font=("Courrier", 40), bg='#41B77F',fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="Amusez-vous", font=("Courrier", 25), bg='#41B77F', fg='white')
        label_subtitle.pack()

    def create_button(self):
        label_button = Button(self.frame, text="start", font=('Courrier', 25), bg='White')
        label_button.pack()





# afficher
app = MyApp()
app.window.mainloop()
