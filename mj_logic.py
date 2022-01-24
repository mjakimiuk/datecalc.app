from datetime import datetime, date
import typing


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
