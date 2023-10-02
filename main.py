from datetime import date

from flask import Flask, render_template, request
from flask_seeder import FlaskSeeder

from logic import Employee_logic
from model import Employee_0, db, Employee
from seeds.demo import DemoSeeder


API_ROOT = '/employees/v1/'


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
seeder = FlaskSeeder()
seeder.init_app(app, db)


with app.app_context():  #Заполняю базу первыми лицами компаний, далее - с помощью генератора
    db.drop_all()
    db.create_all()
    e1 = Employee_logic(fullname='Попов Мечеслав Еремеевич', position='Генеральный директор', salary=10000, day=date(2023, 3, 4))
    e1.add_employee()
    e2 = Employee_logic(fullname='Моисеев Осип Глебович', position='Заместитель директора', salary=6000, boss_id=1, day=date(2023, 2, 12))
    e2.add_employee()
    e3 = Employee_logic(fullname='Куликов Устин Львович', position='Финансовый директор', salary=7000, boss_id=1, day=date(2023, 6, 6))
    e3.add_employee()
    e4 = Employee_logic(fullname='Новикова Эрида Пантелеймоновна', position='Глава департамента', salary=4000, boss_id=2, day=date(2023, 1, 30))
    e4.add_employee()
    e5 = Employee_logic(fullname='Носов Иван Натанович', position='Глава департамента', salary=5000, boss_id=3, day=date(2023, 3, 3))
    e5.add_employee()
    e6 = Employee_logic(fullname='Николаева Диана Викторовна', position='Ведущий менеджер', salary=2400, boss_id=2, day=date(2023, 3, 5))
    e6.add_employee()
    e7 = Employee_logic(fullname='Котова Изабелла Валентиновна', position='Администратор', salary=1400, boss_id=6, day=date(2023, 3, 4))
    e7.add_employee()
    a = DemoSeeder()
    a.run()

@app.route(API_ROOT, methods=["GET"])
def show():
    '''view страницы с деревом'''
    employees = Employee_0.query.all()
    return render_template('main_page.html', employees=employees)



@app.route(API_ROOT+'list/<argument>', methods=["GET"])
def sort_by(argument):
    '''view главной страницы со списком всех работников'''
    if argument == 'id':
        employees = Employee.query.order_by(Employee.id).all()
    elif argument == 'fullname':
        employees = Employee.query.order_by(Employee.fullname).all()
    elif argument == 'position':
        employees = Employee.query.order_by(Employee.position).all()
    elif argument == 'day':
        employees = Employee.query.order_by(Employee.day).all()
    elif argument == 'salary':
        employees = Employee.query.order_by(Employee.salary).all()
    return render_template('main_page_2.html', employees=employees)




@app.route(API_ROOT, methods=["POST"])
def create():
    '''создание работника'''
    data = request.get_data().decode('utf-8')
    lst = data.split()
    fullname = lst[0]
    position = lst[1]
    salary = int(lst[2])
    boss_id = int(lst[3])
    new_employee = Employee_logic(fullname=fullname, position=position, salary=salary, boss_id=boss_id)
    new_employee.add_employee()



if __name__ == '__main__':
    app.run(debug=True)
