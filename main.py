# God script use .gsc

from engine import *

T = tokenizer("test.gsc")
P = parser()
I = interpreter()

A = I.exec(P.parse(T.sendData()))
