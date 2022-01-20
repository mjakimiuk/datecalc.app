from flask import Flask, request, render_template
from datetime import datetime, date

from mj_logic import date_from_now_logic, today_str_func

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/date_from_now", methods=['GET','POST'])
def date_from_now():
    name = ""
    today_str = today_str_func()
    if request.method == "POST" and "input_date" in request.form:
        name = request.form.get("input_date")
        name = date_from_now_logic(name)
    return render_template("date_from_now.html",
                            name = name,
                            today_str = today_str)


@app.route("/week_dates", methods=['GET','POST'])
def week_dates():
    today_str = today_str_func()
    return render_template("week_dates.html",
                            today_str = today_str)


@app.route("/holiday_planner")
def holiday_planner():
    return render_template("holiday_planner.html")