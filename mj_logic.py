from datetime import datetime, date

def days_from_now_logic(date_str: str) -> int:
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.combine(date.today(), datetime.min.time())
        return (dt-today).days
    except ValueError:
        return 'error'
    

def today_str_func():
    return datetime.today().date().strftime("%Y-%m-%d")

def week_dates_logic(year: str,week: str) -> str:
    try:
        d = f"{year}-W{week}"
        r = datetime.strptime(d + '-1', "%Y-W%W-%w")
        q = datetime.strptime(d + '-0', "%Y-W%W-%w")
        return r.date().strftime("%d/%m/%Y"),q.date().strftime("%d/%m/%Y")
    except ValueError:
        return ('error','error')