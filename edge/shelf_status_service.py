import time
from shelf_vision_service import detect_shelf_status

last_status = None

while True:
    status = detect_shelf_status()
    if status != last_status:
        print(f"[STATUS CHANGE] Shelf is now: {status}")
        # Simulate sending to cloud
        with open("event.txt", "w") as f:
            f.write(status)
        last_status = status
    time.sleep(5)
