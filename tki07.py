import tkinter as tk

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
    
	for j in range(0, 3):
		frame = tk.Frame(
			master=window, 
            relief=tk.GROOVE, 
            borderwidth=3
		)
		frame.grid(row=i, column=j, padx=3, pady=3)
        
		label = tk.Label(master=frame, text=f"Row {i}\ncolumn {j}")
		label.pack(padx=3, pady=3)
			
window.mainloop()

