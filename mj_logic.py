from datetime import datetime, date

def date_from_now_logic(date_str: str) ->str:
    t_delta = ""
    dt = datetime.strptime(date_str, "%Y-%m-%d")

    
    today = datetime.combine(date.today(), datetime.min.time())
    t_delta = str((dt-today).days)
    return t_delta


def today_str_func():
    return datetime.today().date().strftime("%Y-%m-%d")
