from datetime import datetime

def is_running_on_raspberry_pi():
    # TODO actually check the hardware somehow once I have it
    return False

def resource_path(relative):
    return f"/home/resources/{relative}"

def now_as_string():
    return datetime.now().strftime("%m-%d-%Y %H:%M")

def get_battery_percent():
    # TODO
    return 100

def shutdown():
    # TODO
    pass