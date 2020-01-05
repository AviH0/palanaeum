import datetime
import re


class Student:

    def __init__(self, row, index, stu=None):
        if stu:
            self.timestamp = stu.timestamp
            self.name = stu.name
            self.topic = stu.topic
            self.status = stu.status
            self.index = stu.index
        else:
            self.timestamp = row[0]
            self.name = str(row[1]).encode(encoding='cp424', errors='replace').decode(encoding='cp424',
                                                                                      errors='replace')
            self.topic = str(row[2]).encode(encoding='cp424', errors='replace').decode(encoding='cp424',
                                                                                       errors='replace')
            self.time_made_orange = row[3]
            self.status = None
            if len(row) > 4:
                self.status = row[4]
            self.index = index

    def should_be_red(self):
        if not self.time_made_orange:
            return False
        date_pattern = '(\d+)/(\d+)/(\d+)'
        date_result = re.search(date_pattern, self.timestamp)
        time_made_orange = self.time_made_orange.split(':')
        hours = int(time_made_orange[0].zfill(2))
        minutes = int(time_made_orange[1].zfill(2))
        if len(time_made_orange) > 2 and time_made_orange[2][-2:] == 'PM':
            hours += 12
        time_made_orange = datetime.datetime.now().replace(day=int(date_result.group(2)),
                                                           month=int(date_result.group(1)),
                                                           year=int(date_result.group(3)), hour=hours,
                                                           minute=minutes)
        return datetime.datetime.now().timestamp() - time_made_orange.timestamp() > 60 * 30
