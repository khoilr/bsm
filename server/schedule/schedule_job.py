
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


class ScheduleManager:
    _schedule = BlockingScheduler()
    _jobs = []

    def __init__(self):
        pass

    def addNewJob(self, func, scheduleTime: datetime, args: list[str] = []):
        self._jobs.append({
            'function': func,
            'args': args,
            'time': scheduleTime,
        })

    def start(self):
        for job in self._jobs:
            self._schedule.add_job(func=job['function'], trigger='date', run_date=job['time'], args=job['args'])
        self._schedule.start()

