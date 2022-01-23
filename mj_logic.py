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
