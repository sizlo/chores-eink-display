from util import now_as_string
from word_wrapper import WordWrapper

class ErrorRenderer:
    def __init__(self, eink, left_border, start_y, line_height, characters_per_line):
        self.eink = eink
        self.x = left_border
        self.y = start_y
        self.line_height = line_height
        self.characters_per_line = characters_per_line

    def render_error(self, error):
        self.eink.draw_text((self.x, self.y), f"Error occurred at {now_as_string()}")
        self.y += self.line_height
        error_lines = WordWrapper(str(error), self.characters_per_line).wrap_words()
        for line in error_lines:
            self.eink.draw_text((self.x, self.y), line)
            self.y += self.line_height
