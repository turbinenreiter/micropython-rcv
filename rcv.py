import pyb
import gc

class Reciever():
'''This class provides a reader to get input from RC-recievers. Pass a list of Pins on which the channels are connected.'''

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
        '''Returns the angle that the recievers is getting on the channel. Pass number of channel as argument.'''
        try:
            pin = self.ch[ch-1]
        except (NameError, IndexError):
            print('only channels 1 to', len(self.ch)+1, 'available')
        
        angle = int((self._time_pin(pin)-1500)/7.5)
        if abs(angle) < 4:
            angle = 0
        return angle