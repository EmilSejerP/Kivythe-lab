from datetime import datetime, date

class TimeScript:

    def __init__(self):
        self.time = datetime.now()
        self.month = datetime.now().month
        self.year = datetime.now().year

    def get_current_time(self):
        return self.time

    def get_day_amount(self):
        return (date(self.year, self.month + 1 ,1) - date(self.year,self.month,1)).days
