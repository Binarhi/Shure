from Shure.Shuremic import *
#from Shuremic import *
from Shure.X32Api import *

import threading

# Setup console connection and poll for all channel names
con = Console (X32_IP)


# Subscribe to updates from console
sub = threading.Thread(target=con.subscribe)
sub.start()


# Setup polling for each QLXD receiver in the RX_IP_LIST
for ip in rx_ip_list:
    rec = Receiver(ip, con)
    poll = threading.Thread(target=rec.poller)
    poll.start()