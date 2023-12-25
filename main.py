import tkinter as tk
import logging
from binance_futures import write_log



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

logger.debug("logger debug")
logger.info("logger info")
logger.warning("logger warning")
logger.error("logger error")

write_log() 

root = tk.Tk()
root.mainloop()



















if __name__ == "__main__":
    pass