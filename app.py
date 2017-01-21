from flask import Flask, render_template, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap
from forms import *
from gsheets import googleSheet
import json

app = Flask(__name__)
app.secret_key = 'lkgknwlkknflkewfnokwek'
GSHEET_KEY = '12UCWPoJ46pMkE5DGZJiy303xQ1GYUGyHB8R5uf6TuPM'

bootstrap = Bootstrap()
bootstrap.init_app(app)

# MAGIC VALUES
CHART_DATA_TITLE = "Charts"

# Basics
AGE_CELL = "B2"
SALARY_CELL = "B3"
SAVINGS_CELL = "B4"
PERCENT_SAVED_PER_MONTH = "B13"

# Advanced
PERCENT_INCREASE_SALARY = "B11"
PERCENT_SAVINGS_INTEREST = "B15"
PERCENT_REDUCED_EXP = "B16"
INFLATION_RATE = "B18"
DESIRED_RETIREMENT_AGE = "B19"

# CPF
O_ACC = "B6"
S_ACC = "B7"
M_ACC = "B8"
R_ACC = "B9"

# Major Loans

LOANS_M_REPAY = "D2"
LOANS_M_LEFT = "D3"

H_PRICE = "D6"
H_BUY_AGE = "D7"
H_PERCENT_LOAN = "D8"
H_LOAN_YEARS = "D9"
H_INTEREST_RATE = "D10"


@app.route('/', methods=['GET', 'POST'])
def step1():
    form = StepOneForm()
    if form.validate_on_submit():
        gs = googleSheet(GSHEET_KEY)
        gs.update_cell(AGE_CELL, form.age.data)
        gs.update_cell(SALARY_CELL, form.salary.data)
        gs.update_cell(SAVINGS_CELL, form.savings.data)
        gs.update_cell(PERCENT_SAVED_PER_MONTH, form.perc_saved.data)

        return redirect(url_for('step2'))
    return render_template('step1.html', form = form)

@app.route('/step2', methods=['GET', 'POST'])
def step2():
    form = StepTwoForm()
    if form.validate_on_submit():
        # TODO: update values in gspread
        return redirect(url_for('step3'))
    return render_template('step2.html', form=form)

@app.route('/step3', methods=['GET', 'POST'])
def step3():
    form = StepThreeForm()
    if form.validate_on_submit():
        curr_age = googleSheet(GSHEET_KEY).getWorksheet(0).acell(AGE_CELL)
        if form.house_buy_age.data < curr_age:
            return render_template('step3.html', form=form)
        return redirect(url_for('final'))
    return render_template('step3.html', form=form)

@app.route('/final', methods=['GET', 'POST'])
def final():
    return render_template('final.html')

@app.route('/chart_data', methods=['GET', 'POST'])
def get_chart_data():
    data = googleSheet(GSHEET_KEY).get_chart_data()
    title = data[0]

    output = []
    for row in data[1:]:
        if '' not in row:
            d = {}
            for i in range(len(title)):
                d[title[i]] = int(float(row[i].replace("$", "").replace(",", "")))
            output.append(d)

    return json.dumps(output)


if __name__ == "__main__":
    app.run()
