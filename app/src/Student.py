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
            self.name = row[1]
            self.topic = row[2]
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
        time_made_orange = datetime.datetime.now().replace(day=int(date_result.group(2)), month=int(date_result.group(1)),
                                  year=int(date_result.group(3)), hour=int(self.time_made_orange[:2]),
                                  minute=int(self.time_made_orange[3:]))
        return datetime.datetime.now().timestamp() - time_made_orange.timestamp() > 60*30

