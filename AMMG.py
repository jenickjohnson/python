import tkinter as tk
import webbrowser

def firstbutton(event):
    webbrowser.open_new_tab('https://www.bmw.com/en/performance.html')

def secondbutton(event):
    webbrowser.open_new_tab('https://www.mercedes-amg.com/en.html')

def thirdbutton(event):
    webbrowser.open_new_tab("https://www.audi.de/de/brand/de.html")


window =tk.Tk()
window.geometry('500x300')

mainlabel=tk.Label(window, text='welcome to cars.com')
mainlabel.grid(column=0, row=0)

titlelabel=tk.Label(window, text="choose your car brand")
titlelabel.grid(column=0, row=1)

button1=tk.Button(window, text="BMW M SPORTS")
button1.grid(column=1, row=3)

button2=tk.Button(window, text="AMG")
button2.grid(column=2, row=3)

button3=tk.Button(window,text="AUDI")
button3.grid(column=3, row=3)

button1.bind("<Button-1>",firstbutton)
button2.bind("<Button-1>",secondbutton)
button3.bind("<Button-1>",thirdbutton)

window.mainloop()
