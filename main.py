from flask import Flask, render_template, request
from sqlalchemy.orm import DeclarativeBase
from datetime import date
from model import Employee_0, db, Employee_1, Employee_2, Employee
from logic import Employee_logic

API_ROOT = '/employees/v1/'


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

@app.route(API_ROOT, methods=["GET"])
def show():
    '''view главной страницы'''
    employees = Employee_0.query.all()
    return render_template('main_page.html', employees=employees)


@app.route(API_ROOT+'all/', methods=["GET"])
def show_all():
    '''view главной страницы'''
    employees = Employee.query.all()
    return render_template('main_page_2.html', employees=employees)

@app.route(API_ROOT, methods=["POST"])
def create():
    '''создание работника'''
    data = request.get_data().decode('utf-8')

    lst = data.split()
    print(lst)
    fullname = lst[0]
    position = lst[1]
    salary = int(lst[2])
    boss_id = int(lst[3])

    print(boss_id)
    new_employee = Employee_logic(fullname=fullname, position=position, salary=salary, boss_id=boss_id)
    print(new_employee)
    new_employee.add_employee()
    return render_template('1.html')

if __name__ == '__main__':
    app.run(debug=True)
