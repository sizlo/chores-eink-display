from eink import EInk
from util import resource_path

from PIL import ImageFont

font_size = 32
font = ImageFont.truetype(resource_path("fonts/pixel_operator/PixelOperatorMono-Bold.ttf"), font_size)

# These settings are specific to the display resolution, font, and font size
# If any of those change you'll need to experiment to find the right values
start_y = -2
left_border = 4
line_height = 32
task_lines_per_page = 12
# This relies on a monospace font
characters_per_line = 37

def main():
    eink = EInk()
    task_lines = [
        "-Put bins out",
        "-Do something else which has more wor",
        "ds causing it to line wrap",
        "-Clean downstairs bathroom"
    ]
    show_page(eink, 1, 3, task_lines)

def show_page(eink, current_page, total_pages, task_lines):
    eink.reset_image()
    x = left_border
    y = start_y
    eink.draw.text((x, y), f"Overdue tasks page {current_page}/{total_pages}", eink.BLACK, font=font)
    y += line_height
    # TODO - Add title spacer, and center title?
    for line in task_lines:
        eink.draw.text((x, y), line, eink.BLACK, font=font)
        y += line_height
    eink.show()

if __name__ == "__main__":
    main()
