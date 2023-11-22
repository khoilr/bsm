from datetime import datetime

SCHEDULE_TIME = datetime.today().replace(hour=18, minute=30, second=0).timestamp()
print(SCHEDULE_TIME)