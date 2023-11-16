import mysql.connector
from tkinter import *


def display_page():
    display_window = Tk()
    display_window.configure(bg="#CCD1D1")

    # Setting title of screen
    display_window.title("Address Data")

    # setting height and width of screen
    display_window.geometry("660x350")


    # connect to MySQl
    conn = mysql.connector.connect(
        host="localhost",  # server name
        user="root",  # username
        password="Poot",  # password
        database="address_book"  # database name
    )
    cursor = conn.cursor()

    # end of connection
    cursor.execute("SELECT * FROM data limit 0,20")
    i = 0
    for user in cursor:
        for j in range(len(user)):
            e = Entry(display_window, width=15, fg='black', bg='#ABB2B9')
            e.grid(row=i, column=j)
            e.insert(END, user[j])
        i = i + 1

    display_window.mainloop()
