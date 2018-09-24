import tkinter as tk

window =tk.Tk()
window.geometry("500x300")
window.title("KW to Hp CCONVERTER")
firstlabel=tk.Label(window, text="Enter Engine Output In KW")
firstlabel.grid(column=0, row=0)

kw_entry=tk.Entry()
kw_entry.grid(column=0,row=3) #the postion of this entry in the window

secondlabel=tk.Label(window, text="KW")
secondlabel.grid(column=1, row=3)



def conversion():
    performance=kwtohp('The Engine Output In Horsepower', int(kw_entry.get()))

    text_answer=tk.Text(master =window, height=5, width=20)
    text_answer.grid(column=1, row=5)
    answer_text="{name} Is : {HP} horsepower".format(name=performance.name, HP=performance.HP())
    text_answer.insert(tk.END, answer_text)

convertbutton=tk.Button(text="Convert",command=conversion)
convertbutton.grid(column=1, row=4)

class kwtohp():
    def __init__(self, name, KW):
        self.name=name
        self.KW=KW

    def HP(self):
        horsepower=self.KW*1.341
        return horsepower

window.mainloop()
