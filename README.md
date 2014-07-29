micropython-rcv
===============

Module rcv
----------

micropython-rcv is a micropython module to get input from RC receivers.

### Wiring the receiver to the pyboard

Connect the signal pin of the channel you want to use to an input pin on the pyboard.

### Quickstart

Example:
```python
import pyb
from rcv import Receiver
pin_ch1 = pyb.Pin.board.X1
rcv = Receiver([pin_ch1])
angle = rcv.get_angle_of_ch[1]
print(angle)
```

Classes
-------
``Receiver``  
This class provides a reader to get input from RC-receivers. Pass a list of pins on which the channels are connected.  
![UML diagramm](https://raw.githubusercontent.com/turbinenreiter/micropython-rcv/master/classes_Reciever.png "UML diagramm")

Methods
--------------


``get_angle_of_ch(ch)``  
Returns the angle the Receiver sends on ch.

Instance variables
------------------
``ch_list``  
List of pins on which channels are connected.
