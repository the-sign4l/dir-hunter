#!/usr/bin/python
from tkinter import *
from tkinter import messagebox
from urllib2 import Request , urlopen ,HTTPError , URLError
from tkinter import ttk
from tkinter.filedialog import asksaveasfile


root = Tk()
root.geometry("900x650")
root.title("Dir Hunter")
root.configure(bg = "black")

f = open("dictionary.txt","r")
logo = Label(text = "Dir Hunter", bg = "black" ,fg = "red" , font = ("times",30,"bold")).place(x = 400 , y = 10)

a = StringVar()
tar = Label(root,text = "Target" , fg = "red",bg = "black",font = ("tahoma",12)).place(x = 50 , y = 70)
target = Entry(root,bg = "white", fg = "black" , width = 55 , textvariable = a)
target.place(x = 110 , y = 70)
target.insert(0,"http://www.target.com/")
messagebox.showinfo(title="Warning" , message="Due to the high volume of payloads, it may take some time")

def attack():
	b = a.get()
	for aline in f.readlines():
		try:
			tmp = aline.split()
			url = b+tmp[0]
			req = Request(url)
			response = urlopen(req)
		except IndexError:
			output.insert(0 , "--- No Internet ---")
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			output.insert(0,url)


start = Button(text = "Start" , bg = "black" , fg = "green" , command = attack ).place(x = 560 , y = 65)


output = Listbox(bg = "white" , width = 72 , fg = "green")
output.place(x = 50 , y = 140)


photo = PhotoImage(file = r"sign4l.png") 
photoimage = photo.subsample(3, 3) 

Button(root, image = photoimage).place(x = 80 , y = 400)
Label(root , text = "Author:" , fg = "red" , bg = "black").place(x = 300 , y = 400)
Label(root , text = "sign4l" , fg = "white" , bg = "black").place(x = 350 , y = 400)
Label(root , text = "Instagram:" , fg = "red" , bg = "black").place(x = 300 , y = 420)
Label(root , text = "thesign4l" , fg = "white" , bg = "black").place(x = 372 , y = 420)
Label(root , text = "Twitter:" , fg = "red" , bg = "black").place(x = 300 , y = 440)
Label(root , text = "sign4l1" , fg = "white" , bg = "black").place(x = 352 , y = 440)
Label(root , text = "Youtube:" , fg = "red" , bg = "black").place(x = 300 , y = 460)
Label(root , text = "Sign4l security" , fg = "white" , bg = "black").place(x = 358 , y = 460)
Label(root , text = "Discord:" , fg = "red" , bg = "black").place(x = 300 , y = 480)
Label(root , text = "https://discord.gg/JRm2nPt" , fg = "white" , bg = "black").place(x = 355 , y = 480)
Label(root , text = "Github:" , fg = "red" , bg = "black").place(x = 300 , y = 500)
Label(root , text = "https://github.com/the-sign4l" , fg = "white" , bg = "black").place(x = 350 , y = 500)
Label(root , text = "Copyright sign4l | 2020" , fg = "green" , bg = "black").place(x = 350 , y = 540)

root.mainloop()
