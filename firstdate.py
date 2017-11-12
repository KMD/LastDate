import calendar


class IncorrectInputString(Exception):
    def __str__(self):
        return "Incorrect input data string format"


class FirstDate:
    def __init__(self, date):
        """
        Sets day,mounth and year
        :param date: string with date ex: '3/4/7'
        """

        # there is no '/' in input string
        if(date.find('/') == -1):
            raise IncorrectInputString()

        date_array = date.split("/")

        # there is more or less "/" than 2
        if len(date_array) is not 3:
            raise IncorrectInputString()

        # things between "/" are not integers
        try:
            self.a = int(date_array[0])
            self.b = int(date_array[1])
            self.c = int(date_array[2])
        except ValueError:
            raise IncorrectInputString()

        # can be only one 0 (for year)
        if (self.a == 0 and self.b == 0):
            raise IncorrectInputString()
        if (self.a == 0 and self.c == 0):
            raise IncorrectInputString()
        if (self.c == 0 and self.b == 0):
            raise IncorrectInputString()

        self.set_year()
        self.set_mounth()
        self.set_day()

    def set_year(self):
        if self.a > 1999 and self.a < 3000:
            self.year = self.a
            self.day_and_mounth = [self.b, self.c]
        elif self.b > 1999 and self.a < 3000:
            self.year = self.b
            self.day_and_mounth = [self.a, self.c]
        elif self.c > 1999 and self.a < 3000:
            self.year = self.c
            self.day_and_mounth = [self.a, self.b]
        else:
            self.year = min([self.a, self.b, self.c])
            self.day_and_mounth = [self.a, self.b, self.c]
            self.day_and_mounth.remove(self.year)
            self.year = self.year + 2000
            if self.year < 2000 or self.year > 2999:
                raise IncorrectInputString

    def set_mounth(self):
        self.mounth = min(self.day_and_mounth)
        if self.mounth == 0 or self.mounth > 12:
            raise IncorrectInputString()

    def set_day(self):
        self.day_and_mounth.remove(self.mounth)
        self.day = self.day_and_mounth[0]
        if self.day == 0:
            raise IncorrectInputString()
        if self.day > calendar.monthrange(self.year, self.mounth)[1]:
            raise IncorrectInputString()

    def __str__(self):
        return "%d-%02d-%02d" % (self.year, self.mounth, self.day)
