import tkinter as tk
from time import strftime

def time_update():
    # सध्याची वेळ मिळवणे (Format: तास:मिनिट:सेकंद)
    string = strftime('%H:%M:%S %p')
    # लेबलचा मजकूर बदलणे
    label.config(text=string)
    # दर १ सेकंदाने (१००० मिलिसेकंद) हे फंक्शन पुन्हा चालवणे
    label.after(1000, time_update)

root = tk.Tk()
root.title("अजिंक्यचे घड्याळ")

# घड्याळाचा लूक डिझाइन करणे
label = tk.Label(root, font=("Arial", 50, "bold"), background="black", foreground="cyan")
label.pack(anchor='center', expand=True)

# वेळ अपडेट करण्याचे फंक्शन सुरू करणे
time_update()

root.mainloop()
