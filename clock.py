import tkinter as tk
from time import strftime 

# Create the main window
root = tk.Tk()
root.title('Time Display')

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p\n%D')
    label.config(text=string)
    label.after(1000, time)

# Create a label widget to display time
label = tk.Label(root, font=('calibri', 50, 'bold'), background='green', foreground='black')
label.pack(anchor='center')

# Call the time function to start the clock
time()

# Run the GUI main loop
root.mainloop()

