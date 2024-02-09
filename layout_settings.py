from util import resource_path

class LayoutSettings:
    font_path = resource_path("fonts/pixel_operator/PixelOperatorMono-Bold.ttf")
    font_size = 32
    minor_font_size = 16

    # These settings are specific to the font and font sizes, if those change these will need to be updated
    left_border = 4
    info_text_y = 0
    info_separator_y = 18
    tasks_start_y = 22
    task_line_height = 32
    task_separator_offset = 32
    task_character_width = 16  # This relies on a monospace font

def calculate_task_characters_per_line(eink):
    return (eink.display.width - LayoutSettings.left_border) // LayoutSettings.task_character_width

def calculate_task_lines_that_will_fit_on_screen(eink):
    return (eink.display.height - LayoutSettings.tasks_start_y) // LayoutSettings.task_line_height
