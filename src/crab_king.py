import alphabot
import time

alphabot = alphabot.AlphaBot()
alphabot.stop()

alphabot.setMotor(20, 20)
alphabot.forward()
time.sleep(1)
alphabot.stop()