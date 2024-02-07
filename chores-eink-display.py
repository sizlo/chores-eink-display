from eink import EInk
from task_fetcher import TaskFetcher
from tasks_renderer import TasksRenderer
from info_renderer import InfoRenderer
from error_renderer import ErrorRenderer
from util import resource_path, shutdown

from PIL import ImageFont

font_size = 32
font = ImageFont.truetype(resource_path("fonts/pixel_operator/PixelOperatorMono-Bold.ttf"), font_size)
minor_font_size = 16
minor_font = ImageFont.truetype(resource_path("fonts/pixel_operator/PixelOperatorMono-Bold.ttf"), minor_font_size)

# These settings are specific to the display resolution, font, and font size
# If any of those change you'll need to experiment to find the right values
left_border = 4
info_text_y = 0
info_separator_y = 18
tasks_start_y = 22
task_line_height = 32
task_separator_offset = 32
task_lines_which_will_fit_on_screen = 13
# This relies on a monospace font
task_characters_per_line = 37

def main():
    eink = EInk(font, minor_font)

    try:
        task_fetcher = TaskFetcher()
        tasks_renderer = TasksRenderer(eink, left_border, tasks_start_y, task_line_height, task_separator_offset, task_lines_which_will_fit_on_screen, task_characters_per_line)
        info_renderer = InfoRenderer(eink, left_border, info_text_y, info_separator_y)

        tasks = task_fetcher.fetch_overdue_tasks()

        eink.reset_image()
        tasks_renderer.render_tasks(tasks)
        info_renderer.render_info(len(tasks), tasks_renderer.tasks_rendered)
        eink.show()
    except Exception as error:
        print(f"Got error: {error}")
        error_renderer = ErrorRenderer(eink, left_border, tasks_start_y, task_line_height, task_characters_per_line)
        eink.reset_image()
        error_renderer.render_error(error)
        eink.show()

    # TODO - shutdown only if we are currently running via battery, remain on when plugged in to allow ssh-ing in

if __name__ == "__main__":
    main()
