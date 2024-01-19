import os
import bluetooth

# Simple Bluetooth (bluez) wrapper
class BT():
    # Initialize Bluetooth Connections
    def __init__(self, is_server = False):
        os.system("bluetoothctl discoverable on")
        
        if is_server:
            # Important Bluetooth MAC Address
            mac = [
                # S
                "B8:27:EB:48:52:95", # 0 = Pi 0
                "B8:27:EB:10:0D:19", # 1 = Pi 3 (pihub)
                "DC:A6:32:6B:3A:AB", # 2 = Pi 4
                "98:D3:B1:FE:43:BA", # 3 = Pico (ladybug S)

                # M
                "E4:5F:01:E2:7F:B6", # 4 = Pi 4 (ladybug M)

                # Z
                "DC:A6:32:6E:92:A5", # 5 = Pi 4 (ladybug Z)

                # MISC
                # nothing
            ]

            # Required Devices to connect to
            required = {
                mac[3],
                mac[4],
                mac[5]
            }
            
            # Connect to Clients
            self.clients = 0
            self.pi = []
            for pi in required:
                try:
                    bt = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                    bt.connect((pi, 1))

                    self.pi.append(bt)
                    self.clients += 1
                except:
                    print("Failed to connect to " + pi)

        else:
            # Start Listening
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.bind(("", 1))
            self.sock.listen(1)

            self.client, address = self.sock.accept()

    # Send Message to All Connected Clients
    def send(self, message):
        sent = 0
        for pi in self.pi:
            try:
                pi.send(message)
                sent += 1
            except:
                print("Failed to send message")

        return sent

    # Wait for Message
    def wait_for(self, message):
        data = ""
        while (data != message):            
            data = self.client.recv(128)
            print(data)

    def destroy(self):
        self.client.close()
        self.sock.close()