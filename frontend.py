"""
This program stores this book information:
Title - Author - year - ISBN

After that, a user can:

- View all records
- Search a book
- Add a book
- Update the information of a book
- Delete 
- Close the program

Frontend view:

  |   0   |  1  |   2    |    3    |
0 | Title | ___ | Author | _______ |
1 | Year  | ___ |  ISBN  | _______ |
2 | ----------  |   ▲    | View All|  
3 | |  List  |  |   |    |  Search |
4 | |   Box  |  |   |    |   Add   |
5 | |        |  |   |    |  Update |
6 | |        |  |   |    |  Delete |
7 |  --------   |   ▼    |  Close  |
"""

from tkinter import *

window = Tk()

# Create the labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Create the entry points with their variables
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# Create the listbox
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Create the scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# Configure and associate the listbox with the scrollbar
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# create the buttons
b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)

# Init the GUI
window.mainloop()