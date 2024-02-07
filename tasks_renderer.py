from word_wrapper import WordWrapper

class TasksRenderer:
    def __init__(self, eink, left_border, start_y, line_height, separator_offset, max_lines, characters_per_line):
        self.eink = eink
        self.x = left_border
        self.y = start_y
        self.line_height = line_height
        self.separator_offset = separator_offset
        self.lines_left = max_lines
        self.characters_per_line = characters_per_line
        self.tasks_rendered = 0

    def render_tasks(self, tasks):
        for task in tasks:
            self.render_task(task)
            if self.lines_left > 0:
                self.render_seperator()
            else:
                break

    def render_task(self, task):
        lines = WordWrapper(task.name, self.characters_per_line).wrap_words()
        for i in range(0, len(lines)):
            line = lines[i]
            is_last_line_of_task = i == len(lines) - 1

            if self.lines_left == 1 and not is_last_line_of_task:
                line = self.add_ellipsis(line)

            self.eink.draw_text((self.x, self.y), line)
            self.y += self.line_height
            self.lines_left -= 1
            if self.lines_left <= 0:
                break

        self.tasks_rendered += 1

    def add_ellipsis(self, line):
        characters = list(line)
        characters[-2] = "."
        characters[-3] = "."
        if characters[-4] == " ":
            characters[-4] = "."
            characters = characters[:-1]
        else:
            characters[-1] = "."
        return "".join(characters)

    def render_seperator(self):
        self.eink.draw_full_width_line(self.y - self.line_height + self.separator_offset)
