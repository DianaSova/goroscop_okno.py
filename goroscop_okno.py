from tkinter import *
from tkinter import ttk
from datetime import datetime

def Data(day, month, year):
    JD = day + (153*month + 2) / 5 + 365*year + year / 4 - year / 100 + \
    year / 400 - 32045
    return JD

def Proverka(value, Min, Max):
    D = value.get()
    D = int(D)
    if D >= Min and D <= Max:
        return D

def calculate():
    global Resultlable
    try:
        A = Proverka(year, -9999, 9999)
        B = Proverka(month, 1, 12)
        if A % 4 == 0:
            E = 1
        else:
            E = 0
        Days=[31, 28+E, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        C = Proverka(day, 1, Days[B-1])

        now = datetime.date(datetime.now())
        now = Data(now.day, now.month, now.year)

        F = now - Data(C, B, A)
        if F == 0:
            Resultlable.set('Все ясно, автору 0 лет')
        if F > 0:
            Resultlable.set(f'Прошло {datetime.now().year - A} '
                f'лет или {F} дней, или {F*23.9344444444} часов, '
                f'или {F*23.9344444444*60} минут, или '
                f'{F*23.9344444444*60*3600} секунд со дня рождения.')
        if F < 0:
            Resultlable.set(f'До рождения осталось '
                f'{-(datetime.now().year - A)} лет, или {-F} дней, '
                f'или {-(F*23.9344444444)} часов, или '
                f'{-(F*23.9344444444*60)} минут, или '
                f'{-(F*23.9344444444*60*3600)} секунд.')
    except:
        pass
        Resultlable.set('Введены некорректные данные. Try again.')

root = Tk()
root.title("Goroscop")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Узнай, сколько времени ты существуешь.")\
    .grid(column=1, columnspan=3, row=0, sticky=W)

ttk.Label(mainframe, text="Укажи дату рождения")\
    .grid(column=1, columnspan=3, row=1, sticky=W)

ttk.Label(mainframe, text="День:")\
    .grid(column=1, columnspan=1, row=2, sticky=E)

day = StringVar()
day_entry = ttk.Entry(mainframe, width=7, textvariable=day)
day_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Месяц:")\
    .grid(column=1, columnspan=1, row=3, sticky=E)

month = StringVar()
month_entry = ttk.Entry(mainframe, width=7, textvariable=month)
month_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Label(mainframe, text="Год:")\
    .grid(column=1, columnspan=1, row=4, sticky=E)

year = StringVar()
year_entry = ttk.Entry(mainframe, width=7, textvariable=year)
year_entry.grid(column=2, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Рассчитать", command=calculate)\
    .grid(column=2, row=5, sticky=(W, E))

Resultlable = StringVar()
ttk.Label(mainframe, justify=CENTER, textvariable = Resultlable)\
    .grid(column=1, columnspan=3, row=6)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()