from typing import Callable, List, Dict, Any
from datetime import datetime, date, timedelta
from calendar import Calendar, month_name
import typing
import holidays
from dateutil.relativedelta import *

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


def calendar_holiday(year: int,
                     country: Callable = holidays.US()
                     ) -> Dict[str, List[Any]]:
    WEEKEND = (5, 6)  # (Saturday, Sunday)
    months_tuple: List = [(month_name[i], []) for i in range(1, 13)]
    months_dictionary = dict(months_tuple)
    indexes = [(i, i+7) for i in range(0, 42, 7)]
    for month, _ in enumerate(months_dictionary, start=1):
        date_list = list(Calendar(firstweekday=0
                                  ).itermonthdates(year, month)
                         )
        for index_range in indexes:
            if date_list[index_range[0]:index_range[1]]:
                data_tuple = [(date, 'holiday', date.isocalendar()[1],
                              date.strftime("%B"))
                              if (date in country or date.weekday() in WEEKEND)
                              else (date, '', date.isocalendar()[1],
                              date.strftime("%B"))
                              for date
                              in date_list][index_range[0]:index_range[1]]
                months_dictionary[list(months_dictionary)[month-1]
                                  ].append(data_tuple)
    return months_dictionary


def date_calculator_function(input_data):
    datetime_obj = datetime.strptime(input_data[0], "%Y-%m-%d")
    operator = input_data[1]
    td_days = 0 if input_data[5] == None else int(input_data[5])
    td_weeks = 0 if input_data[4] == None else int(input_data[4])
    td_months = 0 if input_data[3] == None else int(input_data[3])
    td_years = 0 if input_data[2] == None else int(input_data[2])
    tdelta = relativedelta(years=td_years, months=td_months,
                           weeks=td_weeks, days=td_days)
    if operator == 'option_add':
        result = datetime_obj + tdelta
    elif operator == "option_substract":
        result = datetime_obj - tdelta
    return result.strftime("%d-%m-%Y")
