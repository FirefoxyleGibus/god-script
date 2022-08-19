# God script use .gsc

from engine import *
import time

t1 = time.perf_counter()
T = tokenizer("test.gsc")
P = parser()
I = interpreter()
t2 = time.perf_counter()
A = I.exec(P.parse(T.sendData()))
t3 = time.perf_counter()

print("\n\n=========")
print("Data read in {0:.5f}s\nExecuted in {1:.5f}s\nTotal time spent {2:.5f}s".format(t2-t1,t3-t2,t3-t1))
input("Press enter to close the process ... ")
