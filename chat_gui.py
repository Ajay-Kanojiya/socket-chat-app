from tkinter import *

root = Tk()

root.title("ChatApp")
root.iconbitmap("chatapp.ico")
root.geometry("700x500")
root.configure(background="#a08e8e")
root.resizable(width=False, height=False)
wndw = Label(root, text="Welcome to ChatApp", font="Helvetica 15 bold", bg="#a08e8e")
wndw.place(x=350, y=60, anchor="center")
host_label = Label(root, text="Enter host", bg="#a08e8e")
port_label = Label(root, text="Enter port", bg="#a08e8e")
host_label.place(x=250, y=90)
port_label.place(x=250, y=120)
host_entry = Entry(root)
port_entry = Entry(root)
host_entry.place(x=320, y=90)
port_entry.place(x=320, y=120)

def callback():
    host = Label(root, text=host_entry.get(), bg="#a08e8e")
    port = Label(root, text=port_entry.get(), bg="#a08e8e")
    host.place(x=350, y=250, anchor="center")
    port.place(x=350, y=270, anchor="center")

submit_button = Button(root, text="Submit", font="Helvetica 10 bold" ,bg="#a08e8e", command=callback)
submit_button.place(x=320, y=160)

root.mainloop()
