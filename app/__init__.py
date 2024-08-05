import time
from multiprocessing import Process

from celery.signals import worker_init, worker_shutdown
from app.logs import get_logger

from . import tasks
from .setup import app

logger = get_logger()


def process_test():
    while True:
        time.sleep(1)
        logger.info("logger.info ---------------Process test")


@worker_init.connect
def init_worker(**kwargs):
    global test_process
    print("------------------------Worker init")
    test_process = Process(target=process_test)
    test_process.start()


@worker_shutdown.connect
def shutdown_worker(**kwargs):
    test_process.terminate()
    test_process.join()
    print("------------------------Worker shutdown")
