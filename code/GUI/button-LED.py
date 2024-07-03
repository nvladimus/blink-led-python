import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import nidaqmx
from nidaqmx.constants import LineGrouping
import time

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = loadUi('./button.ui', self)
        # Connect the button's clicked signal to the blinkLED method
        self.ui.pushButton.clicked.connect(self.blinkLED)
    
    def blinkLED(self):
        # Blink the LED connected to the NI DAQ USB-6211
        with nidaqmx.Task() as task:
            # Adjust "Dev1/port0/line0" according to your setup
            task.do_channels.add_do_chan("Dev1/port1/line0", line_grouping=LineGrouping.CHAN_PER_LINE)
            
            # Turn LED on
            task.write(True)
            time.sleep(1)
            
            # Turn LED off
            task.write(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())