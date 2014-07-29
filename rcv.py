'''
rcv is a small module to get input from RC receivers in micropython.
It is based on the code originally posted here:
https://github.com/micropython/micropython/issues/570

The MIT License (MIT)

Copyright (c) 2014 Sebastian Plamauer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import pyb
import gc

class Reciever():
'''This class provides a reader to get input from RC-receivers. Pass a list of Pins on which the channels are connected.'''

    def __init__(self, channels):

        if type(channels) is list:
            self.ch = channels
        else:
            print('pass a list containing pins as argument')

        self.timer = pyb.Timer(2, prescaler=83, period=0x3ffffff)

    def _time_pin(self, pin):

        gc.collect()
        pyb.disable_irq()
        while not pin.value():
            pass
        self.timer.counter(0)
        while pin.value():
            pass
        dt = self.timer.counter()
        pyb.enable_irq()

        return dt

    def get_angle_of_ch(self, ch):
        '''Returns the angle that the receiver is getting on the channel. Pass number of channel as argument.'''
        try:
            pin = self.ch[ch-1]
        except (NameError, IndexError):
            print('only channels 1 to', len(self.ch)+1, 'available')
        
        angle = int((self._time_pin(pin)-1500)/7.5)         # The Formula on this line has to be adjusted for your servo.
        if abs(angle) < 4:
            angle = 0

        return angle
