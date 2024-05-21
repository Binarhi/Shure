
import tkinter as tk
from tkinter import ttk, messagebox
from M32APi import * 

from interface import *

from ShureAP import *



con = Console(X32_IP)


Threads =set()

def poll():
         for mic in mics:
            Solo_Parser= Receiver(mic['receiver_ip'], mic['receiver_x32_ch'], mic['receiver_name'], mic['receiver_ch'])   
            #Solo_Parser.Is_Soloed()
            Solo_Btn = threading.Thread(target=Solo_Parser.Is_Soloed)
            Threads.add(Solo_Btn)
            #Solo_Btn.start()




def toggle_script():
   

    if toggle_state:
        print("Script is running.")
        sub = threading.Thread(target=con.subscribe)
        sub.start()     
        startr = threading.Thread(target=trig)
        startr.start()

       
        

        poll()    
        for _ in Threads:
                _.start()
                
        for mic in mics :
         try:
            Console_updater(mic)
            Receiver_updater(mic)
         except error as er:
            print(f'cannot establish connection because of the fatal error, {er}')
        # Restart polling threads or perform any necessary setup
        for mic in mics:
            rec = Receiver(con, mic['receiver_type'], mic['receiver_x32_ch'], mic['receiver_ip'], mic['receiver_ch'],
                            mic['receiver_name'])
            poll = threading.Thread(target=rec.poller)
            poll.start()
        # Restart polling threads or perform any necessary setup
        
    else:
        print("Script is stopped.")
        # Stop or pause polling threads if needed
        # You might need to implement a mechanism to stop the threads gracefully

# Create the main window

switch = threading.Thread(target=toggle_script)
switch.start()

# ... (your existing code)

# Start the main event loop
root.mainloop()