from ctypes import windll
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import time
hdc = windll.user32.GetDC(0)
tiempo = time.time()
time.sleep(2)
for i in range(1000):
#    a = windll.gdi32.GetPixel(hdc, 1000, 1000)
    press("w", 0.001)
print(time.time() - tiempo)
