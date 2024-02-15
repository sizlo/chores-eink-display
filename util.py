from datetime import datetime
import sys
import os

def require_env(key):
    try:
        return os.environ[key]
    except KeyError:
        print(f"Missing required envar: {key}")
        sys.exit(1)

def log(message):
    print(f"{datetime.now().strftime('%m-%d-%Y %H:%M:%S.%f')} - {message}")

def is_running_with_eink_screen():
    try:
        return os.environ["DISPLAY_MODE"] == "eink-screen"
    except KeyError:
        return False

def resource_path(relative):
    return f"{require_env('RESOURCES_PATH')}/{relative}"

def api_url():
    return require_env("CHORES_API_URL")

def now_as_string():
    return datetime.now().strftime("%m-%d-%Y %H:%M")

def get_battery_percent():
    # TODO
    return 100

def shutdown():
    # TODO
    pass