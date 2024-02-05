def is_running_on_raspberry_pi():
    # TODO actually check the hardware somehow once I have it
    return False

def resource_path(relative):
    return f"/home/resources/{relative}"
