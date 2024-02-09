from eink import EInk
from task_fetcher import TaskFetcher
from tasks_renderer import TasksRenderer
from info_renderer import InfoRenderer
from error_renderer import ErrorRenderer

def main():
    eink = EInk()

    try:
        show_overdue_tasks(eink)
    except Exception as error:
        print(f"Got error: {error}")
        show_error(eink, error)

    # TODO - shutdown only if we are currently running via battery, remain on when plugged in to allow ssh-ing in

def show_overdue_tasks(eink):
    task_fetcher = TaskFetcher()
    tasks_renderer = TasksRenderer(eink)
    info_renderer = InfoRenderer(eink)

    tasks = task_fetcher.fetch_overdue_tasks()

    eink.reset_image()
    tasks_renderer.render_tasks(tasks)
    info_renderer.render_info(len(tasks), tasks_renderer.tasks_rendered)
    eink.show()

def show_error(eink, error):
    error_renderer = ErrorRenderer(eink)
    eink.reset_image()
    error_renderer.render_error(error)
    eink.show()

if __name__ == "__main__":
    main()
