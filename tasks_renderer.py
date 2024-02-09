from word_wrapper import WordWrapper
from layout_settings import LayoutSettings, calculate_task_characters_per_line

class TasksRenderer:
    def __init__(self, eink):
        self.eink = eink
        self.x = LayoutSettings.left_border
        self.y = LayoutSettings.tasks_start_y
        self.characters_per_line = calculate_task_characters_per_line(eink)
        self.tasks_rendered = 0

    def render_tasks(self, tasks):
        for task in tasks:
            self.render_task(task)
            self.render_seperator()
            if self.number_of_further_task_lines_that_will_fit() <= 0:
                break

    def render_task(self, task):
        lines = WordWrapper(task.name, self.characters_per_line).wrap_words()
        for i in range(0, len(lines)):
            line = lines[i]
            is_last_line_of_task = i == len(lines) - 1

            if self.number_of_further_task_lines_that_will_fit() == 1 and not is_last_line_of_task:
                line = self.add_ellipsis(line)

            self.eink.draw_text((self.x, self.y), line)
            self.y += LayoutSettings.line_height
            if self.number_of_further_task_lines_that_will_fit() <= 0:
                break

        if self.can_fit_a_minor_line():
            self.eink.draw_text((self.x, self.y), task.overdue_text, minor=True)
            self.y += LayoutSettings.minor_line_height

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

    def number_of_further_task_lines_that_will_fit(self):
        return (self.eink.height - self.y) // LayoutSettings.line_height

    def can_fit_a_minor_line(self):
        return (self.eink.height - self.y) >= LayoutSettings.minor_line_height

    def render_seperator(self):
        self.y += LayoutSettings.above_task_separator_padding
        if self.number_of_further_task_lines_that_will_fit() > 0:
            self.eink.draw_full_width_line(self.y)
