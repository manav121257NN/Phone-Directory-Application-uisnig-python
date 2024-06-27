from tkinter import *

from tkinter import ttk
import re
from tkinter import filedialog

from tkinter import messagebox

# import re
# import sys
import csv

def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)


def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data

# view()

def remove(i):
    def save(j):
        with open('data.csv',  'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i

    with open('data.csv', 'r') as file:
        reader =  csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element == telephone:
                    new_list.remove(row)
    save(new_list)

# remove('54321')
# view()
def clear():
    Name = e_name.get()
    Gender = c_gender.get()
    Telephone = e_telephone.get()
    Email = e_email.get()

    # Validate mobile number
    if not re.match(r'^(\+\d{1,3}\s?)?(\(\d{1,3}\)?\s?|\d{1,3}\-?\d{1,3}\-?\d{1,4})$', Telephone) or len(Telephone)!= 10:
        messagebox.showwarning('data', 'Please enter a valid mobile number (10 digits only)')
        return

    # Validate email address
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', Email):
        messagebox.showwarning('data', 'Please enter a valid email address')
        return

    data = [Name, Gender, Telephone, Email]

    if Name == '' or Gender == '' or Telephone == '' or Email == '':
        messagebox.showwarning('data', 'Please fill in all fields')
    
    else:
        add(data)
        messagebox.showinfo('data', 'data added successfully')

        # Clear input data
        e_name.delete(0, 'end')
        c_gender.delete(0, 'end')
        e_telephone.delete(0, 'end')
        e_email.delete(0, 'end')

        show()

def update(i):

    def update_newlist(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i[0]
    # ['123','demo','M','123','demo@gmail.com']

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    gender = i[2]
                    telephone = i[3]
                    email = i[4]
                    
                    data = [name, gender, telephone, email]
                    index = new_list.index(row)
                    new_list[index] = data

    update_newlist(new_list)

# sample = ['123', 'girlCoder', 'F', '123', 'girl123@gmail.com']
# update(sample)

# ANSI escape codes for color
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def search(telephone):
    data = []
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]  # Assuming the name is in the first column
            if name.startswith(telephone):
                data.append(row)

    # Print data with colored text
    for row in data:
        colored_row = [Color.CYAN + col + Color.RESET if col.startswith(telephone) else col for col in row]
        print(' '.join(colored_row))

    return data

search('123')

# New function to delete all data from the CSV file
def delete_all():
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete all data?")
    if confirmation:
        with open('data.csv', 'w', newline='') as file:
            file.truncate(0)
        messagebox.showinfo('Success', 'All data has been deleted successfully')
        for widget in frame_table.winfo_children():
            widget.destroy()
        show()



co0 = "#B2D2E3"
co1 = "#840909"
co2 = "#4456F0" 

window = Tk()
window.title ("Phone directory")
window.geometry('700x600')
window.configure(background=co0)
window.resizable(width=FALSE, height=FALSE)

#frames
frame_up = Frame(window, width=800, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=250, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=700, height=450, bg=co0, relief="flat")
frame_table.grid(row=2, column=0, columnspan=1, padx=10, pady=1, sticky=NW)

# functions
def show():  
    global tree

    listheader = ['Name', 'Gender', 'Telephone', 'Email']

    demo_list = view()

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    #tree head
    tree.heading(0, text=' Name', anchor=NW)
    tree.heading(1, text='Gender', anchor=NW)
    tree.heading(2, text='Telephone', anchor=NW)
    tree.heading(3, text='Email', anchor=NW)

    # tree  columns
    tree.column(0, width=175, anchor='nw')
    tree.column(1, width=145, anchor='nw')
    tree.column(2, width=170, anchor='nw')
    tree.column(3, width=175, anchor='nw')

    for item in demo_list:
        tree.insert('', 'end', values=item)

show()

def insert():
    Name = e_name.get()
    Gender = c_gender.get()
    Telephone = e_telephone.get()
    Email = e_email.get()

    # Validate mobile number
    if not re.match(r'^(\+\d{1,3}\s?)?(\(\d{1,3}\)?\s?|\d{1,3}\-?\d{1,3}\-?\d{1,4})$', Telephone) or len(Telephone)!= 10:
        messagebox.showwarning('data', 'Please enter a valid mobile number (10 digits only)')
        return

    # Validate email address
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', Email):
        messagebox.showwarning('data', 'Please enter a valid email address')
        return

    data = [Name, Gender, Telephone, Email]

    if Name == '' or Gender == '' or Telephone == '' or Email == '':
        messagebox.showwarning('data', 'Please fill in all fields')
    
    else:
        add(data)
        messagebox.showinfo('data', 'data added successfully')

        e_name.delete(0, 'end')
        c_gender.delete(0, 'end')
        e_telephone.delete(0, 'end')
        e_email.delete(0, 'end')

        show()

def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        Name = str(tree_list[0])
        Gender = str(tree_list[1])
        Telephone = str(tree_list[2])
        Email = str(tree_list[3])

        e_name.insert(0, Name)
        c_gender.insert(0, Gender)
        e_telephone.insert(0, Telephone)
        e_email.insert(0, Email)

        def confirm():
            new_name = e_name.get()
            new_gender = c_gender.get()
            new_telephone = e_telephone.get()
            new_email = e_email.get()

            data = [new_telephone, new_name, new_gender, new_telephone, new_email]

            update(data)

            messagebox.showinfo('Success', 'data updated successfully')

            e_name.delete(0, 'end')
            c_gender.delete(0, 'end')
            e_telephone.delete(0, 'end')
            e_email.delete(0, 'end')

            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()
            
        b_confirm =  Button(frame_down, text="Confirm", width=10, height=1, bg=co2, fg = co0, font=('Ivy 8 bold'), command=confirm)
        b_confirm.place(x = 290, y = 110)

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_telephone = str(tree_list[2])

        remove(tree_telephone)

        messagebox.showinfo('Success', 'Data has been deleted successfully')

        for widget in frame_table.winfo_children():
            widget.destroy()
        show()

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')

def to_search():
    telephone = e_search.get()

    data = search(telephone)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end', values = item)
        
    e_search.delete(0, 'end')

def import_contacts():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("CSV files", ".csv"), ("All files", ".*")))
    if filename:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                add(row)
        messagebox.showinfo('Success', 'Contacts imported successfully')
        show()

