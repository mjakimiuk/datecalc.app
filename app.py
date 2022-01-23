from flask import Flask, request, render_template
from datetime import datetime, date

from mj_logic import days_from_now_logic, today_str_func, week_dates_logic

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/days_from_now", methods=['GET','POST'])
def days_from_now():
    name = ""
    today_str_txt = today_str_func()
    today_str = today_str_func()
    if request.method == "POST" and "input_date" in request.form:
        name = request.form.get("input_date")
        name = days_from_now_logic(name)
        today_str = request.form.get("input_date")
    
    return render_template("days_from_now.html",
                            name = name,
                            today_str = today_str,
                            today_str_txt = today_str_txt)


@app.route("/week_dates", methods=['GET','POST'])
def week_dates():
    today_str = today_str_func()
    date_1 = ""
    date_Year = ""
    date_Week = ""
    date_2 = ""
    
    if request.method == "POST" and "input_Year" in request.form and "input_Week" in request.form:
        date_Year = request.form.get("input_Year")
        date_Week = request.form.get("input_Week")
        date_1 = week_dates_logic(date_Year,date_Week)[0]
        date_2 = week_dates_logic(date_Year,date_Week)[1]

    return render_template("week_dates.html",
                            today_str = today_str,
                            date_1 = date_1,
                            date_2 = date_2)


@app.route("/holiday_planner")
def holiday_planner():
    return render_template("holiday_planner.html")