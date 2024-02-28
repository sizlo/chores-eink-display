from util import friendly_date_string, api_url
from layout_settings import LayoutSettings

from datetime import datetime

class InfoRenderer:
    def __init__(self, eink, pisugar):
        self.eink = eink
        self.pisugar = pisugar
        self.x = LayoutSettings.left_border
        self.text_y = LayoutSettings.info_start_y

    def render_info(self, total_tasks, tasks_rendered):
        # TODO - Draw as separate blocks and put a real vertical line seperator between blocks
        info_text = f"{self.pisugar.get_battery_percent()}% | {api_url()} | {friendly_date_string(datetime.now())} | {tasks_rendered}/{total_tasks}"
        self.eink.draw_text((self.x, self.text_y), info_text, minor=True)
        self.eink.draw_full_width_line(LayoutSettings.info_separator_y)
