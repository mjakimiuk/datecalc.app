from distutils.log import debug
from flask import Flask, request, render_template
from datetime import date
import holidays

from app_functions import (days_from_now_logic,
                           week_dates_logic, calendar_holiday,
                           date_calculator_function)


app = Flask(__name__)


TODAY = str(date.today())
TODAY_int = date.today().year
YEARS = [str(i) for i in range(TODAY_int, TODAY_int + 20)]

COUNTRIES = {"Angola": getattr(holidays, 'AO'),
             "Argentina": getattr(holidays, 'AR'),
             "Aruba": getattr(holidays, 'AW'),
             "Australia": getattr(holidays, 'AU'),
             "Austria": getattr(holidays, 'AT'),
             "Azerbaijan": getattr(holidays, 'AZ'),
             "Bangladesh": getattr(holidays, 'BD'),
             "Belarus": getattr(holidays, 'BY'),
             "Belgium": getattr(holidays, 'BE'),
             "Botswana": getattr(holidays, 'BW'),
             "Brazil": getattr(holidays, 'BR'),
             "Bulgaria": getattr(holidays, 'BG'),
             "Burundi": getattr(holidays, 'BI'),
             "Canada": getattr(holidays, 'CA'),
             "Chile": getattr(holidays, 'CL'),
             "China": getattr(holidays, 'CN'),
             "Colombia": getattr(holidays, 'CO'),
             "Croatia": getattr(holidays, 'HR'),
             "Curacao": getattr(holidays, 'CW'),
             "Czechia": getattr(holidays, 'CZ'),
             "Denmark": getattr(holidays, 'DK'),
             "Djibouti": getattr(holidays, 'DJ'),
             "DominicanRepublic": getattr(holidays, 'DO'),
             "Egypt": getattr(holidays, 'EG'),
             "Estonia": getattr(holidays, 'EE'),
             "Ethiopia": getattr(holidays, 'ET'),
             "EuropeanCentralBank": getattr(holidays, 'ECB'),
             "Finland": getattr(holidays, 'FI'),
             "France": getattr(holidays, 'FR'),
             "Georgia": getattr(holidays, 'GE'),
             "Germany": getattr(holidays, 'DE'),
             "Greece": getattr(holidays, 'GR'),
             "Honduras": getattr(holidays, 'HN'),
             "HongKong": getattr(holidays, 'HK'),
             "Hungary": getattr(holidays, 'HU'),
             "Iceland": getattr(holidays, 'IS'),
             "India": getattr(holidays, 'IN'),
             "Ireland": getattr(holidays, 'IE'),
             "Israel": getattr(holidays, 'IL'),
             "Italy": getattr(holidays, 'IT'),
             "Jamaica": getattr(holidays, 'JM'),
             "Japan": getattr(holidays, 'JP'),
             "Kazakhstan": getattr(holidays, 'KZ'),
             "Kenya": getattr(holidays, 'KE'),
             "Korea": getattr(holidays, 'KR'),
             "Latvia": getattr(holidays, 'LV'),
             "Lesotho": getattr(holidays, 'LS'),
             "Lithuania": getattr(holidays, 'LT'),
             "Luxembourg": getattr(holidays, 'LU'),
             "Malaysia": getattr(holidays, 'MY'),
             "Malawi": getattr(holidays, 'MW'),
             "Mexico": getattr(holidays, 'MX'),
             "Morocco": getattr(holidays, 'MA'),
             "Mozambique": getattr(holidays, 'MZ'),
             "Netherlands": getattr(holidays, 'NL'),
             "Namibia": getattr(holidays, 'NA'),
             "NewZealand": getattr(holidays, 'NZ'),
             "Nicaragua": getattr(holidays, 'NI'),
             "Nigeria": getattr(holidays, 'NG'),
             "NorthMacedonia": getattr(holidays, 'MK'),
             "Norway": getattr(holidays, 'NO'),
             "Paraguay": getattr(holidays, 'PY'),
             "Peru": getattr(holidays, 'PE'),
             "Poland": getattr(holidays, 'PL'),
             "Portugal": getattr(holidays, 'PT'),
             "PortugalExt": getattr(holidays, 'PTE'),
             "Romania": getattr(holidays, 'RO'),
             "Russia": getattr(holidays, 'RU'),
             "SaudiArabia": getattr(holidays, 'SA'),
             "Serbia": getattr(holidays, 'RS'),
             "Singapore": getattr(holidays, 'SG'),
             "Slovakia": getattr(holidays, 'SK'),
             "Slovenia": getattr(holidays, 'SI'),
             "SouthAfrica": getattr(holidays, 'ZA'),
             "Spain": getattr(holidays, 'ES'),
             "Swaziland": getattr(holidays, 'SZ'),
             "Sweden": getattr(holidays, 'SE'),
             "Switzerland": getattr(holidays, 'CH'),
             "Taiwan": getattr(holidays, 'TW'),
             "Turkey": getattr(holidays, 'TR'),
             "Tunisia": getattr(holidays, 'TN'),
             "Ukraine": getattr(holidays, 'UA'),
             "UnitedArabEmirates": getattr(holidays, 'AE'),
             "UnitedKingdom": getattr(holidays, 'UK'),
             "UnitedStates": getattr(holidays, 'US'),
             "Venezuela": getattr(holidays, 'VE'),
             "Vietnam": getattr(holidays, 'VN'),
             "Zambia": getattr(holidays, 'ZM'),
             "Zimbabwe": getattr(holidays, 'ZW'),
             }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/days_from_now", methods=['GET', 'POST'])
