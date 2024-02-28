from eink import EInk
from pisugar import create_pisugar
from task_fetcher import TaskFetcher
from tasks_renderer import TasksRenderer
from info_renderer import InfoRenderer
from error_renderer import ErrorRenderer
from util import log, shutdown, require_env

def main():
    log("Setting up Eink")
    eink = EInk()
    log("Setting up Eink - Done")

    log("Setting up PiSugar")
    pisugar = create_pisugar()
    log("Setting up PiSugar - Done")

    try:
        schedule_next_refresh(pisugar)
        show_overdue_tasks(eink, pisugar)
    except Exception as error:
        log(f"Got error: {error}")
        show_error(eink, error)

    if pisugar.is_plugged_in():
        log("Remaining switched on because we are plugged in")
    else:
        log("Shutting down")
        shutdown()

def schedule_next_refresh(pisugar):
    if pisugar.real:
        log("Scheduling next refresh")
        pisugar.ensure_pisugar_and_raspberry_pi_have_correct_current_time()
        pisugar.schedule_next_boot(int(require_env("REFRESH_HOUR")))
        log("Scheduling next refresh - Done")

def show_overdue_tasks(eink, pisugar):
    log("===== Showing over due tasks =====")

    log("Setting up objects")
    task_fetcher = TaskFetcher()
    tasks_renderer = TasksRenderer(eink)
    info_renderer = InfoRenderer(eink, pisugar)
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
