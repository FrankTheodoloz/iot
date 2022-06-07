from machine import Pin
from time import *

"""
Premiere approche
"""

# p22 = Pin(22, Pin.IN)  # pir sur la patte 22
# while True:
#     print(p22.value())
#     sleep(.5)

"""
Prise en compte du comportement
"""
# p22 = Pin(22, Pin.IN)  # pir sur la patte 22
# print("attente")
# etat = 0
# while True:
#     if (p22.value() != etat):
#         if (p22.value() == 0):
#             print("attente")
#             etat = 0
#             sleep(1)
#         else:
#             print("mouvement")
#             etat = 1
#             sleep(4)

"""
On utilise les interruptions
"""
# p22 = Pin(22, Pin.IN)  # pir sur la patte 22
# mvtInstant = 0
# mvt = 0
#
#
# def actionInterruption(pin):
#     global mvtInstant
#     if (pin.value() == 1):
#         mvtInstant = 1
#     else:
#         mvtInstant = 0
#
#
# p22.irq(trigger=(Pin.IRQ_RISING | Pin.IRQ_FALLING), handler=actionInterruption)
#
# while True:
#     if ((mvt == 0) and (mvtInstant == 1)):
#         print('Mouvement detecte!')
#         mvt = 1
#
#     elif ((mvt == 1) and (mvtInstant == 0)):
#         print('En attente...')
#         mvt = 0
#
#     sleep(.5)

"""
On cree un objet PIR
"""
# class PIR():
#     def __init__(self):
#         self.pin = Pin(22, Pin.IN)
#         self.mvt = 0
#         self.pin.irq(trigger=(Pin.IRQ_RISING | Pin.IRQ_FALLING), handler=self.actionInterruption)
#
#     def actionInterruption(self, pin):
#         if (pin.value() == 1):
#             if (self.mvt == 0):
#                 self.mvt = 1
#         else:
#             if (self.mvt == 1):
#                 self.mvt = 0
#
#     def read(self):
#         return self.mvt
#
#
# pir = PIR()
# while True:
#     print(pir.read())
#     sleep(.5)


"""
On cree un objet PIR avec historique
"""
# class PIR():
#     def __init__(self):
#         self.pin = Pin(22, Pin.IN)
#         self.mvt = 0
#         self.pin.irq(trigger=(Pin.IRQ_RISING | Pin.IRQ_FALLING), handler=self.actionInterruption)
#         self.hist = []
#         self.taille = 5
#
#     def ajoute(self):
#         print(round(time()))
#         self.hist.append(round(time()))
#         if (len(self.hist) > self.taille):
#             self.hist.pop(0)
#
#     def actionInterruption(self, pin):
#         if (pin.value() == 1):
#             if (self.mvt == 0):
#                 self.mvt = 1
#                 self.ajoute()
#         else:
#             if (self.mvt == 1):
#                 self.mvt = 0
#
#     def read(self):
#         return self.mvt
#
#     def histo(self):
#         return self.hist
#
#
# pir = PIR()
# while True:
#     print(pir.histo())
#     sleep(1)
