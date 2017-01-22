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
AGE_CELL = "I2"
SALARY_CELL = "I3"
SAVINGS_CELL = "I4"
PERCENT_SAVED_PER_MONTH = "I9"

# Advanced
PERCENT_INCREASE_SALARY = "I17"
PERCENT_SAVINGS_INTEREST = "I18"
PERCENT_REDUCED_EXP = "I19"
INFLATION_RATE = "I20"
DESIRED_RETIREMENT_AGE = "I21"

# CPF
O_ACC = "I5"
S_ACC = "I6"
M_ACC = "I7"
R_ACC = "I8"

# Major Loans

LOANS_M_REPAY = "I10"
LOANS_M_LEFT = "I11"

H_PRICE = "I12"
H_BUY_AGE = "I13"
H_PERCENT_LOAN = "I14"
H_LOAN_YEARS = "I15"
H_INTEREST_RATE = "I16"


@app.route('/', methods=['GET', 'POST'])
def step1():
    form = StepOneForm()
    if form.validate_on_submit():
        gs = googleSheet(GSHEET_KEY)
        gs.update_cell(AGE_CELL, form.age.data)
        gs.update_cell(SALARY_CELL, form.salary.data)
        gs.update_cell(SAVINGS_CELL, form.savings.data)
        gs.update_cell(PERCENT_SAVED_PER_MONTH, form.perc_saved.data)

        # TODO: Advanced Options
        return redirect(url_for('step2'))

    gs = googleSheet(GSHEET_KEY)
    worksheet = gs.inputArea
    cell_list = worksheet.range('I3:I12')
    for cell in cell_list:
        cell.value = 0
    worksheet.update_cells(cell_list)
    return render_template('step1.html', form = form)

@app.route('/step2', methods=['GET', 'POST'])
def step2():
    form = StepTwoForm()
    if form.validate_on_submit():
        gs = googleSheet(GSHEET_KEY)
        gs.update_cell(O_ACC, form.cpf_oa.data)
        gs.update_cell(S_ACC, form.cpf_sa.data)
        gs.update_cell(M_ACC, form.cpf_ma.data)
        gs.update_cell(R_ACC, form.cpf_ra.data)

        return redirect(url_for('step3'))
    return render_template('step2.html', form=form)

@app.route('/step3', methods=['GET', 'POST'])
def step3():
    form = StepThreeForm()
    if form.validate_on_submit():
        gs = googleSheet(GSHEET_KEY)
        curr_age = int(gs.inputArea.acell(AGE_CELL).value)
        if form.house_buy_age.data < curr_age:
            return render_template('step3.html', form=form)

        gs.update_cell(LOANS_M_REPAY, form.loan_monthly_repayment.data)
        gs.update_cell(LOANS_M_LEFT, form.loan_months_left.data)
        gs.update_cell(H_PRICE, form.house_price.data)
        gs.update_cell(H_BUY_AGE, form.house_buy_age.data)
        gs.update_cell(H_PERCENT_LOAN, form.house_perc_loan.data)
        gs.update_cell(H_LOAN_YEARS, form.house_loan_years.data)
        gs.update_cell(H_INTEREST_RATE, form.house_int_rate.data)
        return redirect(url_for('final'))
    return render_template('step3.html', form=form)

@app.route('/final', methods=['GET', 'POST'])
def final():
    return render_template('final.html')

@app.route('/chart_data', methods=['GET', 'POST'])
def get_chart_data():
    data = googleSheet(GSHEET_KEY).get_chart_data()
    titles = data[0]
    d = {}
    
    for row in data[1:]:
        if '' not in row:
            for i in range(len(titles)):
                if not d.get(titles[i]):
                    d[titles[i]] = []
                d[titles[i]].append(int(float(row[i].replace("$", "").replace(",", ""))))

    return json.dumps(d)


if __name__ == "__main__":
    app.run()
