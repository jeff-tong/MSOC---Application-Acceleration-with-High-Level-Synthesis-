import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append('/home/xilinx')
from pynq import Overlay
import numpy as np
def square_diff():
    while i <= 9:
        print("--**--")
        while j <= 9:
            regIP.write(0x400, i)
            regIP.write(0x800, j )
            out = regIP.read(0xc00)
            print("yours (%f - %f)^2= %f\n"%(i, j, out  ))
            print("golds (%f - %f)^2= %f\n"%(i, j, (i-j)**2  ))
            print("--**--")
            


if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")
    ol = Overlay("/home/xilinx/bitstream/Square_diff.bit")
    regIP = ol.top_process_magnitude_0    
    square_diff()
    print("Exit process")