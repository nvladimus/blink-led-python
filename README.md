# Blinking an LED with NI DAQ board and minimal python code

# Requirements
## Software
- Python >= 3.7 such as [Anaconda](https://www.anaconda.com/download)
- IDE such as [Visual Studio Code](https://code.visualstudio.com/download)
- [QtDesigner](https://build-system.fman.io/qt-designer-download)
- NI DAQmx [drivers](https://www.ni.com/en/support/downloads/drivers/download.ni-daq-mx.html)
- tested on Windows 10, other OS todo

# Hardware
- any NI DAQ board compatible with your computer (we will use NI USB-6211 just because we have it)
- a small 5-mm LED of any color (fordward voltage up to 5V, current ~20 mA)

# Software installation
- after installing Anaconda, open the Anaconda prompt and type
  ```
  conda create -n daq-python python=3.7
  conda activate daq-python
  git clone https://github.com/nvladimus/blink-led-python.git
  cd blink-led-python
  ```
- install the dependencies
```
pip install requirements.txt
```
