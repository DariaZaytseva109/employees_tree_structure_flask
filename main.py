from flask import Flask, render_template, request
from model import Employee_0, db, Employee_1, Employee_2, Employee
from logic import Employee_logic
from flask_seeder import FlaskSeeder

from seeds.demo import DemoSeeder

API_ROOT = '/employees/v1/'


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

seeder = FlaskSeeder()
seeder.init_app(app, db)


with app.app_context():
    db.drop_all()
    db.create_all()
    e1 = Employee_logic(fullname='Laurie Stevenson', position='Директор', salary=5000)
    e1.add_employee()
    e2 = Employee_logic(fullname='Michael Washington', position='Зам.Директора', salary=4000, boss_id=1)
    e2.add_employee()
    e3 = Employee_logic(fullname='Robert Jordan', position='Зам.Директор', salary=4000, boss_id=1)
    e3.add_employee()
    e4 = Employee_logic(fullname='Gloria Green', position='Начальник отдела', salary=2000, boss_id=2)
    e4.add_employee()
    e5 = Employee_logic(fullname='Carol Hoffman', position='Начальник отдела', salary=3000, boss_id=3)
    e5.add_employee()
    e6 = Employee_logic(fullname='Linda Reeves', position='Главный менеджер', salary=2400, boss_id=2)
    e6.add_employee()
    a = DemoSeeder()
    a.run()

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
