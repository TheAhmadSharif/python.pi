import tkinter as tk



def start_action():
    print("Start button clicked")

def stop_action():
    print("Stop button clicked")








root = tk.Tk()
root.geometry("600x300")
root.title("Keyboard Storke")


menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_command(label='Exit', command=root.quit)


start_button = tk.Button(root, text='Start', width=25, command=start_action)
start_button.pack(pady=20) 

stop_button = tk.Button(root, text='Stop', width=25, command=stop_action)
stop_button.pack()

root.mainloop()
