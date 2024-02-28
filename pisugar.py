from log import logger

import subprocess
from datetime import datetime, timedelta, timezone

class PiSugar:
    def __init__(self):
        self.real = True
        self.url = "127.0.0.1"
        self.port = 8423

    def get_model(self):
        return self.run_command("get model")

    def get_battery_percent(self):
        return int(float(self.run_command("get battery")))

    def is_plugged_in(self):
        return self.parse_bool(self.run_command("get battery_power_plugged"))

    def ensure_pisugar_and_raspberry_pi_have_correct_current_time(self):
        self.run_command("rtc_web")

    def schedule_next_boot(self, hour):
        now = datetime.now(tz=timezone.utc)
        next_boot = datetime(year=now.year, month=now.month, day=now.day, hour=hour, minute=0, tzinfo=timezone.utc)
        next_boot_str = next_boot.isoformat()
        repeat = 127 # 1111111 in binary, each bit is a day of the week, all are enabled
        self.run_command(f"rtc_alarm_set {next_boot_str} {repeat}")

    def run_command(self, command):
        result = subprocess.run(
            ["nc", "-q", "0", self.url, f"{self.port}"],
            input=command,
            capture_output=True,
            text=True,
        )
        full_output = result.stdout
        if "invalid request" in full_output.lower():
            raise Exception(f"Error running pisugar command: {command}")
        return full_output.split(":")[-1].strip()

    def parse_bool(self, text):
        if text.lower() == "true":
            return True
        elif text.lower() == "false":
            return False
        elif int(text) != 0:
            return True
        else:
            return False


class MockPiSugar:
    def __init__(self):
        self.real = False

    def get_model(self):
        return "MockPiSugar"

    def get_battery_percent(self):
        return 999

    def is_plugged_in(self):
        return True

    def ensure_pisugar_and_raspberry_pi_have_correct_current_time(self):
        pass

    def schedule_next_boot(self, hour):
        pass

    def get_next_boot_time(self):
        return datetime.now() + timedelta(hours=1)

def create_pisugar():
    try:
        real_pisugar = PiSugar()
        real_pisugar.get_model()
        return real_pisugar
    except:
        logger.info("Could not get PiSugar model, using MockPiSugar")
        return MockPiSugar()
