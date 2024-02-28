from eink import EInk
from pisugar import create_pisugar
from task_fetcher import TaskFetcher
from tasks_renderer import TasksRenderer
from info_renderer import InfoRenderer
from error_renderer import ErrorRenderer
from util import shutdown, require_env
from log import logger

def main():
    logger.info("Setting up Eink")
    eink = EInk()
    logger.info("Setting up Eink - Done")

    logger.info("Setting up PiSugar")
    pisugar = create_pisugar()
    logger.info("Setting up PiSugar - Done")

    try:
        schedule_next_refresh(pisugar)
        show_overdue_tasks(eink, pisugar)
    except Exception as error:
        logger.info(f"Got error: {error}")
        show_error(eink, error)

    if pisugar.is_plugged_in():
        logger.info("Remaining switched on because we are plugged in")
    else:
        logger.info("Shutting down")
        shutdown()

def schedule_next_refresh(pisugar):
    if pisugar.real:
        logger.info("Scheduling next refresh")
        pisugar.ensure_pisugar_and_raspberry_pi_have_correct_current_time()
        pisugar.schedule_next_boot(int(require_env("REFRESH_HOUR")))
        logger.info("Scheduling next refresh - Done")

def show_overdue_tasks(eink, pisugar):
    logger.info("===== Showing over due tasks =====")

    logger.info("Setting up objects")
    task_fetcher = TaskFetcher()
    tasks_renderer = TasksRenderer(eink)
    info_renderer = InfoRenderer(eink, pisugar)
    logger.info("Setting up objects - Done")

    logger.info("Fetching tasks")
    tasks = task_fetcher.fetch_overdue_tasks()
    logger.info("Fetching tasks - Done")

    logger.info("Resetting image")
    eink.reset_image()
    logger.info("Resetting image - Done")

    logger.info("Rendering tasks")
    tasks_renderer.render_tasks(tasks)
    logger.info("Rendering tasks - Done")

    logger.info("Rendering info")
    info_renderer.render_info(len(tasks), tasks_renderer.tasks_rendered)
    logger.info("Rendering info - Done")

    logger.info("Updating screen")
    eink.show()
    logger.info("Updating screen - Done")

def show_error(eink, error):
    logger.info("===== Showing error =====")

    logger.info("Setting up objects")
    error_renderer = ErrorRenderer(eink)
    logger.info("Setting up objects - Done")

    logger.info("Resetting image")
    eink.reset_image()
    logger.info("Resetting image - Done")

    logger.info("Rendering error")
    error_renderer.render_error(error)
    logger.info("Rendering error - Done")

    logger.info("Updating screen")
    eink.show()
    logger.info("Updating screen - Done")

if __name__ == "__main__":
    main()
