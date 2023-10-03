from datetime import date
from model import Employee, db


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


