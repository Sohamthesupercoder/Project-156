from tkinter import *root = Tk()root.title("Pokemon")root.geometry("500x500")root.configure(bg = "Red")from PIL import ImageTk , ImageP1label = Label(root , text = "Player 1" , bg = "Blue" , fg = "Aqua")P1label.place(relx = 0.1 , rely = 0.4 , anchor = CENTER)P2label = Label(root , text = "Player 2" , bg = "Blue" , fg = "Aqua")P2label.place(relx = 0.9 , rely = 0.4 , anchor = CENTER)P1score = Label(root , fg = "Blue" , bg = "Aqua")P1score.place(relx = 0.1 , rely = 0.45 , anchor = CENTER)P2score = Label(root , fg = "Blue" , bg = "Aqua")P2score.place(relx = 0.9 , rely = 0.45 , anchor = CENTER)ImageLabel = Label(root , bg = "White")ImageLabel.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)root.mainloop()