def days_from_now():
    name = ""
    today_str_txt = TODAY
    today_str = TODAY
    if request.method == "POST" and "input_date" in request.form:
        name = request.form.get("input_date")
        name = days_from_now_logic(name)
        today_str = request.form.get("input_date")
    return render_template("days_from_now.html",
                           name=name,
                           today_str=today_str,
                           today_str_txt=today_str_txt)


@app.route("/week_dates", methods=['GET', 'POST'])
def week_dates():
    today_str = TODAY
    date_1 = ""
    date_Year = ""
    date_Week = ""
    date_2 = ""
    if (request.method == "POST" and "input_Year" in request.form
       and "input_Week" in request.form):
        date_Year = request.form.get("input_Year")
        date_Week = request.form.get("input_Week")
        date_1 = week_dates_logic(date_Year, date_Week)[0]
        date_2 = week_dates_logic(date_Year, date_Week)[1]

    return render_template("week_dates.html",
                           today_str=today_str,
                           date_1=date_1,
                           date_2=date_2)


@app.route("/holiday", methods=['GET', 'POST'])
def holiday_planner():
    generated_list = ''
    choosen_country_flask = ''
    choosen_year_flask = ''
    holiday_list_flask = ''
    if (request.method == "POST"
       and request.form.get("country") in COUNTRIES
       and request.form.get("year") in YEARS):
        generated_list = (calendar_holiday(int(request.form.get("year")),
                                           country=COUNTRIES[
                                           request.form.get("country")]()))
        choosen_country_flask = request.form.get("country")
        choosen_year_flask = request.form.get("year")
        holiday_list_flask = [(f"{date.day}-{date.strftime('%B')} - {name}")
                              for date, name in
                              sorted(COUNTRIES[request.form.get("country")]
                              (years=int(choosen_year_flask)).items())]
    return render_template("holiday.html",
                           generated_list_jinja=generated_list,
                           countries_jinja=COUNTRIES,
                           years_jinja=YEARS,
                           choosen_country_jinja=choosen_country_flask,
                           choosen_year_jinja=choosen_year_flask,
                           holiday_list_jinja=holiday_list_flask)


@app.route("/date_calculator", methods=['GET', 'POST'])
def date_calculator():
    input_years_flask = list(range(51))
    input_months_flask = list(range(51))
    input_weeks_flask = list(range(51))
    input_days_flask = list(range(51))
    result_date_flask = ""
    today_str_txt = TODAY
    today_str = TODAY
    if request.method == "POST" and "input_date" in request.form:
        today_str = request.form.get("input_date")
        input_tuple = (request.form.get("input_date"),
                       request.form.get("operator"),
                       request.form.get("input_years"),
                       request.form.get("input_months"),
                       request.form.get("input_weeks"),
                       request.form.get("input_days"))
        print(input_tuple)
        result_date_flask = date_calculator_function(input_tuple)
    return render_template("date_calculator.html",
                           today_str=today_str,
                           today_str_txt=today_str_txt,
                           input_years_jinja=input_years_flask,
                           input_months_jinja=input_months_flask,
                           input_weeks_jinja=input_weeks_flask,
                           input_days_jinja=input_days_flask,
                           result_date_jinja=result_date_flask)


if __name__ == "__main__":
    app.run(debug=True)
