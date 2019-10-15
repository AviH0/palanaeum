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
            if len(row)>4:
                self.status = row[4]
            self.index = index

