import bt

bt = bt.BT()

bt.wait_for(b'start')

print("Started!")

bt.wait_for(b'dance')

print("Dancing...")

bt.wait_for(b'end')

print("ended")