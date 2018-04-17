import tkinter as tk
import pymysql


#global variables
name='NULL'
age='404'
contact='404'
address='NULL'

#gui functions
def createViewMissingWindow(): #creates new window on clicking 'See Missing Persons'
    def showRecords():
        data=readfromDB()
        for i, j in enumerate(data):
            tk.Label(missingWindow, text=j[0]).grid(row=i+1, column=0)
            tk.Label(missingWindow, text=j[1]).grid(row=i+1, column=1)
            tk.Label(missingWindow, text=j[2]).grid(row=i+1, column=2)
            tk.Label(missingWindow, text=j[3]).grid(row=i+1, column=3)
     #gui for window2
    missingWindow=tk.Toplevel(window)
    missingWindow.title("Persons Currently Missing")
    missingName=tk.Label(missingWindow, text="Name")
    missingAge=tk.Label(missingWindow, text="Age")
    missingContact=tk.Label(missingWindow, text="Contact")
    missingAdr=tk.Label(missingWindow, text="Last Seen")
    missingName.grid(row=0, column=0)
    missingAge.grid(row=0, column=1)
    missingContact.grid(row=0, column=2)
    missingAdr.grid(row=0, column=3)
    showRecords()
    missingWindow.mainloop()
    
def readfromDB():
     #connect to DB
    db=pymysql.connect("localhost", "root", "1337", "missingPersons")
    cursor=db.cursor()
    cursor.execute("select * from missingpersondetails")
    return cursor.fetchall()
def getValues():
    name=fnameEntry.get()
    age=ageEntry.get()
    contact=contactEntry.get()
    address=addrEntry.get()

def insertData():
    #get values
    name=fnameEntry.get()
    age=ageEntry.get()
    contact=contactEntry.get()
    address=addrEntry.get()

    #connect to DB
    db=pymysql.connect("localhost", "root", "1337", "missingPersons")
    cursor=db.cursor()

    #sqlInsert="insert into missingpersondetails(name, age, mobilenumber, lastseenlocation) values (%s, %s. %s, %s)"
    cursor.execute("insert into missingpersondetails(name, age, mobilenumber, lastseenlocation) values ('"+name+"','"+age+"','"+contact+"','"+address+"')")
    print (name)
    db.commit()
    db.close()
#gui
window = tk.Tk()
window.title("Missing Person Information")
canvas = tk.Canvas(window, width=200, height=200)
photoSpace = canvas.create_rectangle(25, 0, 195, 150, fill='white')
canvas.move(photoSpace, -10,20)
fnameLabel = tk.Label(window, text="Full Name:")
fnameEntry = tk.Entry(window)
ageLabel = tk.Label(window, text="Age:")
ageEntry = tk.Entry(window)
addrLabel = tk.Label(window, text="Last Seen:")
addrEntry = tk.Entry(window)

contactLabel = tk.Label(window, text="Contact for receiving info:")
contactEntry = tk.Entry(window)
submitBtn = tk.Button(text="Submit", bg="red", command=insertData)
seeMissingBtn = tk.Button(text = "See Missing Persons", bg = "white", command=createViewMissingWindow)


#pack
canvas.pack()
fnameLabel.pack()
fnameEntry.pack()

ageLabel.pack()
ageEntry.pack()
addrLabel.pack()
addrEntry.pack()
contactLabel.pack()
contactEntry.pack()
submitBtn.pack()
seeMissingBtn.pack()

#mainloop
window.mainloop()
