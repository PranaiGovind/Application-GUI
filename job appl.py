#Mungara Ganesh Haricharan RA1911030010091
import tkinter as tk
import sqlite3
from tkinter import filedialog
from tkinter import messagebox
conn = sqlite3.connect('thebase.db')
var = conn.cursor()
def submit():
    conn = sqlite3.connect('thebase.db')
    var = conn.cursor()
    var.execute("""CREATE TABLE if not exists entries(first_name text,last_name text,email text,
            education text,address1 text,address2 text,country text,city text,
            state text,zipcode text,phone1 text,phone2 text,hobbies text,company text,
            job text,duration text,r1name text,r1phone text,r2name text,r2phone text)""")
    var.execute('INSERT INTO entries VALUES(:first_name,:last_name,:email,:education,:address1,:address2,:country,:city,:state,:zipcode,:phone1,:phone2,:hobbies,:company,:job,:duration,:r1name,:r1phone,:r2name,:r2phone)',
                {
                    'first_name' : first_name.get(),
                    'last_name' : last_name.get(),
                    'email' : email.get(),
                    'education' : education.get(),
                    'address1' : address1.get(),
                    'address2' : address2.get(),
                    'country' : country.get(),
                    'city' : city.get(),
                    'state' : state.get(),
                    'zipcode' : zipcode.get(),
                    'phone1' : phone1.get(),
                    'phone2' : phone2.get(),
                    'hobbies' : hobbies.get(),
                    'company' : company.get(),
                    'job' : job.get(),
                    'duration' : duration.get(),
                    'r1name' : r1name.get(),
                    'r1phone' : r1phone.get(),
                    'r2name' : r2name.get(),
                    'r2phone' : r2phone.get()}
                )
    conn.commit()
    msg = messagebox.showinfo( "Job Application","SUBMITTED SUCCESSFULLY")
    conn.close()
def browsing():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File", filetypes = (("Text files",".txt"),("all files",".")))
    labelfileexp.configure(text="File Opened:"+filename)
window = tk.Tk()
window.title("Job Portal")
bigl = tk.Label(window, text='Job Application',font=('Helvetica 13 bold'),fg='black').place(x = 145,y= 10)
sidel = tk.Label(window, text='Personal Information',font=('bold'), anchor='w',fg='red',width=25).place(x = 0,y= 30)
name = tk.Label(window, text = "Name").place(x = 0,y = 60)
first_name = tk.Entry(window)
first_name.place(x=140,y=60)
last_name = tk.Entry(window)
last_name.place(x=270,y=60)
email = tk.Entry(window)
email.insert(0, "user@example.com")
email.place(x = 140, y = 100)
label_1 = tk.Label(window, text="First Name", width=15, font=("aerial",6)).place(x=120,y=80)
label_2 = tk.Label(window, text="Last Name", width=15, font=("aerial",6)).place(x=250,y=80)
Email = tk.Label(window, text = "Email").place(x = 0, y = 100)
education = tk.StringVar(window)
education.set("Please Choose")
label = tk.Label(window, text = "Education").place(x = 0, y = 132)
menu = tk.OptionMenu(window, education, "intermediate", "UG", "PG")
menu.configure(width=30)
menu.place(x=138,y=125)
labelfileexp = tk.Label(window, width = 100, height = 4, fg = "blue")
explorer = tk.Label(window, text = "Resume").place(x = 0, y = 172)
labelfileexp.place(x=108,y=152)
buttonfileexp = tk.Button(window,text = "Choose File",command = browsing).place(x=138,y=170)
address = tk.Label(window, text = "Address").place(x = 0,y = 210) 
address1 = tk.Entry(window, width=42)
address1.place(x=140,y=210)
address2 = tk.Entry(window, width=42)
address2.place(x=140,y=250)
label_3 = tk.Label(window, text="Address 1", width=15, font=("bold",6)).place(x=220,y=232)
label_4 = tk.Label(window, text="Address 2", width=15, font=("bold",6)).place(x=220,y=270)
country = tk.StringVar(window)
country.set("Select a Country")
menu2 = tk.OptionMenu(window, country, "India", "Canada", "USA", "UK", "France", "Brazil")
menu2.configure(width=36)
menu2.place(x=138,y=285)
city = tk.Entry(window, width=22)
city.place(x=138,y=328)
state = tk.Entry(window, width=6)
state.place(x=290,y=328)
zipcode = tk.Entry(window, width=8)
zipcode.place(x=340,y=328)
label_5 = tk.Label(window, text="City", width=6, font=("bold",6)).place(x=127,y=352)
label_6 = tk.Label(window, text="State", width=6, font=("bold",6)).place(x=290,y=352)
label_7 = tk.Label(window, text="ZIP", width=6, font=("bold",6)).place(x=347,y=352)
phnnum = tk.Label(window, text = "Phone Number").place(x = 0,y = 370)
phone1 = tk.Entry(window, width=6)
phone1.place(x=140,y=371)
phone2 = tk.Entry(window, width=30)
phone2.place(x=185,y=371)
hobby = tk.Label(window, text = "What are your hobbies?").place(x = 0,y = 397)
hobbies = tk.Entry(window, width=67)
hobbies.place(x=1,y=417)
side2 = tk.Label(window, text='Previous/Current Employment Details',font=('bold'), anchor='w',fg='red',width=50).place(x=0,y=439)
compname = tk.Label(window, text = "Company Name").place(x=0,y=461)
exp = tk.Label(window, text = "Job Title").place(x=0,y=484)
name = tk.Label(window, text = "How long were you here?").place(x = 0,y = 508)
company = tk.Entry(window, width=42)
company.place(x=140,y=460)
job = tk.Entry(window, width=42)
job.place(x=140,y=485)
duration = tk.Entry(window, width=42)
duration.place(x=140,y=510)
side3 = tk.Label(window, text='Reference #1',font=('bold'), anchor='w',fg='red',width=50).place(x=0,y=535)
nameref1 = tk.Label(window, text = "Name").place(x = 0,y = 560)
r1name = tk.Entry(window, width=42)
r1name.place(x=140,y=561)
phnref1 = tk.Label(window, text = "Phone").place(x = 0,y = 590)
r1phone = tk.Entry(window, width=42)
r1phone.place(x=140,y=591)
side4 = tk.Label(window, text='Reference #2',font=('bold'), anchor='w',fg='red',width=50).place(x=0,y=615)
nameref2 = tk.Label(window, text = "Name").place(x = 0,y = 640)
r2name = tk.Entry(window, width=42)
r2name.place(x=140,y=641)
phnref2 = tk.Label(window, text = "Phone").place(x = 0,y = 670)
r2phone = tk.Entry(window, width=42)
r2phone.place(x=140,y=671)
finalbutton = tk.Button(window,text="Apply",width=10,font=('bold',12),bg='red',fg='white',command=submit)
finalbutton.place(x=165,y=705)
window.geometry("412x740")
window.mainloop()