from tkinter import*

root = Tk()

x = { 
			"name": { "value": ""},
			"age1": { "value": 0.0}
			"age": { "value": 0}
		}

def f():
		for element in x.keys():
			print(element, x[element])

for element in x.keys():
		Label(root, text = element).pack()
		t = type(x[element]["value"])
		if t == int:
			x[element]["var"] = IntVar()
		elseif t == str:
			x[element]["var"] = StringVar()
		else:
			raise TypeError

		x[element]["entry"] = Entry(root, textvariable = x[element]["var"])
		x[element]["entry"].pack()

Button(root, text='Ok', command=f).pack()

root.mainloop()
