from util import resource_path

class LayoutSettings:
    font_path = resource_path("fonts/pixel_operator/PixelOperatorMono-Bold.ttf")
    font_size = 32
    minor_font_size = 16

    orientation = "portrait"

    # These settings are specific to the font and font sizes, if those change these will need to be updated
    left_border = 4
    info_text_y = 0
    info_separator_y = 18
    line_height = 32
    minor_line_height = 16
    tasks_start_y = 22
    above_task_separator_padding = 2
    task_character_width = 16  # This relies on a monospace font

def calculate_task_characters_per_line(eink):
    return (eink.width - LayoutSettings.left_border) // LayoutSettings.task_character_width
