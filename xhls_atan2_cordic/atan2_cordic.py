import sys
import numpy as np
import math

import matplotlib.pyplot as plt
sys.path.append('/home/xilinx')
from pynq import Overlay
import numpy as np
def cordic_atan2():
    while i <= numSamples:
        regIP.write(0x400, inBuffer0[0])
        regIP.write(0x800,  inBuffer0[1])
        out = regIP.read(0xc00)
        print("IP    cordic_atan2 of atan2(%f / %f) = %f\n"%(inBuffer0[0], inBuffer0[1], out  ))
        print("Numpy cordic_atan2 of atan2(%f / %f) = %f\n"%(inBuffer0[0], inBuffer0[1], math.atan2(j/i)  ))
        print("-----------------------------****---------------------------------")
            


if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")
    ol = Overlay("/home/xilinx/bitstream/cordic_atan2.bit")

    fiSamples = open("input_data.txt", "r+")
    numSamples = 0
    line = fiSamples.readline()
    while line:
        numSamples = numSamples + 1
        line = fiSamples.readline()

    inBuffer0 = allocate(shape=(numSamples,), dtype=np.int32)
    outBuffer0 = allocate(shape=(numSamples,), dtype=np.int32)
    fiSamples.seek(0)
    for i in range(numSamples):
        line = fiSamples.readline()
        inBuffer0[i] = int(line)
    fiSamples.close()

    regIP = ol.top_process_magnitude_0    
    cordic_atan2()
    print("Exit process")