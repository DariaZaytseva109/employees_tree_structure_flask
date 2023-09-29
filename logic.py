from datetime import date

from model import Employee, db, Employee_0, Employee_1, Employee_2


class Employee_logic:
    def __init__(self, fullname, position, salary, boss_id=0, day=date.today()):
        self.fullname = fullname
        self.position = position
        self.day = day
        self.salary = salary
        self.boss_id = boss_id
        if boss_id==0:
            self.level = 0
        else:
            self.level = Employee.query.get_or_404(self.boss_id).level + 1

    def add_employee(self):
        new_employee = Employee(fullname=self.fullname, position=self.position, salary=self.salary, boss_id=self.boss_id, level=self.level)
        db.session.add(new_employee)
        db.session.commit()

        if new_employee.level==0:
            new = Employee_0(id=new_employee.id, fullname=self.fullname, position=self.position, salary=self.salary)
            db.session.add(new)
        elif new_employee.level==1:
            new = Employee_1(id=new_employee.id, fullname=self.fullname, position=self.position, salary=self.salary, boss_id=self.boss_id)
            db.session.add(new)
        elif new_employee.level==2:
            new = Employee_2(id=new_employee.id, fullname=self.fullname, position=self.position, salary=self.salary, boss_id=self.boss_id)
            db.session.add(new)
        db.session.commit()
        



class Counter:
    def __init__(self):
        self.n = 0