import tkinter as tk
import logging
from binance_futures import get_contracts



logger = logging.getLogger()


logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s :: %(message)s")

stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)






if __name__ == "__main__":
    root = tk.Tk()
    # fill in the background so there is no whitespace
    root.configure(bg="gray12")

    binance_contracts = get_contracts(count=50)
    i = 0
    j = 0 

    calibri_font = ("Calibri", 10, "normal")
    for contract in binance_contracts:
        # label_widget = tk.Label(root, text=contract, borderwidth=1, relief=tk.GROOVE, width=14)
        label_widget = tk.Label(root, text=contract, bg="gray12", fg="SteelBlue1", width=14, font=calibri_font)
        # label_widget.pack(side=tk.TOP)
        label_widget.grid(row=i, column=j, sticky='ew')

        if i == 4:
            j += 1
            i = 0
        else:
            i += 1
        



    root.mainloop()
