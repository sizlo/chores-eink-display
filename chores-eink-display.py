from eink import EInk
from task_fetcher import TaskFetcher
from tasks_renderer import TasksRenderer
from info_renderer import InfoRenderer
from error_renderer import ErrorRenderer
from util import log

def main():
    log("Setting up Eink")
    eink = EInk()
    log("Setting up Eink - Done")

    try:
        show_overdue_tasks(eink)
    except Exception as error:
        log(f"Got error: {error}")
        show_error(eink, error)

    # TODO - shutdown only if we are currently running via battery, remain on when plugged in to allow ssh-ing in

def show_overdue_tasks(eink):
    log("===== Showing over due tasks =====")

    log("Setting up objects")
    task_fetcher = TaskFetcher()
    tasks_renderer = TasksRenderer(eink)
    info_renderer = InfoRenderer(eink)
    log("Setting up objects - Done")

    log("Fetching tasks")
    tasks = task_fetcher.fetch_overdue_tasks()
    log("Fetching tasks - Done")

    log("Resetting image")
    eink.reset_image()
    log("Resetting image - Done")

    log("Rendering tasks")
    tasks_renderer.render_tasks(tasks)
    log("Rendering tasks - Done")

    log("Rendering info")
    info_renderer.render_info(len(tasks), tasks_renderer.tasks_rendered)
    log("Rendering info - Done")

    log("Updating screen")
    eink.show()
    log("Updating screen - Done")

def show_error(eink, error):
    log("===== Showing error =====")

    log("Setting up objects")
    error_renderer = ErrorRenderer(eink)
    log("Setting up objects - Done")

    log("Resetting image")
    eink.reset_image()
    log("Resetting image - Done")

    log("Rendering error")
    error_renderer.render_error(error)
    log("Rendering error - Done")

    log("Updating screen")
    eink.show()
    log("Updating screen - Done")

if __name__ == "__main__":
    main()
