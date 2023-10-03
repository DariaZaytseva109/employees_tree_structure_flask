from datetime import date
from model import Employee, db, Employee_0, Employee_1, Employee_2, Employee_3, Employee_4


class Employee_logic:
    def __init__(self, fullname, position, salary, boss_id=0, day=date.today()):
        self.fullname = fullname
        self.position = position
        self.day = day
        self.salary = salary
        self.boss_id = boss_id
        self.level = 0



    def add_employee(self):
        if self.boss_id == 0:
            self.level = 0
            self.boss_name = '-'
        else:
            self.level = int(Employee.query.get_or_404(self.boss_id).level) + 1
            self.boss_name = Employee.query.get_or_404(self.boss_id).fullname
        new_employee = Employee(fullname=self.fullname, position=self.position, salary=self.salary, boss_id=self.boss_id, level=self.level, day=self.day, boss_name=self.boss_name)
        db.session.add(new_employee)
        db.session.commit()

        if new_employee.level==0:
            new = Employee_0(id=new_employee.id, fullname=self.fullname, position=self.position, salary=self.salary, day=self.day, level=0, boss_name = self.boss_name)
            db.session.add(new)
        elif new_employee.level==1:
            new = Employee_1(id=new_employee.id, fullname=self.fullname, position=self.position, salary=self.salary, day=self.day, boss_id=self.boss_id, level=1, boss_name = self.boss_name)
            db.session.add(new)
        elif new_employee.level==2:
            new = Employee_2(id=new_employee.id, fullname=self.fullname, position=self.position, salary=self.salary, day=self.day, boss_id=self.boss_id, level=2, boss_name = self.boss_name)
            db.session.add(new)
        elif new_employee.level==3:
            new = Employee_3(id=new_employee.id, fullname=self.fullname, position=self.position, salary=self.salary, day=self.day, boss_id=self.boss_id, level=3, boss_name = self.boss_name)
            db.session.add(new)
        elif new_employee.level==4:
            new = Employee_4(id=new_employee.id, fullname=self.fullname, position=self.position, salary=self.salary, day=self.day, boss_id=self.boss_id, level=4, boss_name = self.boss_name)
            db.session.add(new)
        db.session.commit()

