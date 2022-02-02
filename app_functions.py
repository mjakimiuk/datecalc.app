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
    indexes = list(zip(range(0, 43, 7), range(7, 43, 7)))
    for i, _ in enumerate(months_dictionary):
        date_list = list(calendar.Calendar(
                                          firstweekday=0
                                          ).itermonthdates(2022, i+1)
                         )
        for q in indexes:
            if date_list[q[0]:q[1]]:
                months_dictionary[
                                 list(months_dictionary)[i]
                                  ].append([(
                                            date, 'holiday',
                                            date.isocalendar()[1])
                                            if (
                                            date in country
                                            or
                                            date.weekday() in (6, 5))
                                            else
                                            (date, '', date.isocalendar()[1])
                                            for date
                                            in date_list][q[0]:q[1]])
    return months_dictionary
