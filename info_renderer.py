from util import get_battery_percent, now_as_string
from layout_settings import LayoutSettings

class InfoRenderer:
    def __init__(self, eink):
        self.eink = eink
        self.x = LayoutSettings.left_border
        self.text_y = LayoutSettings.info_text_y

    def render_info(self, total_tasks, tasks_rendered):
        # TODO - Draw as seperate blocks and put a real vertical line seperator between blocks
        info_text = f"Showing {tasks_rendered}/{total_tasks} tasks | Updated at {now_as_string()} | Battery {get_battery_percent()}%"
        self.eink.draw_text((self.x, self.text_y), info_text, minor=True)
        self.eink.draw_full_width_line(LayoutSettings.info_separator_y)
