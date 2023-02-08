from tkinter import *

from random import sample, randint, uniform


def click_1():
    def click():
        lbl.config(
            text=f"{randint(int(num_1.get()), int(num_2.get()))}"
        )

    new_window_1 = Tk()
    new_window_1.title('Окно номер 1')
    new_window_1.geometry('300x100')

    num_1 = Entry(new_window_1, width=20)
    num_2 = Entry(new_window_1, width=20)

    num_1.grid(column=1, row=0)
    num_2.grid(column=1, row=1)

    lbl_1 = Label(new_window_1, text="Первое число:")
    lbl_2 = Label(new_window_1, text="Второе число:")

    lbl_1.grid(column=0, row=0)
    lbl_2.grid(column=0, row=1)

    lbl = Label(new_window_1)
    lbl.grid(column=1, row=2)

    btn = Button(new_window_1, text='Случайное число:', command=click)
    btn.grid(column=0, row=2)


def click_2():
    def click():
        lbl.config(
            text=f"{uniform(float(num_1.get()), float(num_2.get()))}"
        )

    new_window_2 = Tk()
    new_window_2.title('Окно номер 2')
    new_window_2.geometry('300x100')

    num_1 = Entry(new_window_2, width=20)
    num_2 = Entry(new_window_2, width=20)

    num_1.grid(column=1, row=0)
    num_2.grid(column=1, row=1)

    lbl_1 = Label(new_window_2, text="Первое число:")
    lbl_2 = Label(new_window_2, text="Второе число:")

    lbl_1.grid(column=0, row=0)
    lbl_2.grid(column=0, row=1)

    lbl = Label(new_window_2)
    lbl.grid(column=1, row=2)

    btn = Button(new_window_2, text='Случайное число:', command=click)
    btn.grid(column=0, row=2)


def click_3():
    def click():
        sequences = range(int(num_1.get()), int(num_2.get()) + 1)
        lbl.config(
            text=f'{sample(sequences, k=len(sequences))}'
        )

    new_window_3 = Tk()
    new_window_3.title('Окно номер 3')
    new_window_3.geometry('300x100')

    num_1 = Entry(new_window_3, width=20)
    num_2 = Entry(new_window_3, width=20)

    num_1.grid(column=1, row=0)
    num_2.grid(column=1, row=1)

    lbl_1 = Label(new_window_3, text="Первое число:")
    lbl_2 = Label(new_window_3, text="Второе число:")

    lbl_1.grid(column=0, row=0)
    lbl_2.grid(column=0, row=1)

    lbl = Label(new_window_3)
    lbl.grid(column=1, row=2)

    btn = Button(new_window_3, text='Перемешанные числа:', command=click)
    btn.grid(column=0, row=2)


def click_4():
    def click():
        elements = element_str.get().split()

        new_elements = Entry(new_window_4, width=20)
        new_elements.grid(column=1, row=2)

        count_elements = int(count.get())

        new_elements.insert(0, str(sample(elements, k=count_elements)))
        new_elements.configure(state='readonly')

    new_window_4 = Tk()
    new_window_4.title('Окно номер 4')
    new_window_4.geometry('300x100')

    element_str = Entry(new_window_4, width=20)
    count = Entry(new_window_4, width=20)

    element_str.grid(column=1, row=0)
    count.grid(column=1, row=1)

    lbl_1 = Label(new_window_4, text='Элементы: ')
    lbl_2 = Label(new_window_4, text='Количество: ')

    lbl_1.grid(column=0, row=0)
    lbl_2.grid(column=0, row=1)

    btn = Button(new_window_4, text='Выбрать:', command=click)
    btn.grid(column=0, row=2)


window = Tk()
window.title('Main')
window.geometry('220x100')

button_1 = Button(window, text='1', command=click_1, height=3, width=3)
button_2 = Button(window, text='2', command=click_2, height=3, width=3)
button_3 = Button(window, text='3', command=click_3, height=3, width=3)
button_4 = Button(window, text='4', command=click_4, height=3, width=3)

button_1.grid(column=1, row=0)
button_2.grid(column=2, row=0)
button_3.grid(column=3, row=0)
button_4.grid(column=4, row=0)

window.mainloop()
