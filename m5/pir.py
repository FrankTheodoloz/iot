from machine import Pin


class PIR():
    def __init__(self):
        self.pin = Pin(22, Pin.IN)
        self.mvt = 0
        self.pin.irq(trigger=(Pin.IRQ_RISING | Pin.IRQ_FALLING), handler=self.actionInterruption)

    def actionInterruption(self, pin):
        if (pin.value() == 1):
            if (self.mvt == 0):
                self.mvt = 1
        else:
            if (self.mvt == 1):
                self.mvt = 0

    def read(self):
        return self.mvt

# pir = PIR()
# while True:
#     print(pir.read())
#     sleep(.5)

