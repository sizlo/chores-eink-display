from datetime import datetime
import sys
import os

def require_env(key):
    try:
        return os.environ[key]
    except KeyError:
        print(f"Missing required envar: {key}")
        sys.exit(1)

def env(key, default=None):
    try:
        return os.environ[key]
    except KeyError:
        return default

def log(message):
    print(f"{datetime.now().strftime('%m-%d-%Y %H:%M:%S.%f')} - {message}")

def is_running_with_eink_screen():
    return env("DISPLAY_MODE", default="not-eink-screen") == "eink-screen"

def resource_path(relative):
    return f"{require_env('RESOURCES_PATH')}/{relative}"

def api_url():
    return require_env("CHORES_API_URL")

def friendly_date_string(date):
    return date.strftime("%m-%d-%Y %H:%M")

def shutdown():
    # TODO
    pass
