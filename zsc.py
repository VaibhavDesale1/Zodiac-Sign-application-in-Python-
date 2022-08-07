from tkinter import *
from random import choice
from PIL import Image, ImageTk

root = Tk()
root.title("Zodiac Sign Calculator")
root.geometry("500x700+400+10")

def f1():
	date = int(ent_birth_date.get())
	month = int(ent_birth_month.get())
	if date < 1 or date > 31:
		zdi = 'invalid.png'
	elif month < 1 or month > 12:
		zdi = 'invalid.png'
	elif (month == 1 and date >=22) or (month == 2 and date <=21):
		zdi = "aquarius.png"
	elif (month == 2 and date >=22) or (month == 3 and date <=21):
		zdi = "pisces.png"
	elif (month == 3 and date >=22) or (month == 4 and date <=21):
		zdi = "aries.png"
	elif (month == 4 and date >=22) or (month == 5 and date <=21):
		zdi = "taurus.png"
	elif (month == 5 and date >=22) or (month == 6 and date <=21):
		zdi = "gemini.png"
	elif (month == 6 and date >=22) or (month == 7 and date <=21):
		zdi = "cancer.png"
	elif (month == 7 and date >=22) or (month == 8 and date <=21):
		zdi = "leo.png"
	elif (month == 8 and date >=22) or (month == 9 and date <=21):
		zdi = "virgo.png"
	elif (month == 9 and date >=22) or (month == 10 and date <=21):
		zdi = "libra.png"
	elif (month == 10 and date >=22) or (month == 11 and date <=21):
		zdi = "scorpio.png"
	elif (month == 11 and date >=22) or (month == 12 and date <=21):
		zdi = "sagittarius.png"
	elif (month == 12 and date >=22) or (month == 1 and date <=21):
		zdi = "capricorn.png"

	else:
		zdi = 'invalid.png'
	img1 = ImageTk.PhotoImage(Image.open(zdi))
	lbl_result.configure(image=img1)
	lbl_result.image = img1		

f = ('calibri', 20, 'bold')
lbl_birth_date = Label(root, text="enter birth date", font=f)
ent_birth_date = Entry(root, bd=5, font=f)
lbl_birth_date.pack(pady=5)
ent_birth_date.pack(pady=5)

lbl_birth_month = Label(root, text="enter birth month", font=f)
ent_birth_month = Entry(root, bd=5, font=f)
lbl_birth_month.pack(pady=5)
ent_birth_month.pack(pady=5)

btn_find = Button(root, text="Find", font=f, command=f1)
btn_find.pack(pady=5)

img1 = ImageTk.PhotoImage(Image.open("zod.png"))
lbl_result = Label(root, image=img1)
lbl_result.pack()

root.mainloop()

