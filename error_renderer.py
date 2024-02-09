from util import now_as_string
from word_wrapper import WordWrapper
from layout_settings import LayoutSettings, calculate_task_characters_per_line

class ErrorRenderer:
    def __init__(self, eink):
        self.eink = eink
        self.x = LayoutSettings.left_border
        self.y = LayoutSettings.tasks_start_y
        self.characters_per_line = calculate_task_characters_per_line(eink)

    def render_error(self, error):
        self.eink.draw_text((self.x, self.y), f"Error occurred at {now_as_string()}")
        self.y += LayoutSettings.line_height
        error_lines = WordWrapper(str(error), self.characters_per_line).wrap_words()
        for line in error_lines:
            self.eink.draw_text((self.x, self.y), line)
            self.y += LayoutSettings.line_height
