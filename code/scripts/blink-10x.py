import nidaqmx
from nidaqmx.constants import LineGrouping
import time

def send_pulses():
    with nidaqmx.Task() as task:
        # Configure digital output channel
        task.do_channels.add_do_chan("Dev1/port1/line0", line_grouping=LineGrouping.CHAN_PER_LINE)
        
        for _ in range(10):
            # Set pin high
            task.write(True)
            time.sleep(1)
            
            # Set pin low
            task.write(False)
            time.sleep(1)

if __name__ == "__main__":
    send_pulses()