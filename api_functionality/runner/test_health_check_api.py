import requests
import ctypes



def test_get_health_ready():
        health_api = requests.get("http://localhost:9000/health")
        if health_api.text == '"status":"Ok':
              message_box = ctypes.windll.user32.MessageBoxW
              return_box = message_box(None, "API health status is OK, ","Disney API", 0x40 | 0x0)
        else:
              message_box = ctypes.windll.user32.MessageBoxW
              return_box = message_box(None, "API health status is not ok","Disney API", 0x40 | 0x0)
test_get_health_ready()
