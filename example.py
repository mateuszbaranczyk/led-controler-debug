from flux import FluxLedDevice
import time

device_ip = "192.168.0.102"  
device = FluxLedDevice(device_ip)

def turn_on_device():
    print("Turning on the device...")
    response = device.set_power_state_on()
    time.sleep(1)
    print(f"Device turned ON. Response: {response.hex()}")
    
def turn_off_device():
    print("Turning off the device...")
    response = device.set_power_state_off()
    time.sleep(1)
    print(f"Device turned OFF. Response: {response.hex()}")

print("Getting device status...")
status = device.get_status()
print(f"Status retrieved: {status.hex()}")
time.sleep(1)

turn_on_device()
status = device.get_status()
print(f"Status retrieved: {status.hex()}")
time.sleep(2)

turn_off_device()
status = device.get_status()
print(f"Status retrieved: {status.hex()}")

print("Demo completed.")
