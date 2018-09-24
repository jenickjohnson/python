import datetime
import tkinter as tk

window= tk.Tk()
window.geometry("500x200")
alabel=tk.Label(window, text= 'please enter date of birth details')
alabel.grid(column=0, row=1)

blabel=tk.Label(window, text= 'Year')
blabel.grid(column=0, row=2)

clabel=tk.Label(window, text= 'Month')
clabel.grid(column=0, row=3)

dlabel=tk.Label(window, text= 'Day')
dlabel.grid(column=0, row=4)

yearentry=tk.Entry()
yearentry.grid(column=1, row=2)

monthentry=tk.Entry()
monthentry.grid(column=1, row=3)

dayentry=tk.Entry()
dayentry.grid(column=1,row=4)

def agecl():
    print(yearentry.get())
    print(monthentry.get())
    print(dayentry.get())   # these print lines are optional will be clean if not used
    you= agecalc('you', datetime.date(int(yearentry.get()),int(monthentry.get()), int(dayentry.get())))

    print(you.age()) # connects to the class agecalc to do the operation with given information to birthday, int is given to convert the yearentry,month...etc from str to integer format
    text_answer=tk.Text(master=window, height=15,width=20) # to show the result in the field
    text_answer.grid(column=1, row=6)
    answer_text="{name} are {age} years old".format(name=you.name, age=you.age())
    text_answer.insert(tk.END, answer_text)

Calculate_button=tk.Button(text="Calculate", command=agecl)# for connecting the button
Calculate_button.grid(column=1, row=5)

class agecalc:
    def __init__(self, name, birthday):
        self.name=name
        self.birthday=birthday


    def age(self):
        today=datetime.date.today()     # intakes the present day
        ageindays= today - self.birthday      #today.year -self.birthday.year for years
        return ageindays

window.mainloop()
