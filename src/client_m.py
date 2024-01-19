import alphabot
import bt
import time

alphabot = alphabot.AlphaBot()
alphabot.stop()

def dance(speed = 60): # arduinoSpeed/250*100
    for i in range(2):
        alphabot.setMotor(speed, speed) # elore
        time.sleep(1)

        alphabot.setMotor(0, speed) # balra kor
        time.sleep(1)

        alphabot.setMotor(speed, 0) # jobbra kor
        time.sleep(1)

        alphabot.setMotor(-speed, -speed) # hatra
        time.sleep(1)

        alphabot.setMotor(0, speed) # balra kor
        time.sleep(1)

        alphabot.setMotor(speed, 0) # jobbra kor
        time.sleep(1)

        alphabot.setMotor(speed, speed) # elore
        time.sleep(1)

        alphabot.setMotor(-speed, -speed)  # hatra
        time.sleep(1)

    alphabot.setMotor(speed, speed) # elore
    time.sleep(1)

    alphabot.setMotor(0, speed) # balra kor
    time.sleep(1)

    alphabot.setMotor(speed, 0) # jobbra kor
    time.sleep(1)

    alphabot.setMotor(-speed, -speed) # hatra
    time.sleep(1)

    alphabot.stop()

# Init Bluetooth Communication
bt = bt.BT()

# Wait for Start
bt.wait_for(b'start')
time.sleep(1.6)
alphabot.forward()
time.sleep(1.3)
alphabot.stop()

# Wait for Dance
bt.wait_for(b'dance')
dance(60)

# Wait for End
bt.wait_for(b'end')
bt.destroy()