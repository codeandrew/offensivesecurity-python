import bluetooth

"""
# ====================================
# PRE-REQUISITES
sudo apt install -y \
    libbluetooth-dev \
    python-dev

# THIS USSUALLY HAS ERRORS
# pip3 install pybluez

# So manually install it by source code
wget https://github.com/pybluez/pybluez/archive/master.tar.gz
tar -xzvf master.tar.gz
cd pybluez-master
# This requires sudo because of  hardware interaction
sudo python3 setup.py install

# ====================================
# USAGE
╰─$ python3 bluetooth-enum.py
Scanning for Bluetooth devices...
Found 2 devices.
    Address: 30:03:C8:2F:8E:E2, Name: SONY KD-75X80K
    Address: 04:7A:0B:0B:84:CD, Name: Mi Soundbar
    [('30:03:C8:2F:8E:E2', 'SONY KD-75X80K'), ('04:7A:0B:0B:84:CD', 'Mi Soundbar')]
Connecting to AV Remote Control Target on 30:03:C8:2F:8E:E2...
Could not connect: [Errno 111] Connection refused
"""


class BluetoothEnumerator:
    def __init__(self):
        # Initialize any necessary attributes
        pass

    def scan_for_devices(self):
        """Scans for nearby Bluetooth devices."""
        print("Scanning for Bluetooth devices...")
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        
        if not nearby_devices:
            print("No devices found.")
            return []

        print(f"Found {len(nearby_devices)} devices.")
        devices = []
        for addr, name in nearby_devices:
            print(f"  Address: {addr}, Name: {name}")
            devices.append((addr, name))
        return devices

    def connect_to_device(self, address):
        """Attempts to connect to a Bluetooth device."""
        service_matches = bluetooth.find_service(address=address)
        
        if not service_matches:
            print("No services found for the device.")
            return False

        first_match = service_matches[0]
        port = first_match["port"]
        name = first_match["name"]
        host = first_match["host"]

        print(f"Connecting to {name} on {host}...")
        
        # Create the client socket
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            sock.connect((host, port))
            print("Connected successfully.")
            return True
        except bluetooth.BluetoothError as e:
            print(f"Could not connect: {e}")
            return False
        finally:
            sock.close()

# Usage
if __name__ == "__main__":
    enumerator = BluetoothEnumerator()
    devices = enumerator.scan_for_devices()
    print(devices)

    # Connect to the first found device
    if devices:
        address = devices[0][0]
        enumerator.connect_to_device(address)
