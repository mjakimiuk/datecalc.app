from datetime import datetime, date
import typing
import holidays
import calendar


def days_from_now_logic(date_str: str) -> str:
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.combine(date.today(), datetime.min.time())
        return str((dt-today).days)
    except ValueError:
        return 'error'


def week_dates_logic(year: str, week: str) -> typing.Tuple[str, str]:
    const_1 = "%Y-W%W-%w"
    const_2 = "%d/%m/%Y"
    try:
        week_str = f"{year}-W{week}"
        range_1 = datetime.strptime(week_str + '-1', const_1)
        range_2 = datetime.strptime(week_str + '-0', const_1)
        return (range_1.date().strftime(const_2),
                range_2.date().strftime(const_2))
    except ValueError:
        return ('error', 'error')


def calendar_holiday(year, country=holidays.US()):
    cal_generator = []
    months_dictionary = {"January": [],
                         "February": [],
                         "March": [],
                         "April": [],
                         "May": [],
                         "June": [],
                         "July": [],
                         "August": [],
                         "September": [],
                         "October": [],
                         "November": [],
                         "December": []
                         }

    for i in range(1, 13):
        (cal_generator.
         append(calendar.Calendar(firstweekday=0).itermonthdates(year, i)))

    for d_key, i in zip(months_dictionary.keys(), cal_generator):
        for y in i:
            if y in country or y.weekday() == 6 or y.weekday() == 5:
                (months_dictionary[d_key].
                 append((y, 'holiday', y.isocalendar()[1])))
            else:
                months_dictionary[d_key].append((y, '', y.isocalendar()[1]))
    return months_dictionary
