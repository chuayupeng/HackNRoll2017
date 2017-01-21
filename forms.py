from wtforms import SubmitField, SelectField, StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, NumberRange, Length
from wtforms_components import DateField, TimeField
from flask_wtf import FlaskForm

class StepOneForm(FlaskForm):
    age = IntegerField('Age', validators=[NumberRange(min=20, max=90, 
        message="Please enter an age between 20 and 90."), InputRequired()])
    salary = IntegerField('Current Salary', validators=[NumberRange(min=0, 
        message="Please enter a salary of at least 0."), InputRequired()])
    savings = IntegerField('Current Savings', validators=[NumberRange(min=0, 
        message="How much have you saved up? Don't enter negative numbers; we'll ask you about loans later."), InputRequired()])
    perc_saved = IntegerField('% of Salary Saved', validators=[NumberRange(min=0, max=100,
        message="Please enter a number between 0 and 100."), InputRequired()])
    submit       = SubmitField()


class StepTwoForm(FlaskForm):
    cpf_oa = IntegerField('Ordinary Account', validators=[NumberRange(min=0, 
        message="Please enter a value greater than or equal to 0."), InputRequired()])
    cpf_sa = IntegerField('Special Account', validators=[NumberRange(min=0, 
        message="Please enter a value greater than or equal to 0."), InputRequired()])
    cpf_ma = IntegerField('Medisave Account', validators=[NumberRange(min=0, 
        message="Please enter a value greater than or equal to 0."), InputRequired()])
    cpf_ra = IntegerField('Retirement Account', validators=[NumberRange(min=0,
        message="Please enter a value greater than or equal to 0."), InputRequired()])
    submit       = SubmitField()


class StepThreeForm(FlaskForm):
    loan_monthly_repayment = IntegerField('Loan Monthly Repayment', validators=[NumberRange(min=0, 
        message="Please enter a value greater than or equal to 0."), InputRequired()])
    loan_months_left = IntegerField('Months left to repay loan', validators=[NumberRange(min=0, 
        message="Please enter a value greater than or equal to 0."), InputRequired()])
    house_price = IntegerField('House Price', validators=[NumberRange(min=0, 
        message="Please enter a value greater than or equal to 0."), InputRequired()])
    house_buy_age = IntegerField('Age when buying house', validators=[NumberRange(min=18,
        message="Please enter a number greater than your current age."), InputRequired()])
    house_perc_loan = IntegerField('Percentage Taken on Housing Loan', validators=[NumberRange(min=0, max=100,
        message="Please enter a number between 0 and 100."), InputRequired()])
    house_loan_years = SelectField('Loan Duration (Years)', choices=[('20', '20'), ('25', '25'), ('30', '30'), ('35', '35')])
    house_int_rate = IntegerField('Fixed Interest Rate (%)', validators=[NumberRange(min=0, max=100,
        message="Please enter a number between 0 and 100."), InputRequired()])
    submit       = SubmitField()
