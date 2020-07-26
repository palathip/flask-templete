from datetime import date
import datetime

class DateFormat:
    def periodMontYear():
        today   = date.today()
        result  = today.strftime("%m%y")
        return result

    def periodLastMonth():
        today       = datetime.date.today()
        first       = today.replace(day=1)
        lastMonth   = first - datetime.timedelta(days=1)
        result      = lastMonth.strftime("%m%y")
        return result