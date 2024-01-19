import serial
import time
import bt

bt = bt.BT()

# Wait for Start
bt.wait_for(b'start')
print("Started")

ser = serial.Serial("/dev/ttyS0", 9600, timeout=1)
def send(data):
    ser.write(bytes(str(data), 'utf-8') + b'\n')
    
send('1000')
time.sleep(1)

# Wait for Dance
bt.wait_for(b'dance')
print("Dancing")
send('2000')
time.sleep(1)

# Wait for End
bt.wait_for(b'end')
print("End")
bt.destroy()

ser.close()
print('Serial connection closed.')