def export_contacts():
    filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV files", ".csv"), ("All files", ".*")))
    if filename:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(view())
        messagebox.showinfo('Success', 'Contacts exported successfully')


#frame_up widgets

app_name = Label(frame_up, text="Phonebook", height = 1, font=('Verdana 17 bold'), bg = co2, fg = co0)
app_name.place(x=5, y=5)

#frame_down widgets
l_name = Label(frame_down, text="Name :-", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_name.place(x=10, y=20)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=80, y=20)

l_gender = Label(frame_down, text="Gender :-", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_gender.place(x=10, y=50)
c_gender = ttk.Combobox(frame_down, width=27)
c_gender['values'] = ['', 'Femal', 'Male'] 
c_gender.place(x=80, y=50)

l_telephone = Label(frame_down, text="Mobile No:-", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_telephone.place(x=10, y=80)
e_telephone = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_telephone.place(x=80, y=80)

l_email = Label(frame_down, text="Email :-", height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_email.place(x=10, y=110)
e_email = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_email.place(x=80, y=110)

b_search = Button(frame_down, text="Search", height=1, bg=co2, fg = co0,font=('Ivy 8 bold'), command=to_search)
b_search.place(x=290, y=20)
e_search = Entry(frame_down, width=16, justify='left', font=('Ivy', 11), highlightthickness=1, relief="solid")
e_search.place(x=347, y=20)

b_view = Button(frame_down, text="View All", width=10, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'), command = show)
b_view.place(x=290, y=50)

b_add = Button(frame_down, text="Add", width=10, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'), command=insert)
b_add.place(x=400, y=50)

b_update = Button(frame_down, text="Update", width=10, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'), command=to_update)
b_update.place(x=400, y=80)

b_delete = Button(frame_down, text="Delete", width=10, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'), command = to_remove)
b_delete.place(x=400, y=110)

# Button to delete all data
b_delete_all = Button(frame_down, text="Delete All", width=10, height=1, bg="#840909", fg="#B2D2E3", font=('Ivy 8 bold'), command=delete_all)
b_delete_all.place(x=290, y=85)

b_import = Button(frame_down, text="IMPORT", width=10, height=1, bg="#00C957", fg="#840909", font=('Verdana 10 bold'), command=import_contacts)
b_import.place(x=100, y=200)

b_export = Button(frame_down, text="EXPORT", width=10, height=1, bg="#00CDCD", fg="#840909", font=('Verdana 10 bold'), command=export_contacts)
b_export.place(x=200, y=200)

b_clear = Button(frame_down, text="Clear", width=10, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'), command=lambda: (e_name.delete(0, 'end'), c_gender.delete(0, 'end'), e_telephone.delete(0, 'end'), e_email.delete(0, 'end')))
b_clear.place(x=290, y=120)



window.mainloop()