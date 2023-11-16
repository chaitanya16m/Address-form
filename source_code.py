from tkinter import *
import mysql.connector
from data_retrieve import display_page  # importing function from data_retrieve.py file

# establishing connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='****',
    database='address_book'
)

# print(conn)

cursor = conn.cursor()


# Creating the Database
# query = 'CREATE DATABASE address_book'
# cursor.execute(query)

# Creating Table
# query = """CREATE TABLE data(
#     pid int NOT NULL AUTO_INCREMENT,
#     first_name varchar(255) NOT NULL,
#     last_name varchar(255),
#     address varchar(255),
#     city varchar(255),
#     state varchar(255),
#     pincode int,
#     PRIMARY KEY (pid)
# )"""
# cursor.execute(query)


def submit():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='****',
        database='address_book'
    )
    cursor = conn.cursor()

    # getting form data
    fname1 = fname.get()
    lname1 = lname.get()
    adres1 = adres.get()
    cty1 = cty.get()
    stat1 = stat.get()
    pcode1 = pcode.get()

    # applying empty validation
    if fname1 == '' or lname1 == '' or adres1 == '' or cty1 == '' or stat1 == '' or pcode1 == '':
        message.set("Fill the empty field!!!")
    else:

        # # Preparing SQL query to INSERT a record into the database.
        insert_stmt = (
            """INSERT INTO data(first_name, last_name, address, city, state, pincode)
            VALUES (%s, %s, %s, %s, %s, %s)"""
        )
        data = (fname1, lname1, adres1, cty1, stat1, pcode1)

        try:
            # executing the sql command
            cursor.execute(insert_stmt, data)
            # commit changes in database
            conn.commit()
            conn.close()

        except:
            conn.rollback()
        message.set("Stored successfully")

        # clearing entry box after entering data
        fname.set('')
        lname.set('')
        adres.set('')
        cty.set('')
        stat.set('')
        pcode.set('')


def address_form():
    global add_window
    add_window = Tk()
    add_window.configure(bg="#E9F7EF")

    # Setting title of window
    add_window.title("Address Form")

    # setting height and width of screen
    add_window.geometry("350x400")

    # declaring variable
    global message;
    global fname
    global lname
    global adres
    global cty
    global stat
    global pcode

    fname = StringVar()
    lname = StringVar()
    adres = StringVar()
    cty = StringVar()
    stat = StringVar()
    pcode = StringVar()
    message = StringVar()

    # Creating layout of Registration form
    Label(add_window, width="300", text="Please enter details below", bg="violet", fg="white").pack()

    # fname Label
    Label(add_window, text="First Name * ").place(x=20, y=40)
    # fname textbox
    Entry(add_window, textvariable=fname).place(x=90, y=42)

    # lname Label
    Label(add_window, text="Last Name * ").place(x=20, y=80)
    # lname textbox
    Entry(add_window, textvariable=lname).place(x=90, y=82)

    # address Label
    Label(add_window, text="Address * ").place(x=20, y=120)
    # address textbox
    Entry(add_window, textvariable=adres).place(x=90, y=122)

    # city Label
    Label(add_window, text="City * ").place(x=20, y=160)
    # city textbox
    Entry(add_window, textvariable=cty).place(x=90, y=162)

    # state Label
    Label(add_window, text="State * ").place(x=20, y=200)
    # state textbox
    Entry(add_window, textvariable=stat).place(x=90, y=202)

    # pincode Label
    Label(add_window, text="Pincode *").place(x=20, y=240)
    # pincode textbox
    Entry(add_window, textvariable=pcode).place(x=90, y=242)

    # Label for displaying login status[success/failed]
    Label(add_window, text="", textvariable=message).place(x=95, y=264)

    # Submit button
    Button(add_window, text="Submit", width=10, height=1, bg="orange", command=submit).place(x=105, y=300)


    # Button to display data
    Button(add_window, text="View Data", width=10, height=1, bg="pink", command=display_page).place(x=105, y=340)

    add_window.mainloop()


# calling function address_form
address_form()
