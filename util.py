import sys
import os
import subprocess

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

def is_running_with_eink_screen():
    return env("DISPLAY_MODE", default="not-eink-screen") == "eink-screen"

def resource_path(relative):
    return f"{require_env('RESOURCES_PATH')}/{relative}"

def api_url():
    return require_env("CHORES_API_URL")

def remove_protocol(url):
    return url.split("//")[1]

def friendly_date_string(date):
    return date.strftime("%m-%d-%Y %H:%M")

def shutdown():
    subprocess.run(["sudo", "shutdown", "now"])
