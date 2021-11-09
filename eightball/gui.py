import tkinter
from ask import ask

class GUI:
	def __init__(self, master):
		self.ask = ask()
		self.answer = ""
		self.root = master
		self.root.title("Eight Ball")
		self.label = tkinter.Label(self.root, text="Enter your question here!")
		self.label.pack()
		self.entry1 = tkinter.Entry(self.root)
		self.entry1.pack()
		self.enter_button = tkinter.Button(self.root, text="Enter", command=self.enter)
		self.enter_button.pack()
		self.close_button = tkinter.Button(self.root, text="Close", command=master.quit)
		self.close_button.pack()

	def enter(self):
		self.label.destroy()
		self.entry1.delete(0, 'end')
		question = self.entry1.get()
		if question != False:
			self.answer = self.ask.choose()
			self.label = tkinter.Label(self.root, text=self.answer)
			self.label.pack()
		else:
			self.label.destroy()
