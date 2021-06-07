from tkinter import *
import tkinter.messagebox
import time
import sqlite3


class Forms(Frame):
    def __init__(self, master):
        super(Forms, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.db_conn = None
        self.my_db_title = "db_citizens"

    def create_widgets(self):
        line = 1

        self.lbl_title = Label(self, text="NEW BIRTH REGISTRATION")
        self.lbl_title.grid(row=line, column=0, sticky=N, columnspan=30)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_lstname = Label(self, text='Lastname:')
        self.lbl_lstname.grid(row=line, column=0, sticky=W)
        self.lstname = Entry(self, width=20, text='')
        self.lstname.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_frstname = Label(self, text='Firstname:')
        self.lbl_frstname.grid(row=line, column=0, sticky=W)
        self.frstname = Entry(self, width=20, text='')
        self.frstname.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_mdname = Label(self, text='Middlename:')
        self.lbl_mdname.grid(row=line, column=0, sticky=W)
        self.mdname = Entry(self, width=20, text='')
        self.mdname.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_d8fbrth = Label(self, text='Date of Birth(Format:DD/MM/YYYY): ')
        self.lbl_d8fbrth.grid(row=line, column=0, sticky=W)
        self.d8fbrth = Entry(self, width=20, text='')
        self.d8fbrth.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_mthrname = Label(self, text="Mother's Name (Lastname first):")
        self.lbl_mthrname.grid(row=line, column=0, sticky=W)
        self.mthrname = Entry(self, width=20, text='')
        self.mthrname.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_fthrname = Label(self, text="Father's Name (Lastname first):")
        self.lbl_fthrname.grid(row=line, column=0, sticky=W)
        self.fthrname = Entry(self, width=20, text='')
        self.fthrname.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_plcefbrth = Label(self, text='Place of Birth')
        self.lbl_plcefbrth.grid(row=line, column=0, sticky=W)
        self.plcefbrth = Entry(self, width=20, text='')
        self.plcefbrth.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.lbl_SOO = Label(self, text='State of Origin')
        self.lbl_SOO.grid(row=line, column=0, sticky=W)
        self.SOO = StringVar()
        self.SOOr = ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River",
                     "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina",
                     "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau",
                     "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara"]
        self.SOO.set(self.SOOr[0])
        self.drpdwn_SOO = OptionMenu(self, self.SOO, *self.SOOr)
        self.drpdwn_SOO.grid(row=line, column=1, sticky=W)

        line += 1
        self.lbl_empty = Label(self, text="").grid(row=line, column=0, sticky=W)

        line += 1
        self.btn_reset = Button(self, text="Reset", width=12, command=self.reset).grid(row=line, column=0, sticky=E)
        self.btn_submit = Button(self, text="Submit", width=12, command=self.submit).grid(row=line, column=1, sticky=W)

    def reset(self):
        self.lstname.delete(0, END)
        self.frstname.delete(0, END)
        self.mdname.delete(0, END)
        self.d8fbrth.delete(0, END)
        self.mthrname.delete(0, END)
        self.fthrname.delete(0, END)
        self.plcefbrth.delete(0, END)

        self.SOO.set(self.SOOr[0])

    def submit(self):
        data = 'Lastname: {}\n'.format(self.lstname.get())
        data += 'Firstname: {}\n'.format(self.frstname.get())
        data += 'Middlename: {}\n'.format(self.mdname.get())
        data += 'Date of Birth: {}\n'.format(self.d8fbrth.get())
        data += "Mother's name: {}\n".format(self.mthrname.get())
        data += "Father's name: {}\n".format(self.fthrname.get())
        data += 'Place of Birth: {}\n'.format(self.frstname.get())
        data += 'State of Origin: {}\n'.format(self.SOO.get())

        self.create_or_connect_to_db()
        self.create_table()
        self.create_rec()
        self.read_birth_db()
        self.exit_db()

        filename = self.lstname.get() + " " + self.frstname.get() + " " + self.mdname.get()
        file = open(filename, 'w+')
        file.write(data)
        file.close()

        # f = open(filename, 'r')
        # print(f.read())
        # f.close()

        tkinter.messagebox.showinfo("Submission Status", "Submitted Successfully!\nNew File created!\nRecord added to Database")
        self.reset()

    def create_or_connect_to_db(self):
        """this will create a database if none exists or open it if it does"""
        self.db_conn = sqlite3.connect(self.my_db_title)

    def create_table(self):
        """this will create the table and the columns in it. the different case (capital and lower letter) is
        just a formality so the code can look neat."""

        query = """
                CREATE TABLE IF NOT EXISTS birth_records
                (
                    number INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50) NOT NULL,
                    dob VARCHAR NOT NULL,
                    mother_name VARCHAR(50) NOT NULL,
                    father_name VARCHAR(50) NOT NULL,
                    place_of_birth VARCHAR(50) NOT NULL,
                    st8_of_origin VARCHAR(50) NOT NULL
                    )
                    """
        print("creating initial columns.....\t\t", end="")
        self.db_conn.execute(query)
        time.sleep(0.5)
        print("Table Created!")

    def create_rec(self):
        """This will enter the records available at the time the database was created"""
        brth_rec = ["INSERT INTO birth_records(name, dob, mother_name, father_name, place_of_birth, st8_of_origin) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format((self.lstname.get() + " " + self.frstname.get() + " " + self.mdname.get()),
                                    self.d8fbrth.get(), self.mthrname.get(), self.fthrname.get(), self.plcefbrth.get(), self.SOO.get())]
        for an_item in brth_rec:
            self.db_conn.execute(an_item)
        self.db_conn.commit()
        time.sleep(0.5)
        print("new record added to database....")

    def read_birth_db(self):
        """pull up all the record in the database for viewing"""
        query1 = "SELECT * FROM birth_records"
        rec_lst = self.db_conn.execute(query1)
        for an_item in rec_lst:
            print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(an_item[0], an_item[1], an_item[2], an_item[3],
                                                                  an_item[4], an_item[5], an_item[6]))

    def exit_db(self):
        """Exit the database after usage"""
        self.db_conn.close()


window = Tk()
window.title("Forms")
window.geometry('600x900')
app = Forms(window)
app.mainloop()
