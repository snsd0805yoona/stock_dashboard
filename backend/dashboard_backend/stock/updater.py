from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .task import update_stock


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_stock, "interval", minutes=1)
    scheduler.start()
