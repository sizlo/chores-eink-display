from datetime import datetime
import sys
import os

def is_running_on_raspberry_pi():
    # TODO actually check the hardware somehow once I have it
    return False

def resource_path(relative):
    return f"/home/resources/{relative}"

def api_url():
    try:
        return os.environ["CHORES_API_URL"]
    except KeyError:
        print("Missing required envar: CHORES_API_URL")
        sys.exit(1)

def now_as_string():
    return datetime.now().strftime("%m-%d-%Y %H:%M")

def get_battery_percent():
    # TODO
    return 100

def shutdown():
    # TODO
    pass