import socket

class FluxLedDevice:
    def __init__(self, ip, port=5577):
        self.ip = ip
        self.port = port

    def _send_data(self, data):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((self.ip, self.port))
                print(f"Connected to {self.ip}:{self.port}")
                
                s.send(data)
                print(f"Sent data: {data.hex()}")
                
                response = s.recv(1024)
                print(f"Received response: {response.hex()}")
                
                return response
            
            except Exception as e:
                print(f"Error: {e}")
                return None

    def get_status(self):
        status_request = bytes([0x81, 0x8A, 0x8B, 0x96])
        return self._send_data(status_request)

    def set_state(self, state_data):
        return self._send_data(state_data)

    def set_power_state_on(self):
        on_data = bytes([0x71, 0x23, 0x0F, 0xA3])
        return self._send_data(on_data)

    def set_power_state_off(self):
        off_data = bytes([0x71, 0x24, 0x0F, 0xA4])
        return self._send_data(off_data)

