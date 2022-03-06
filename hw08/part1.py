from functools import reduce


class Date:
    @staticmethod
    def validate_date(date):
        if type(date) != Date:
            raise ValueError("Income is not date")
        if len(date.date) != 3:
            raise ValueError("Income is not date")
        if date.date[2] < 0:
            raise ValueError("Income is not date")
        if date.date[1] < 1 or date.date[1] > 12:
            raise ValueError("Income is not date")
        if date.date[0] < 1 or \
                date.date[1] in (1, 3, 5, 7, 8, 10, 12) and date.date[0] > 31 or \
                date.date[1] in (4, 6, 9, 11) and date.date[0] > 30 or \
                date.date[0] > 28:
            raise ValueError("Income is not date")

    def __init__(self, date):
        self.date = tuple(int(x) for x in date.split("-") if len(x) != 0)
        Date.validate_date(self)

    def __str__(self):
        return f"{self.date}"

    @classmethod
    def to_long(cls, date):
        if type(date) != cls:
            raise ValueError("Income is not date")
        return reduce(lambda x, y: x + y, date.date)


def try_date(date):
    try:
        testing_date = Date(date)
    except ValueError as ve:
        print(ve)
    else:
        print(testing_date)
        print(Date.to_long(testing_date))


try_date("2-2-2002")
try_date("1-1-0")
try_date("")
try_date("0-0-0")
try_date("1-0-0")
try_date("0-1-0")
try_date("32-1-0")
try_date("29-2-0")
try_date("31-4-0")
try_date("31-13-0")
try_date("31-13-0-123")
